# Funciones para ETL
import pandas as pd

from src.utils.log import logInfo

# Constantes de imputación en nulos de variables categóricas
UNSPECIFIED = "N/E" 
NOT_APPLY = "N/A"

def format_str_to_datetime(df, column):
    """
    Recibe un dataframe y el nombre de una columna
    Convierte a fecha los valores de la columna
    """
    try:
        df[column] = pd.to_datetime(df[column], format='%Y-%m-%d %H:%M:%S')
    except ValueError:
        logInfo(f"Error al convertir la columna {column} a tipo fecha y hora.")

def format_to_int_type(df, columna):
    """
    Recibe un dataframe y el nombre de una columna
    Convierte a int los valores de la columna
    """
    try:
        df[columna] = df[columna].astype(int)
    except ValueError as e:
        logInfo(f"Error al convertir los valores de la columna '{columna}' a tipo entero: {e}")

def export_to_csv(df, url_path):  
    """
    Recibe un dataframe y url destino del archivo
    Exporta el df a csv
    """
    try:
        df.to_csv(url_path, index=False)
    except ValueError as e:
        logInfo(f"Error al exportar {url_path}, error:{e}")

def trim_string(df, column):
    """
    Recibe un dataframe y el nombre de una columna
    Recorta espacios sobrantes de la cadena
    """
    try:
        df[column] = df[column].str.strip()
    except AttributeError:
        logInfo(f"Error al limpiar espacios en la columna {column}.")

def capitalize_text(df, column):
    """
    Recibe un dataframe y el nombre de una columna
    Capitaliza las palabras de la cadena
    """
    try:
        df[column] = df[column].apply(lambda x: x.capitalize())
    except AttributeError:
        logInfo(f"Error al capitalizar texto en la columna {column}.")

def symbol_remover(text):
    """
    Recibe una cadena como parámetro, 
    filtra los caracteres alfanuméricos 
    y devuelve una nueva cadena.
    """
    return ''.join(filter(str.isalnum, text))

def normalize_text(text):
    """
    Recibe una cadena como parámetro, 
    convierte la cadena a minúscula
    reemplaza tildes, 
    remueve caraceteres no alfanuméricos 
    y devuelve una nueva cadena.
    """
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        text = text.lower().replace(a, b)
    return symbol_remover(text)

def find_similar_words(df, column):
    """
    Recibe como parámetros un dataframe y el nombre de la columna donde se debe buscar similitudes, 
    ordena el dataframe por la columna y la normaliza
    y devuelve una nueva cadena.
    """
    sorted_df = df.sort_values(by=column, ascending=True)
    sorted_df["normalized_column"] = sorted_df[column].apply(lambda x: normalize_text(x))
    normalized_values = sorted_df["normalized_column"].unique()
    
    result = f"{len(normalized_values)} valores normalizados\n"
    
    for value in normalized_values:
        similar_words = sorted_df.loc[sorted_df['normalized_column'] == value]
        original_similar_words = similar_words[column].unique()
        
        if len(original_similar_words) > 1:
            words = " | ".join(original_similar_words)
            result += f"PALABRAS SIMILARES PARA {value}: {words}.\n"

    filename = f'{column}_similar_words.txt'
    with open(filename, 'w') as file:
        file.write(result)

