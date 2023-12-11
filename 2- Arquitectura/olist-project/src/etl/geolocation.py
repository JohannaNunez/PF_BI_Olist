import pandas as pd
import os

from settings.url_constants import DATASETS_DIR, DATASOURCES_DIR
from src.etl.etl_functions import export_to_csv, capitalize_text
from src.models.dbConnection import db_instance
from src.models.apiDto import TransferMethod

def clean_olist_geolocation_dataset():
    # Leemos el csv con pandas
    df_geolocation=pd.read_csv(f'{DATASETS_DIR}/olist_geolocation_dataset.csv')

    # LIMPIEZA Y TRANSFORMACIÓN DE DATOS 

    ### geolocation: 
    
    # Eliminamos campos donde haya null y duplicados
    df_geolocation['geolocation_zip_code_prefix'].dropna(inplace=True)
    df_geolocation.drop_duplicates(subset='geolocation_zip_code_prefix', inplace=True)
    df_geolocation['geolocation_lat'].dropna(inplace=True)
    df_geolocation['geolocation_lng'].dropna(inplace=True)

    # Buscamos previamente ciudades a normalizar con ayuda de la funcion find_similar_words 
    df_geolocation['geolocation_city'] = df_geolocation['geolocation_city'].str.replace("arraial d ajuda", "arraial d'ajuda")
    df_geolocation['geolocation_city'] = df_geolocation['geolocation_city'].str.replace("dias d avila", "dias d'avila")
    df_geolocation['geolocation_city'] = df_geolocation['geolocation_city'].str.replace("estrela d oeste", "estrela d'oeste")
    df_geolocation['geolocation_city'] = df_geolocation['geolocation_city'].str.replace("mogi-mirim", "mogi mirim")
    df_geolocation['geolocation_city'] = df_geolocation['geolocation_city'].str.replace("palmeira d oeste", "palmeira d'oeste")
    df_geolocation['geolocation_city'] = df_geolocation['geolocation_city'].str.replace("santa barbara d oeste", "santa barbara d'oeste")

    # Capitalizamos los nombres de las ciudades
    df_geolocation["geolocation_city"] = capitalize_text(df_geolocation, "geolocation_city")

    # Aseguramos el orden de las columnas 

    ordered_columns = ["geolocation_zip_code_prefix", "geolocation_lat", "geolocation_lng", "geolocation_city", "geolocation_state"]
    df_geolocation = df_geolocation[ordered_columns]

    # Exportamos df a csv para su posterior carga
    csv_path = f'{DATASOURCES_DIR}/geolocation.csv'
    export_to_csv(df_geolocation, csv_path)

    return os.path.exists(csv_path)

def load_clean_geolocation_dataset():
    # Subimos el csv a la base de datos
    csv_path = f'{DATASOURCES_DIR}/geolocation.csv'
    rows_imported = db_instance.load_csv_to_db(csv_path, "geolocation")
    return rows_imported

def transfer_stg_to_prod_geolocation(method):
    if method == TransferMethod.SP:
        rows_transfered = db_instance.exec_procedure("transfer_data_from_stg_to_geolocation")
    else:
        rows_transfered = db_instance.transfer_stg_to_prod_table("geolocation")
    return rows_transfered