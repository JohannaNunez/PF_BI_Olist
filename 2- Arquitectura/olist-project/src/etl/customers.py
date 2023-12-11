import pandas as pd
import os

from settings.url_constants import DATASETS_DIR, DATASOURCES_DIR
from src.etl.etl_functions import UNSPECIFIED, export_to_csv, capitalize_text
from src.models.dbConnection import db_instance
from src.models.apiDto import TransferMethod

def clean_olist_customers_dataset():
    # Leemos el csv con pandas
    df_customers=pd.read_csv(f'{DATASETS_DIR}/olist_customers_dataset.csv')

    # LIMPIEZA Y TRANSFORMACIÓN DE DATOS 

    ### customers:

    # Eliminamos la columna de customer_unique_id porque tiene duplicados, y utilizaremos customer_id
    df_customers.drop(columns='customer_unique_id', inplace=True)

    # Buscamos previamente ciudades a normalizar con ayuda de la funcion find_similar_words y a partir del resultado transformamos lo necesario (ver archivo customer_city_similar_words.txt)
    df_customers['customer_city'] = df_customers['customer_city'].str.replace("arraial d ajuda", "arraial d'ajuda")
    df_customers['customer_city'] = df_customers['customer_city'].str.replace("dias d avila", "dias d'avila")
    df_customers['customer_city'] = df_customers['customer_city'].str.replace("estrela d oeste", "estrela d'oeste")
    df_customers['customer_city'] = df_customers['customer_city'].str.replace("mogi-mirim", "mogi mirim")
    df_customers['customer_city'] = df_customers['customer_city'].str.replace("palmeira d oeste", "palmeira d'oeste")
    df_customers['customer_city'] = df_customers['customer_city'].str.replace("santa barbara d oeste", "santa barbara d'oeste")

    # Capitalizamos los nombres de las ciudades
    df_customers["customer_city"] = capitalize_text(df_customers, "customer_city")

    # Aseguramos los campos que no deben ser null 
    df_customers['customer_zip_code_prefix'].fillna(UNSPECIFIED, inplace=True)
    df_customers['customer_city'].fillna(UNSPECIFIED, inplace=True)
    df_customers['customer_state'].fillna(UNSPECIFIED, inplace=True)

    # Aseguramos el orden de las columnas
    ordered_columns = ["customer_id", "customer_zip_code_prefix", "customer_city", "customer_state"]
    df_customers = df_customers[ordered_columns]

    # Exportamos df a csv para su posterior carga
    csv_path = f'{DATASOURCES_DIR}/customer.csv'
    export_to_csv(df_customers, csv_path)

    return os.path.exists(csv_path)

def load_clean_customers_dataset():
    # Subimos el csv a la base de datos
    csv_path = f'{DATASOURCES_DIR}/customer.csv'
    rows_imported = db_instance.load_csv_to_db(csv_path, "customers")
    return rows_imported

def transfer_stg_to_prod_customers(method):
    if method == TransferMethod.SP:
        rows_transfered = db_instance.exec_procedure("transfer_data_from_stg_to_customers")
    else:
        rows_transfered = db_instance.transfer_stg_to_prod_table("customers")
    return rows_transfered