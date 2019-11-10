# import json
# from db_importer import dbImporter

# SEASON = 2019

# with open('endpoints.json') as json_file:
#     data = dict(json.load(json_file))
# 'Stopped at games'
# print(len(data['data']))
# i=1
# print(data['data'])
# while i <= len(data['data']):
#     print(data[1][])
#     i+=1
# # for sec in data['data'].items():
# #     print(sec)
# # for sec in data['data'].items():
# #     start = 0
# #     if (sec[1]['endpoint'] == 'games') & (sec[0] != 'blocks'):
# #         print(f'Importing {sec[0]} for the {SEASON} season into database')
# #         importer = dbImporter(sec[0])
# #         importer.set_season(SEASON)
# #         importer.set_start(start)
# #         importer.set_offset(1)
# #         importer.grab_data()
# #         data = importer.json_load 
# #         importer.insert_data(data)