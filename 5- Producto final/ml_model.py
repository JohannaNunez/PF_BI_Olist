import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
import datetime

from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA

from dbConnection import db_instance

def obtener_datos_desde_mysql():
    # Utilizar el método get_data_from_query de db_instance para obtener los datos de MySQL
    query_orders = "SELECT * FROM public.orders"
    df5 = db_instance.get_data_from_query(query_orders)

    query_payments = "SELECT * FROM public.order_payments"
    df6 = db_instance.get_data_from_query(query_payments)

    return df5, df6

def calcular_pago_por_orden(df6):
    # Agrupar por 'order_id' y sumar 'payment_value'
    df6pagos = df6.groupby('order_id')['payment_value'].sum().reset_index()

    # Renombrar la columna de sumas como 'pago_orden'
    df6pagos.rename(columns={'payment_value': 'pago_orden'}, inplace=True)

    return df6pagos

def procesar_datos(df5, df6pagos):
    df5.columns = ['order_id', 'order_status', 'order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date', 'customer_id']
    df6pagos.columns = ['order_id', 'pago_orden']

    # Fusionar los DataFrames en uno solo basado en el campo 'order_id'
    merged_df = pd.merge(df5, df6pagos, on='order_id', how='inner')  # Fusionar DF5 y DF6pagos por 'order_id'

    return merged_df

def crear_columna_pago_orden(merged_df):
    # Crear una copia del DataFrame original para no modificar el original
    dfextra = merged_df.copy().reset_index()

    # Filtrar merged_df por order_status igual a "delivered"
    dfextra2 = dfextra[dfextra['order_status'] == 'delivered'].copy()
    columnas_a_mantener = ['order_id', 'order_purchase_timestamp', 'pago_orden']
    dfventas = dfextra2[columnas_a_mantener]
    return dfventas

def agrupar_por_mes(dfventas):
    # Convertir 'order_purchase_timestamp' a tipo datetime
    dfventas['order_purchase_timestamp'] = pd.to_datetime(dfventas['order_purchase_timestamp'])

    # Establecer 'order_purchase_timestamp' como índice
    dfventas.set_index('order_purchase_timestamp', inplace=True)

    # Agrupar por mes y sumar los valores
    dfventas.drop('order_id', axis=1, inplace=True)

    df_monthly = dfventas.resample('M').sum()

    return df_monthly

def diferencia_y_arima(df_monthly):
    # Diferenciación
    df_diff = df_monthly['pago_orden'].diff().dropna()
    # Realizar nuevamente la prueba de Dickey-Fuller
    #result_diff = adfuller(df_diff)
    #print('ADF Statistic:', result_diff[0])
    #print('p-value:', result_diff[1])

    # Ajustar el modelo ARIMA(x,x,x) a los datos diferenciados
    model = ARIMA(df_monthly, order=(2, 0, 3))
    model_fit = model.fit()

    # Retornar el modelo ajustado
    return model_fit

def hacer_predicciones(model_fit, steps=100):
    # Realizar predicciones para los próximos 'steps' períodos
    predicciones = model_fit.get_forecast(steps=steps)
    pred_interval = predicciones.conf_int()

    # Obtener las predicciones
    predicciones_mean = predicciones.predicted_mean

    # Retornar las predicciones
    return predicciones_mean

def obtener_grafico():
    df5, df6 = obtener_datos_desde_mysql()
    df6pagos = calcular_pago_por_orden(df6)
    merged_df = procesar_datos(df5, df6pagos)
    dfventas = crear_columna_pago_orden(merged_df)
    df_monthly = agrupar_por_mes(dfventas)
    model_arima = diferencia_y_arima(df_monthly)
    predicciones = hacer_predicciones(model_arima)

    # Convertir la serie de predicciones en un DataFrame para la graficación
    predicciones_df = pd.DataFrame(predicciones)
    predicciones_df.index = pd.to_datetime(predicciones_df.index)
    predicciones_df['predicted_mean'] = predicciones_df['predicted_mean'].astype(float)

    # Graficar df_monthly y las predicciones
    plt.figure(figsize=(14, 7))
    plt.plot(df_monthly['pago_orden'], label='Ventas Reales', marker='o')
    plt.plot(predicciones_df['predicted_mean'], label='Ventas Predichas', marker='x', linestyle='--')
    plt.title('Ventas Reales vs Predicciones')
    plt.xlabel('Fecha')
    plt.ylabel('Pago de la Orden')
    plt.legend()
    plt.grid(True)
    plt.show()

    return plt, df_monthly, predicciones_df


def obtener_ventas_en_fecha(predicciones_df, fecha_seleccionada):
    # Obtener el valor de las ventas en la fecha seleccionada
    # Filtrar el DataFrame según la fecha seleccionada
    # Verificar si la fecha seleccionada está presente en el índice de predicciones_df
    fecha_seleccionada = pd.to_datetime(fecha_seleccionada)
    mes_seleccionado = fecha_seleccionada.month
    año_seleccionado = fecha_seleccionada.year

    # Filtrar el DataFrame para obtener las ventas del mes y año seleccionados
    df_filtrado = predicciones_df[
        (predicciones_df.index.month == mes_seleccionado) & (predicciones_df.index.year == año_seleccionado)]

    # Verificar si hay ventas para el mes y año seleccionados
    if not df_filtrado.empty:
        # Obtener las ventas reales y predichas para el mes y año seleccionados
        ventas_predichas = predicciones_df[
            (predicciones_df.index.month == mes_seleccionado) & (predicciones_df.index.year == año_seleccionado)
        ]['predicted_mean'].iloc[0]
        return ventas_predichas
    else:
        return ""