import os 

# DIRECTORIOS DEL PROYECTO
MAIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESOURCES_DIR = os.path.join(MAIN_DIR, 'resources')
DATABASE_DIR =  os.path.join(MAIN_DIR, 'database')
DATASETS_DIR = os.path.join(DATABASE_DIR, 'datasets')
DATASOURCES_DIR = os.path.join(DATABASE_DIR, 'datasources')
SQL_SCRIPTS_DIR = os.path.join(DATABASE_DIR, 'sql-scripts')
