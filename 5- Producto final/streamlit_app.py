import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from ml_model import obtener_grafico, obtener_ventas_en_fecha

st.markdown("<h3 style='text-align: center; color: #1f3541;'>OLIST Store Dashboard</h3>", unsafe_allow_html=True)

power_bi_report_url = "https://app.powerbi.com/view?r=eyJrIjoiNTM4N2I1NmQtY2ZhMi00NGZkLWI3MjgtOTgwMTYxNjAyNTQ3IiwidCI6ImE3ZWMwMGM2LTAxZDAtNDc0OS1iNjhmLWFmYThmM2IwYjE0YyIsImMiOjR9"

st.markdown(f'<iframe width="800" height="636" src="{power_bi_report_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)


st.markdown("<h3 style='text-align: center; color: #1f3541;'>OLIST Store ML Model</h3>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: #1f3541;'>Gráfico de Ventas Reales vs Predicciones</h5>", unsafe_allow_html=True)

# Streamlit: Mostrar el gráfico
try:
    plt, df_monthly, predicciones_df = obtener_grafico()
    st.pyplot(plt)

    # Agregar un widget para seleccionar una fecha
    fecha_seleccionada = st.date_input("Selecciona un mes y año:", value=predicciones_df.index[-1], min_value=predicciones_df.index.min(), max_value=predicciones_df.index.max())

    # Llama a la función para obtener el valor de las ventas en la fecha seleccionada
    ventas_predichas = obtener_ventas_en_fecha(predicciones_df, fecha_seleccionada)

    # Muestra el valor de las ventas en la fecha seleccionada
    st.write(f'Valor de las ventas predichas en {fecha_seleccionada}: {ventas_predichas}')
except Exception as e:
    print("ERROR OBTENIENDO EL GRAFICO", e)
