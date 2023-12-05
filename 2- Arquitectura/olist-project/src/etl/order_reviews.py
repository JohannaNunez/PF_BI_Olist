import pandas as pd
import os

from settings.url_constants import DATASETS_DIR, DATASOURCES_DIR
from etl.etl_functions import format_str_to_datetime, export_to_csv
from src.models.dbConnection import db_instance

def clean_olist_order_reviews_dataset():
    # Leemos el csv con pandas
    df_order_reviews=pd.read_csv(f'{DATASETS_DIR}/olist_order_reviews_dataset.csv')

    # LIMPIEZA Y TRANSFORMACIÓN DE DATOS 

    ### order_reviews:

    # Formateamos los campos de fecha
    format_str_to_datetime(df_order_reviews,'review_creation_date')
    format_str_to_datetime(df_order_reviews,'review_answer_timestamp')

    # Descartamos columnas que no serán utilizadas
    df_order_reviews = df_order_reviews.drop(columns=["review_comment_title", "review_comment_message"])

    # Aseguramos el orden de las columnas
    ordered_columns = ["review_id", "review_score", "review_creation_date", "review_answer_timestamp", "order_id"]
    df_order_reviews = df_order_reviews[ordered_columns]

    # Exportamos df a csv para su posterior carga
    csv_path = f'{DATASOURCES_DIR}/order_reviews.csv'
    export_to_csv(df_order_reviews, csv_path)

    return os.path.exists(csv_path)

def load_clean_order_reviews_dataset():
    # Subimos el csv a la base de datos
    csv_path = f'{DATASOURCES_DIR}/order_reviews.csv'
    rows_imported = db_instance.load_csv_to_db(csv_path, "order_reviews")
    return rows_imported

def transfer_stg_to_prod_order_reviews():
    rows_transfered = db_instance.transfer_stg_to_prod_table("order_reviews")
    return rows_transfered