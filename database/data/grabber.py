import requests
import os
from dotenv import load_dotenv
import time
import json


URI = 'https://armchairanalysis.com/api/1.0'
class Grabber():
    '''Grabber class is intended to interact with the Armchair Analysis API. It loads credentials from an env files and
    reads a json endpoints file for specific get requests. To change the standard parameters in the endpoints, use:
    1. set_season
    2. set_team_name
    3. set_offset
    4. set_player_id
    5. set_start
    6. set_delay

    '''


    load_dotenv() 
    creds = (os.getenv('encoded_auth')) # loading env creds
    
    def __init__(self, endpoint:str):

        json_endpoints = self._read_json_endpoints()
        data = json_endpoints['data'] # adding endpoints dictionary
        sub = data.get(endpoint) # get parameters for specific endpoint

        # API endpoint parameters
        self.endpoint = sub.get('endpoint')
        self.id = sub.get('id')
        self.filter = sub.get('filter_by')
        self.season = sub.get('season')
        self.start = sub.get('start')
        self.ext_params = sub.get('ext_params')
        self.team_name = sub.get('team_name_abv')
        self.player_id = sub.get('player_id')
        self.offset = 0
        self.delay = sub.get('delay')
        self.table = sub.get('table')

        return 


    def _read_json_endpoints(self):
        with open('/Users/ridleyleisy/dev/nfl/database/data/endpoints.json') as json_file:
            endpoints = json.load(json_file)
        return endpoints


    def set_season(self, season:int):
        self.season = season
        return


    def set_team_name(self, team_name_abv:str):
        self.team_name = team_name_abv
        return


    def set_offset(self, offset:int):
        self.offset = offset
        return


    def set_start(self, start:int):
        self.start = start
        return
    

    def set_delay(self, delay:str):
        self.delay = delay
        return


    def set_player_ids(self, player_id:int):
        self.player_id = player_id
        return


    def grab_data(self):
        '''
        This function grabs data from the Armchair Analysis API given the specific attributes of the class. It then assigns
        the json data to an attribute called json_load.
        '''
        if (self.filter == 'season') & (self.delay == 'Yes'):
            self.json_load = Grabber.get_season_load_with_delay(self)
        if (self.filter == 'season') & (self.delay != 'Yes'):
            self.json_load = Grabber.get_season_load(self)
        if self.filter == 'player_id':
            self.json_load = Grabber.get_player_load(self)
        if self.filter == 'team_name_abv':
            self.json_load = Grabber.get_team_load(self)
        if self.filter == 'player':
            self.json_load = Grabber.get__active_players_load(self)
        return 


    @staticmethod
    def get_season_load_with_delay(self):
        json_load = []
        
        count = self.start
    
        #while (count - self.start) < 500:
        count = self.start + self.offset
        print(count)
        print(f'{URI}/{self.endpoint}/{self.season}/{self.id}?start={self.start}{self.ext_params}')
        print(self.creds)
        r = requests.get(f'{URI}/{self.endpoint}/{self.season}/{self.id}?count=100&start={self.start}{self.ext_params}',
                            headers={'Authorization': Grabber.creds})
        
        if r.status_code != 200: #moves onto next season api call failed

            print(f'Failed to load {self.season} with status {r.status_code} and {r.reason}') #print what season is loading
            #break

        elif len(r.json()['data']) == 0:
            
            print(f'Finished loading {self.season} because there is no more data')
            #break
        else:
            json = r.json()['data']
            json_load.extend(json)
            self.offset += 1000 #cap of 1000 per api call
            
                
        return json_load


    @staticmethod
    def get_game_load(self):
        json_load = []
        error = True

        while error:
            
            r = requests.get(f'{URI}/{self.endpoint}?start={self.start + self.offset}{self.ext_params}',
                                headers={'Authorization': Grabber.creds})
            
            if r.status_code != 200: #moves onto next season api call failed
                error = False
                print(f'Failed to load {self.season} with status {r.status_code}') #print what season is loading

            elif len(r.json()['data']) == 0:
                error = False
                print(f'Finished loading {self.season} because there is no more data')

            else:
                json = r.json()['data']
                print(f"Currently loading records between {self.start} and {self.offset + self.start}")
                json_load.extend(json)
                self.offset += 1000 #cap of 1000 per api call
        return json_load


    @staticmethod
    def get_season_load(self):
        json_load = []
        error = True

        while error:
            
            r = requests.get(f'{URI}/{self.endpoint}/{self.season}/{self.id}?start={self.start + self.offset}{self.ext_params}',
                                headers={'Authorization': Grabber.creds})
            
            if r.status_code != 200: #moves onto next season api call failed
                error = False
                print(f'Failed to load {self.season} with status {r.status_code}') #print what season is loading

            elif len(r.json()['data']) == 0:
                error = False
                print(f'Finished loading {self.season} because there is no more data')

            else:
                json = r.json()['data']
                print(f"Currently loading records between {self.start} and {self.offset + self.start}")
                json_load.extend(json)
                self.offset += 1000 #cap of 1000 per api call
        return json_load



    @staticmethod
    def get_active_players_load(self):
        json_load = []
        error = True

        while error:
            
            r = requests.get(f'{URI}/{self.endpoint}?start={self.start + self.offset}',
                                headers={'Authorization': Grabber.creds})

            if r.status_code != 200: #moves onto next season api call failed
                error = False
                print(f'Failed to load {self.season} with status {r.status_code}') #print what season is loading

            elif len(r.json()['data']) == 0:
                error = False
                print(f'Finished loading {self.season} because there is no more data')
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
            r = requests.get(f'{URI}/{self.endpoint}/{self.player_id}/{self.id}{self.ext_params}',     
                                headers={'Authorization': Grabber.creds})
            
            if r.status_code != 200: #moves onto next season api call failed
                error = False
                print(f'Failed to load {self.player_id} with status {r.status_code}') #print what season is loading

            elif len(r.json()['data']) == 0:
                error = False
                print(f'Finished loading {self.player_id} because there is no more data')
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
            print(f'Failed to load {self.team_name} with status {r.status_code}') #print what season is loading

        elif len(r.json()['data']) == 0:
            error = False
            print(f'Finished loading {self.team_name} because there is no more data')
        else:
            json = r.json()['data']
            json_load.extend(json)
            self.offset += 1000 #cap of 1000 per api call
    
        return json_load

