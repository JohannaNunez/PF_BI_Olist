import pandas as pd
import os
from sqlalchemy import create_engine, text

class DBConnection:
    engine = None

    def __init__(self):
        self.engine = self.get_engine()

    def get_engine(self):
        if self.engine is None:
            try:    
                self.engine = create_engine("postgresql://olist_dw_user:arCg8bRsHsvfyeUhrvTAQsRBqjJDV51v@dpg-cln6l31r6k8c73ac507g-a.oregon-postgres.render.com/olist_dw")
                print(f"Conectado a DB: {self.engine}")
            except Exception as e:
                print(f"Error en get_engine: {e}")
        
        return self.engine

    def get_data_from_query(self, query):
        engine = self.get_engine()
        df = pd.DataFrame()
        con = None
        try:
            with engine.connect() as con:
                df = pd.read_sql_query(query, con)
            
        except Exception as e:
            print(f"Error en get_data_from_query: {e}")
            pass

        if con:
            con.close()
        
        return df

    def exec_procedure(self, sp_name, params=""):
        result = False
        connection = None
        try:
            connection = self.engine.connect()
            transaction = connection.begin()
            connection.execute(text(f'CALL {sp_name}({params});'))
            transaction.commit()
            result = True

        except Exception as e:
            if transaction:
                transaction.rollback()
            print(f"Error en exec_procedure: {e}")

        finally:
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
            print(f"Error en exec_query: {e}")
            
        if connection:
            connection.close()
        return result
            
db_instance = DBConnection()