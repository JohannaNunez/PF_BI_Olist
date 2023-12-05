import pandas as pd
import os

from settings.url_constants import DATASETS_DIR, DATASOURCES_DIR
from etl.etl_functions import UNSPECIFIED, export_to_csv
from src.models.dbConnection import db_instance

def clean_olist_products_dataset():
    # Abrimos los datasets en dataframe de pandas
    df_products=pd.read_csv(f'{DATASETS_DIR}/olist_products_dataset.csv')

    # LIMPIEZA Y TRANSFORMACIÓN DE DATOS 

    ### products:

    # Reemplazamos los null por variable reservada para no especificado
    df_products['product_category_name'] = df_products['product_category_name'].fillna(UNSPECIFIED)

    # Reemplazamos los guiones bajos por espacio y capitalizamos
    df_products['product_category_name'] = df_products['product_category_name'].str.replace("_2", "").str.replace("_", " ").str.upper()

    # Renombramos columnas segun el esquema
    df_products.rename(columns = {'product_name_lenght':'product_name_length', 'product_description_lenght': 'product_description_length'}, inplace = True)

    # Aseguramos el orden de las columnas
    ordered_columns = ["product_id", "product_category_name", "product_name_length", "product_description_length", "product_photos_qty", "product_weight_g", "product_length_cm", "product_height_cm", "product_width_cm"]
    df_products = df_products[ordered_columns]

    # Exportamos df a csv para su posterior carga
    csv_path = f'{DATASOURCES_DIR}/products.csv'
    export_to_csv(df_products, csv_path)

    return os.path.exists(csv_path)

def load_clean_products_dataset():
    # Subimos el csv a la base de datos
    csv_path = f'{DATASOURCES_DIR}/products.csv'
    rows_imported = db_instance.load_csv_to_db(csv_path, "products")
    return rows_imported

def transfer_stg_to_prod_products():
    rows_transfered = db_instance.transfer_stg_to_prod_table("products")
    return rows_transfered