import pandas as pd
import os

from settings.url_constants import DATASETS_DIR, DATASOURCES_DIR
from etl.etl_functions import format_str_to_datetime, export_to_csv
from src.models.dbConnection import db_instance

def clean_olist_order_items_dataset():
    # Leemos el csv con pandas
    df_order_items=pd.read_csv(f'{DATASETS_DIR}/olist_order_items_dataset.csv')

    # LIMPIEZA Y TRANSFORMACIÓN DE DATOS 

    ### order_items

    # Formateamos los campos de fecha
    format_str_to_datetime(df_order_items,'shipping_limit_date')

    # Aseguramos el orden de las columnas
    ordered_columns = ["order_item_id", "shipping_limit_date", "price", "freight_value", "order_id", "product_id", "seller_id"]
    df_order_items = df_order_items[ordered_columns]

    # Exportamos df a csv para su posterior carga
    csv_path = f'{DATASOURCES_DIR}/order_items.csv'
    export_to_csv(df_order_items, csv_path)

    return os.path.exists(csv_path)

def load_clean_order_items_dataset():
    # Subimos el csv a la base de datos
    csv_path = f'{DATASOURCES_DIR}/order_items.csv'
    rows_imported = db_instance.load_csv_to_db(csv_path, "order_items")
    return rows_imported

def transfer_stg_to_prod_order_items():
    rows_transfered = db_instance.transfer_stg_to_prod_table("order_items")
    return rows_transfered