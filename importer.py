import requests
import mysql.connector
from dotenv import load_dotenv
import os
import grabber



class Importer():

    def __init__(self):
        return 


    @staticmethod
    def _open_connection():
        cnx = mysql.connector.connect(user=os.getenv('db_username'),
                            password=os.getenv('db_password'),
                            host=os.getenv('db_host'),
                            database=os.getenv('db_name'))
        return cnx


    @staticmethod
    def _validate_string(val:str) -> str:
        if val != None:
            if type(val) is int:
                return str(val).encode('utf-8')
            else:
                return val


    def insert_data(self, table_name: str, json):
        
        db_cols = list(json[0].keys()) # selecting databse columns from json keys
        i=0
        rows = []
        for row in json:
            if i >= 1:
                rows.append(section)
            i+=1
            section = []
            for col in db_cols:
                col_value = self._validate_string(row.get(col))
                section.append(col_value)
                
        # preparing data for database insert
        rows_tuple = list(tuple(x) for x in rows)
        seperator = ','
        sql_cols = '(' + seperator.join(db_cols) + ')'
        sql_values = ['%s' for x in range(len(db_cols))]
        sql_values = '(' + seperator.join(sql_values) + ')'
        
        # opening database connection
        cnx = self._open_connection()
        cursor = cnx.cursor()
        data = (f"INSERT INTO {table_name} {sql_cols} VALUES {sql_values}")
        cursor.executemany(data, rows_tuple)
        cnx.commit()
        # closing database connection
        cnx.close()
        
        return print(f'Values Inserted into {table_name}')
