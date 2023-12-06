import pandas as pd
import os

from settings.url_constants import DATASETS_DIR, DATASOURCES_DIR
from etl.etl_functions import format_str_to_datetime, export_to_csv
from src.models.dbConnection import db_instance
from src.models.apiDto import TransferMethod

def clean_olist_orders_dataset():
    # Leemos el csv con pandas
    df_orders=pd.read_csv(f'{DATASETS_DIR}/olist_orders_dataset.csv')

    # LIMPIEZA Y TRANSFORMACIÓN DE DATOS 

    ### orders

    # Formateamos los campos de fecha
    format_str_to_datetime(df_orders,'order_purchase_timestamp')
    format_str_to_datetime(df_orders,'order_approved_at')
    format_str_to_datetime(df_orders,'order_delivered_carrier_date')
    format_str_to_datetime(df_orders,'order_delivered_customer_date')
    format_str_to_datetime(df_orders,'order_estimated_delivery_date')

    # Aseguramos el orden de las columnas
    ordered_columns = ["order_id", "order_status", "order_purchase_timestamp", "order_approved_at", "order_delivered_carrier_date", "order_delivered_customer_date", "order_estimated_delivery_date", "customer_id"]
    df_orders = df_orders[ordered_columns]

    # Exportamos df a csv para su posterior carga
    csv_path = f'{DATASOURCES_DIR}/orders.csv'
    export_to_csv(df_orders, csv_path)

    return os.path.exists(csv_path)

def load_clean_orders_dataset():
    # Subimos el csv a la base de datos
    csv_path = f'{DATASOURCES_DIR}/orders.csv'
    rows_imported = db_instance.load_csv_to_db(csv_path, "orders")
    return rows_imported

def transfer_stg_to_prod_orders(method):
    if method == TransferMethod.SP:
        rows_transfered = db_instance.exec_procedure("transfer_data_from_stg_to_orders")
    else:
        rows_transfered = db_instance.transfer_stg_to_prod_table("orders")
    return rows_transfered