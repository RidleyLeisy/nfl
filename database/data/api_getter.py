import requests
import os
from dotenv import load_dotenv
import time
import json


URI = 'https://armchairanalysis.com/api/1.0'
class apiGetter():
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

        json_endpoints = self._read_json_endpoints() # loading json file endpoints
        data = json_endpoints['data']
        sub = data.get(endpoint) # parameter searcher
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
            self.json_load = apiGetter.get_season_load_with_delay(self)
        if (self.filter == 'season') & (self.delay != 'Yes'):
            self.json_load = apiGetter.get_season_load(self)
        if self.filter == 'player_id':
            self.json_load = apiGetter.get_player_load(self)
        if self.filter == 'games':
            self.json_load = apiGetter.get_game_load(self)
        if self.filter == 'team_name_abv':
            self.json_load = apiGetter.get_team_load(self)
        if self.filter == 'player':
            self.json_load = apiGetter.get_active_players_load(self)
        return 


    @staticmethod
    def get_season_load_with_delay(self):
        '''Loads data from API endpoint with a 30 second delay. Intended to large data pulls'''
        json_load = []
        error = False
        while error == False:
            count = 0
            time.sleep(30)
            while count < 10000:
                count += 1000
                print(count)
                r = requests.get(f'{URI}/{self.endpoint}/{self.season}/{self.id}?start={self.start}{self.ext_params}',
                                    headers={'Authorization': apiGetter.creds})
                
                if r.status_code != 200: #moves onto next season api call failed
                    print(f'Failed to load {self.season} with status {r.status_code} and {r.reason}') # Failure state
                    error = True # Breaking the loop, adding delay, and restarting the counter
                    break

                elif len(r.json()['data']) == 0:
                    print(f'Finished loading {self.season} because there is no more data') # Failure state
                    error = True # Breaking the loop, adding delay, and restarting the counter
                    break

                else:
                    json = r.json()['data']
                    json_load.extend(json)
                    self.start += 1000 # Adding offset
                    
        return json_load


    @staticmethod
    def get_season_load(self):
        '''Loads data from API endpoint that requires a season'''
        json_load = []
        error = False

        while error == False:
            print(f'{URI}/{self.endpoint}/{self.season}/{self.id}?start={self.start + self.offset}{self.ext_params}')
            r = requests.get(f'{URI}/{self.endpoint}/{self.season}/{self.id}?start={self.start + self.offset}{self.ext_params}',
                                headers={'Authorization': apiGetter.creds})
            
            if r.status_code != 200:
                error = True # Breaking loop
                print(f'Failed to load {self.season} with status {r.status_code}. Error: {r.content}') # Failure state

            elif len(r.json()['data']) == 0:
                error = True # Breaking loop
                print(f'Finished loading {self.season} because there is no more data') # Failure state

            else:
                json = r.json()['data']
                json_load.extend(json)
                self.offset += 1000 # Adding offset
        return json_load


    @staticmethod
    def get_game_load(self):
        '''Loads data from API endpoint that requires game details. Intended for game specific endpoints: Game Details, Game Stats'''
        json_load = []
        r = requests.get(f'{URI}/{self.endpoint}/{self.season}',
                            headers={'Authorization': apiGetter.creds})
        
        if r.status_code != 200: 
            print(f'Failed to load {self.season} with status {r.status_code}') # Failure state

        elif len(r.json()['data']) == 0:
            print(f'Finished loading {self.season} because there is no more data')

        else:
            json = r.json()['data']
            print(f"Currently loading records between {self.start} and {self.offset + self.start}") # Failure state
            json_load.extend(json)
        return json_load


    @staticmethod
    def get_active_players_load(self):
        '''Loading data from API endpoint that requires player data. Intended for Active Player endpoint'''
        json_load = []
        error = False

        while error == False:
            
            r = requests.get(f'{URI}/{self.endpoint}?start={self.start + self.offset}',
                                headers={'Authorization': apiGetter.creds})

            if r.status_code != 200: 
                error = True # Breaking loop
                print(f'Failed to load {self.season} with status {r.status_code}') # Failure state

            elif len(r.json()['data']) == 0:
                error = True # Breaking loop
                print(f'Finished loading {self.season} because there is no more data') # Failure state
            else:
                json = r.json()['data']
                json_load.extend(json)
                self.offset += 1000 # Adding offset
        return json_load


    @staticmethod
    def get_player_load(self):
        '''Loading data from API endpoint that requires player id. Intended for Tweets endpoint'''
        json_load = []
        error = False

        while error == False:
            r = requests.get(f'{URI}/{self.endpoint}/{self.player_id}/{self.id}{self.ext_params}',     
                                headers={'Authorization': apiGetter.creds})
            
            if r.status_code != 200:
                error = True # Breaking loop
                print(f'Failed to load {self.player_id} with status {r.status_code}') # Failure state

            elif len(r.json()['data']) == 0:
                error = True # Breaking loop
                print(f'Finished loading {self.player_id} because there is no more data') # Failure state
            else:
                json = r.json()['data']
                json_load.extend(json)
                self.offset += 1000 # Adding offset
        
        return json_load


    @staticmethod
    def get_team_load(self):
        '''Loading data from API endpoint that requires team name. Inteded for Game Stats, Teams endpoint '''
        error = False
        json_load = []
        while error == False:

            r = requests.get(f'{URI}/{self.endpoint}/{self.team_name}',
                                headers={'Authorization': apiGetter.creds})
            if r.status_code != 200: 
                error = True # Breaking loop
                print(f'Failed to load {self.team_name} with status {r.status_code}') # Failure state

            elif len(r.json()['data']) == 0:
                error = True # Breaking loop
                print(f'Finished loading {self.team_name} because there is no more data') # Failure state
            else:
                json = r.json()['data']
                json_load.extend(json)
                self.offset += 1000 # Adding offset
        
        return json_load

