import pandas as pd
import os

from settings.url_constants import DATASETS_DIR, DATASOURCES_DIR
from src.etl.etl_functions import export_to_csv
from src.models.dbConnection import db_instance

def clean_olist_order_payments_dataset():
    # Leemos el csv con pandas
    df_order_payments=pd.read_csv(f'{DATASETS_DIR}/olist_order_payments_dataset.csv')

    # LIMPIEZA Y TRANSFORMACIÓN DE DATOS 

    ### order_payments:

    # Aseguramos el orden de las columnas
    ordered_columns = ["payment_sequential", "payment_type", "payment_installments", "payment_value", "order_id"]
    df_order_payments = df_order_payments[ordered_columns]

    # Exportamos df a csv para su posterior carga
    csv_path = f'{DATASOURCES_DIR}/order_payments.csv'
    export_to_csv(df_order_payments, csv_path)

    return os.path.exists(csv_path)

def load_clean_order_payments_dataset():
    # Subimos el csv a la base de datos
    csv_path = f'{DATASOURCES_DIR}/order_payments.csv'
    rows_imported = db_instance.load_csv_to_db(csv_path, "order_payments")
    return rows_imported

def transfer_stg_to_prod_order_payments():
    rows_transfered = db_instance.transfer_stg_to_prod_table("order_payments")
    return rows_transfered