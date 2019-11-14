import requests
import json
import os
import mysql.connector
from dotenv import load_dotenv
from api_getter import apiGetter



class dbImporter():
    '''
    This class is intended to be used with Armchair Analysis API only. To import data into the mysql db,
    create an dbImporter class for a given endpoint. This will get all supporting API creds, endpoint URLs, and table names
    for you. 
    '''
    def __init__(self, endpoint: str):
        self.endpoint = endpoint
        json_endpoints = self._read_json_endpoints()
        data = json_endpoints['data'] # adding endpoints dictionary
        sub = data.get(endpoint) # get parameters for specific endpoint
        self.table = sub.get('table')
        return 

    
    def _read_json_endpoints(self):
        with open('/Users/ridleyleisy/dev/nfl/database/data/endpoints.json') as json_file:
            endpoints = json.load(json_file)
        return endpoints


    def _open_connection(self):
        """Connects to database given env variables"""
        cnx = mysql.connector.connect(user=os.getenv('db_username'),
                            password=os.getenv('db_password'),
                            host=os.getenv('db_host'),
                            database=os.getenv('db_name'),use_pure=True)
        return cnx


    @staticmethod
    def _validate_string(val: str) -> str:
        """Validates rows in json file for proper database import"""
        if val != None:
            if type(val) is int:
                return str(val).encode('utf-8')
            else:
                return val


    def _json_to_list(self, json):
        """Takes in a json object, tests if it's a string, and returns a list for database import"""
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
    def chunks(l:int, n:int):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]


    @staticmethod
    def _database_prep(rows:list, json):
        """Method used to clean API call in order to properly import into database"""
        db_cols = list(json[0].keys())
        rows_tuple = list(tuple(x) for x in rows)
        seperator = ','
        sql_cols = '(' + seperator.join(db_cols) + ')'
        sql_values = ['%s' for x in range(len(db_cols))]
        sql_values = '(' + seperator.join(sql_values) + ')'
        return sql_cols, sql_values, rows_tuple


    def insert_data(self, json):
        """Main function to import json data into database. All attributes are inherited from Grabber class."""
        rows = self._json_to_list(json)
        sql_cols, sql_values, rows_tuple = self._database_prep(rows, json)
        
        print(f'Import the following columns: {sql_cols} into {self.table}')

        for sec in self.chunks(rows_tuple, 1000):
            cnx = self._open_connection() # opening database connection
            cursor = cnx.cursor()
            data = (f"INSERT IGNORE INTO {self.table} {sql_cols} VALUES {sql_values}")
            cursor.executemany(data, sec)
            cnx.commit()
            cnx.close() # closing database connection
        
        return print(f'Values Inserted into {self.table}')

