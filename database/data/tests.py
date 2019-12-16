from api_getter import apiGetter
from db_importer import dbImporter


api = apiGetter('players')
api.set_season('2019')
api.grab_data()
data = api.json_load
importer = dbImporter('players')
importer.insert_data(data)
