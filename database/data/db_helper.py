import mysql.connector
import os
from dotenv import load_dotenv

class dbHelper():
    def __init__(self):
        load_dotenv()
        self.user = os.getenv('db_username'),
        self.password = os.getenv('db_password'),
        self.host = os.getenv('db_host'),
        self.database = os.getenv('db_name')

    @staticmethod
    def _open_connection():
        cnx = mysql.connector.connect(user=os.getenv('db_username'),
                            password=os.getenv('db_password'),
                            host=os.getenv('db_host'),
                            database=os.getenv('db_name'))
        return cnx