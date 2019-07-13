import requests
import mysql.connector
from dotenv import load_dotenv
import os
from grabber import Grabber



class Importer(Grabber):

    def __init__(self, endpoint:str):
        super().__init__(endpoint)
        
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


    @staticmethod
    def _get_database_cols(json):
        return list(json[0].keys())


    @staticmethod
    def _json_to_list(self, json):
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
        return rows


    @staticmethod
    def _database_prep(rows:list, json):
        db_cols = _get_database_cols(json)
        rows_tuple = list(tuple(x) for x in rows)
        seperator = ','
        sql_cols = '(' + seperator.join(db_cols) + ')'
        sql_values = ['%s' for x in range(len(db_cols))]
        sql_values = '(' + seperator.join(sql_values) + ')'
        return sql_cols, sql_values, rows_tuple


    def insert_data(self, json):
        
        rows = _json_to_list(json)
        sql_cols, sql_values, rows_tuple = _database_prep(rows)
        
        print(sql_values)
        print(sql_cols)
        print(rows_tuple[0])

        # opening database connection
        cnx = self._open_connection()
        cursor = cnx.cursor()
        data = (f"INSERT INTO {self.id} {sql_cols} VALUES {sql_values}")
        cursor.executemany(data, rows_tuple)
        cnx.commit()
        # closing database connection
        cnx.close()
        
        return print(f'Values Inserted into {self.id}')
