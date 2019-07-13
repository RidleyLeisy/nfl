
import requests
import os
from dotenv import load_dotenv
from tqdm import tqdm
from time import time
import json

URI = 'https://armchairanalysis.com/api/1.0'


class Grabber():
    load_dotenv()
    creds = (os.getenv('encoded_auth'))
    
    def __init__(self, endpoint:str):
        json_endpoints = self._read_json_endpoints()
        data = json_endpoints['data'] # adding endpoints dictionary
        sub = data.get(endpoint)
        # API endpoint parameters
        self.endpoint = sub.get('endpoint')
        self.id = sub.get('id')
        self.filter = sub.get('filter_by')
        self.season = sub.get('season')
        self.start = sub.get('start')
        self.ext_params = sub.get('ext_params')
        self.team_name = sub.get('team_name_abv')
        self.player_id = sub.get('player_id')
        self.offset = 1
        
        return 


    def _read_json_endpoints(self):
        with open('endpoints.json') as json_file:
            endpoints = json.load(json_file)
        return endpoints


    def set_season(self, season):
        self.season = season
        return


    def set_team_name(self, team_name_abv):
        self.team_name = team_name_abv
        return


    def set_offset(self, offset):
        self.offset = offset
        return


    def set_start(self, start):
        self.start = start
        return

    def set_player_ids(self, player_id):
        self.player_id = player_id
        return


    def grab_data(self):
        
        if self.filter == 'season':
            self.json_load = Grabber.get_season_load(self)
        if self.filter == 'player_id':
            self.json_load = Grabber.get_player_load(self)
        if self.filter == 'team_name_abv':
            self.json_load = Grabber.get_team_load(self)
        if self.filter == 'player':
            self.json_load = Grabber.get__active_players_load(self)
        return 


    @staticmethod
    def get_season_load(self):
        json_load = []
        error = True

        while error:
            
            r = requests.get(f'{URI}/{self.endpoint}/{self.season}/{self.id}?start={self.start + self.offset}{self.ext_params}',
                                headers={'Authorization': Grabber.creds})
            
            if r.status_code != 200: #moves onto next season api call failed
                error = False
                print(r.status_code, r.content)
                print(f'Finished loading {self.season}') #print what season is loading
            else:
                json = r.json()['data']
                json_load.extend(json)
                self.offset += 1000 #cap of 1000 per api call
        return json_load


    @staticmethod
    def get__active_players_load(self):
        json_load = []
        error = True

        while error:
            
            r = requests.get(f'{URI}/{self.endpoint}?start={self.start + self.offset}',
                                headers={'Authorization': Grabber.creds})

            if r.status_code != 200: #moves onto next season api call failed
                error = False
                print(r.status_code, r.content)
                print(f'Finished loading {self.start}') #print what season is loading
            else:
                json = r.json()['data']
                json_load.extend(json)
                self.offset += 1000 #cap of 1000 per api call
        return json_load


    @staticmethod
    def get_player_load(self):
        json_load = []
        error = True

        while error:
            r = requests.get(f'{URI}/{self.endpoint}/{self.player_id}{self.id}{self.ext_params}',     
                                headers={'Authorization': Grabber.creds})
            
            if r.status_code != 200: #moves onto next season api call failed
                error = False
                print(r.status_code, r.content)
                print(f'Finished loading {self.player_id}') #print what season is loading
            else:
                json = r.json()['data']
                json_load.extend(json)
                self.offset += 1000 #cap of 1000 per api call
        
        return json_load


    @staticmethod
    def get_team_load(self):
        
        json_load = []
        r = requests.get(f'{URI}/{self.endpoint}/{self.team_name}',
                            headers={'Authorization': Grabber.creds})
        if r.status_code != 200: #moves onto next season api call failed
            error = False
            print(r.status_code, r.content)
            print(f'Finished loading {self.team_name}') #print what season is loading
        else:
            json = r.json()['data']
            json_load.extend(json)
            self.offset += 1000 #cap of 1000 per api call
    
        return json_load

