
import requests
import os
from dotenv import load_dotenv
from tqdm import tqdm
from time import time
from endpoints import endpoints as endpoint_dict

URI = 'https://armchairanalysis.com/api/1.0'


class Grabber():
    
    def __init__(self, endpoint:str):
        
        load_dotenv()
        self.key = (os.getenv('encoded_auth'))
        self.data = endpoint_dict['data'] # lading endpoints dictionary
        self.sub = self.data[endpoint] # selecting instance endpoint
        
        # API endpoint parameters
        self.endpoint = self.sub.get('endpoint')
        self.__id = self.sub.get('id')
        self.__filter = self.sub.get('filter_by')
        self.__season = self.sub.get('season')
        self.__start = self.sub.get('start')
        self.__ext_params = self.sub.get('ext_params')
        self.__team_name = self.sub.get('team_name_abv')
        self.__player_id = self.sub.get('player_id')
        self.__offset = 1

        return 

    
    def set_season(self, season):
        self.__season = season
        return


    def set_team_name(self, team_name_abv):
        self.__team_name = team_name_abv
        return


    def set_offset(self,offset):
        self.__offset = offset



    def grab_data(self):
        
        if self.__filter == 'season':
            json_load = Grabber.get_season_load(self)
        if self.__filter == 'player_id':
            json_load = Grabber.get_player_load(self)
        if self.__filter == 'team_name_abv':
            json_load = Grabber.get_team_load(self)
        return json_load


    @staticmethod
    def get_season_load(self):
        json_load = []
        error = True

        while error:
            
            r = requests.get(f'{URI}/{self.endpoint}/{self.__season}/{self.__id}?start={self.__start + self.__offset}{self.__ext_params}',
                                headers={'Authorization': self.key})

            if r.status_code != 200: #moves onto next season api call failed
                error = False
                print(r.status_code, r.content)
                print(f'Finished loading {self.__season}') #print what season is loading
            else:
                json = r.json()['data']
                json_load.extend(json)
                self.__offset += 1000 #cap of 1000 per api call
        return json_load


    @staticmethod
    def get_player_load(self):
        json_load = []
        error = True

        while error:
            r = requests.get(f'{URI}/{self.endpoint}/{self.__player_id}{self.__id}{self.__ext_params}',     
                                headers={'Authorization': self.key})
            if r.status_code != 200: #moves onto next season api call failed
                error = False
                print(r.status_code, r.content)
                print(f'Finished loading {self.__player_id}') #print what season is loading
            else:
                json = r.json()['data']
                json_load.extend(json)
                self.__offset += 1000 #cap of 1000 per api call
        
        return json_load


    @staticmethod
    def get_team_load(self):
        
        json_load = []
        r = requests.get(f'{URI}/{self.endpoint}/{self.__team_name}',
                            headers={'Authorization': self.key})
        if r.status_code != 200: #moves onto next season api call failed
            error = False
            print(r.status_code, r.content)
            print(f'Finished loading {self.__team_name}') #print what season is loading
        else:
            json = r.json()['data']
            json_load.extend(json)
            self.__offset += 1000 #cap of 1000 per api call
    
        return json_load


