import pandas as pd
import os

from settings.url_constants import DATASETS_DIR, DATASOURCES_DIR
from etl.etl_functions import UNSPECIFIED, export_to_csv
from src.models.dbConnection import db_instance

def clean_product_category_name_translation():
    # Abrimos los datasets en dataframe de pandas
    df_category_name=pd.read_csv(f'{DATASETS_DIR}/product_category_name_translation.csv')

    # LIMPIEZA Y TRANSFORMACIÓN DE DATOS 

    ### product_category_name:

    # Reemplazamos los guiones bajos por espacio, los duplicados y capitalizamos
    df_category_name['product_category_name'] = df_category_name['product_category_name'].str.replace("_2", "").str.replace("_", " ").str.upper()
    df_category_name['product_category_name_english'] = df_category_name['product_category_name_english'].str.replace("_2", "").str.replace("_", " ").str.upper()
    df_category_name.drop_duplicates(subset='product_category_name', inplace=True)
    df_category_name.drop_duplicates(subset='product_category_name_english', inplace=True)


    # Agregamos categorías que figuran en products y no tienen traducción
    missing_categories = [{'product_category_name': "PC GAMER", 'product_category_name_english': "PC GAMER"}, {'product_category_name': "PORTATEIS COZINHA E PREPARADORES DE ALIMENTOS", 'product_category_name_english': "KITCHEN PORTABLES AND FOOD PREPARATION"}]
    df_category_name = pd.concat([df_category_name, pd.DataFrame(missing_categories)], ignore_index=True)
    # Agregamos un registro para los valores no especificados
    unspecified_product_name = {'product_category_name': UNSPECIFIED, 'product_category_name_english': "N/S"}
    df_category_name = pd.concat([df_category_name, pd.DataFrame([unspecified_product_name])], ignore_index=True)

    # Aseguramos el orden de las columnas
    ordered_columns = ["product_category_name", "product_category_name_english"]
    df_category_name = df_category_name[ordered_columns]

    # Exportamos df a csv para su posterior carga
    csv_path = f'{DATASOURCES_DIR}/product_category_name_translation.csv'
    export_to_csv(df_category_name, csv_path)

    return os.path.exists(csv_path)

def load_clean_product_category_name_translation_dataset():
    # Subimos el csv a la base de datos
    csv_path = f'{DATASOURCES_DIR}/product_category_name_translation.csv'
    rows_imported = db_instance.load_csv_to_db(csv_path, "product_category_name_translation")
    return rows_imported

def transfer_stg_to_prod_product_category_name_translation():
    rows_transfered = db_instance.transfer_stg_to_prod_table("product_category_name_translation")
    return rows_transfered