import pandas as pd
import os
from sqlalchemy import create_engine, text

from settings import DB_CONNECTION_STRING
from settings.url_constants import SQL_SCRIPTS_DIR
from src.utils.log import logInfo

class DBConnection:
    engine = None

    def __init__(self):
        self.engine = self.get_engine()

    def get_engine(self):
        if self.engine is None:
            try:    
                self.engine = create_engine(DB_CONNECTION_STRING)
                print(f"Conectado a DB: {self.engine}")
            except Exception as e:
                logInfo(f"Error en get_engine: {e}")
        
        return self.engine
    
    def execute_script_file(self, filename):
        connection = None
        try:
            script_sql = None
            with open(os.path.join(SQL_SCRIPTS_DIR, filename), 'r') as script_file:
                script_sql = script_file.read()

            with self.engine.connect() as connection:
                connection.execute(text(script_sql))

        except Exception as e:
            logInfo(f"Error en ejecución de script: {e}")

        if connection:
            connection.close()

    def get_data_from_query(self, query):
        engine = self.get_engine()
        df = pd.DataFrame()
        con = None
        try:
            with engine.connect() as con:
                df = pd.read_sql_query(query, con)
            
        except Exception as e:
            logInfo(f"Error en get_data_from_query: {e}")
            pass

        if con:
            con.close()
        
        return df

    def exec_procedure(self, sp_name, params=""):
        connection = None
        result = False
        try:
            with self.engine.connect() as connection:
                transaction = connection.begin()
                connection.execute(text(f'CALL {sp_name} {params};'))
                transaction.commit()

        except Exception as e:
            transaction.rollback()
            logInfo(f"Error en exec_procedure: {e}")
        if connection:
            connection.close()
        return result

    def exec_query(self, query):
        connection = None
        result = False
        try:
            with self.engine.connect() as connection:
                connection.execute(text(query))
            if connection:
                connection.close()
            result = True
        except Exception as e:
            logInfo(f"Error en exec_query: {e}")
            
        if connection:
            connection.close()
        return result
        
    def drop_table(self, table_name):
        connection = None
        result = False
        try:
            drop_table_query = text(f'DROP TABLE IF EXISTS {table_name};')
            with self.engine.connect() as connection:
                transaction = connection.begin()
                connection.execute(drop_table_query)
                transaction.commit()

        except Exception as e:
            transaction.rollback()
            logInfo(f"Error en drop_table: {e}")
        if connection:
            connection.close()
        return result
        
    def load_csv_to_db(self, csv_path, table_name):
        rows_imported = 0
        self.drop_table(f"stg_{table_name}")
        try:
            with self.engine.begin() as connection:
                for chunk in pd.read_csv(csv_path, chunksize=1000):
                    chunk.to_sql(f"stg_{table_name}", connection, if_exists="append", index=False)
                    rows_imported += len(chunk)
        except Exception as e:
            logInfo(f"Error en load_df_to_db: {e}")       
            if 'ROLLBACK' not in str(e):
                self.engine.execute('ROLLBACK')

        return rows_imported

    def transfer_stg_to_prod_table(self, table_name):
        rows_imported = 0
        try:
            stg_df = pd.read_sql_table(f"stg_{table_name}", self.engine)
            with self.engine.begin() as connection:
                stg_df.to_sql(table_name, connection, if_exists='append', index=False, method='multi')
                rows_imported = len(stg_df)
        except Exception as e:
            logInfo(f"Error en transfer_stg_to_prod_table: {e}")
            if 'ROLLBACK' not in str(e):
                self.engine.execute('ROLLBACK')

        return rows_imported

    
db_instance = DBConnection()