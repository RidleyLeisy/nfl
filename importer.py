import requests
import mysql.connector
from dotenv import load_dotenv
import os


class Importer(Grabber):

    def __init__(self):
                
        cnx = mysql.connector.connect(user=os.getenv('db_username'),
                                    password=os.getenv('db_password'),
                                    host=os.getenv('db_host'),
                                    database=os.getenv('db_name'))

        cursor = cnx.cursor()



    def insert_season_data(self):
        r = requests.get(f'{SEASONS}', headers={'Authorization': self.key})
        json_dump = r.json()
        cnx = mysql.connector.connect(user=os.getenv('db_username'),
                              password=os.getenv('db_password'),
                              host=os.getenv('db_host'),
                              database=os.getenv('db_name'))

        cursor = cnx.cursor()

        
        
        for i, item in enumerate(json_dump['data']):
            date = self.validate_string(item.get("date", None))
            day = self.validate_string(item.get("day", None))
            gid = self.validate_string(item.get("gid", None))
            h = self.validate_string(item.get("h", None))
            seas = self.validate_string(item.get("seas", None))
            stad = self.validate_string(item.get("stad", None))
            surf = self.validate_string(item.get("surf", None))
            v = self.validate_string(item.get("v", None))
            wk = self.validate_string(item.get("wk", None))

            insert_data = (
            '''INSERT INTO schedule (date, day, gid, h, seas, stad, surf, v, wk)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''' )
            cursor.execute(insert_data, (date, day, gid, h, seas, stad, surf, v, wk))

            cnx.commit()
            
        cnx.close()

        return


cnx.close()