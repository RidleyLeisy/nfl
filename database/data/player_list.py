import mysql.connector
import os
from dotenv import load_dotenv
from importer import Importer
from grabber import Grabber

def open_connection():
    cnx = mysql.connector.connect(user=os.getenv('db_username'),
                        password=os.getenv('db_password'),
                        host=os.getenv('db_host'),
                        database=os.getenv('db_name'))
    return cnx

t = open_connection()
cursor = t.cursor()
query = 'SELECT player FROM player'

rows = cursor.execute(query)
player_ids = cursor.fetchall()
player_ids = ["%s/" % x for x in player_ids ]

i=0
player_load = []
while i < len(player_ids):
    player_load.append(player_ids[i:i+100])
    i+=100

t = Grabber('tweets')

for players in player_ids:
    t.set_player_ids(players)
    t.grab_data()
    print(t.json_load)