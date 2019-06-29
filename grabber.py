
import requests
import os
import pandas as pd
from dotenv import load_dotenv
import mysql.connector

ENDPOINT = 'https://armchairanalysis.com/api/1.0/'
BLOCKS = 'https://armchairanalysis.com/api/1.0/game/{}/blocks'
SEASONS = 'https://armchairanalysis.com/api/1.0/schedule'

class Grabber():
    
    def __init__(self):

        load_dotenv()
        self.key = (os.getenv('encoded_auth'))
        return 
    
    @staticmethod
    def _chunks():

      return

    
    @staticmethod
    def _validate_string(val):
        if val != None:
            if type(val) is int:
             #for x in val:
                #   print(x)
                return str(val).encode('utf-8')
            else:
                return val
    
    
    @staticmethod
    def _get_json_request(self, endpoint):
        r = requests.get(f'{endpoint}', headers={'Authorization': self.key})
        json_dump = r.json()
        
        return json_dump


    def get_blocks(self):
        

        df = pd.DataFrame(json_dump['data'])
        return df


