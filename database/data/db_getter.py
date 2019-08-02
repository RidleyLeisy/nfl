import requests
import mysql.connector
from dotenv import load_dotenv
import os

class dbGetter():
    def __init__(self):
        load_dotenv() 
        creds = (os.getenv('encoded_auth')) # loading env creds
        return


    def _open_connection(self):
        """Connects to database given env variables"""
        cnx = mysql.connector.connect(user=os.getenv('db_username'),
                            password=os.getenv('db_password'),
                            host=os.getenv('db_host'),
                            database=os.getenv('db_name'),use_pure=True)
        return cnx


    def query(self, query:str):
        cnx = self._open_connection()
        cur = cnx.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        cnx.close()
        return rows