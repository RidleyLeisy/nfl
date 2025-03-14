import requests
import mysql.connector
from dotenv import load_dotenv
import os

class Query():
    """Class that helps query database"""
    def __init__(self):
        load_dotenv() 
        self.user=os.getenv('db_username')
        self.password=os.getenv('db_password')
        self.host=os.getenv('db_host')
        self.database=os.getenv('db_name')
        #creds = (os.getenv('encoded_auth')) # loading env creds
        return


    def _open_connection(self):
        """Connects to database given env variables"""
        cnx = mysql.connector.connect(user=os.getenv('db_username'),
                            password=os.getenv('db_password'),
                            host=os.getenv('db_host'),
                            database=os.getenv('db_name'),
                            use_pure=True)
        return cnx


    def query(self, query:str):
        """Input your own query using this method"""
        cnx = self._open_connection()
        cur = cnx.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()

        return rows

    
    def get_player_by_id(self, id:str):
        """Get First and Last Name of player by their ID"""
        q = f'''SELECT CONCAT(p.fname,' ',p.lname)
                FROM `player` as p
                WHERE p.player = '{id}' '''
        return self.query(q)
    
    
    def get_player_by_name(self, name:str):
        """Get ID of player by using their First and Last Name"""
        fname,lname = name.split(' ')
        q = f'''SELECT p.id
                FROM `player` as p
                WHERE p.fname = '{fname}' AND p.lname = '{lname}' '''
        return self.query(q)
