from importer import Importer
from grabber import Grabber
import time



# teams = ['ARI','ATL', 'BAL', 'BUF', 'CAR', 'CHI', 'CIN', 'CLE',
#  'DAL', 'DEN', 'DET','GB', 'HOU', 'IND', 'JAC', 'KC', 'LA', 'LAC', 'MIA', 'MIN', 'NE',
#   'NO', 'NYG', 'NYJ', 'OAK', 'PHI', 'PIT', 'SEA', 'SF', 'TB', 'TEN', 'WAS']


# for team in teams:
#     time.sleep(20)
#     g = Grabber('drive_details')
#     g.set_team_name(team)
#     json = g.function_pointer()
#     t = Importer()
#     t.insert_data('games', json)
    


#time.sleep(60)
g = Grabber('penalties')
g.set_season(2000)
json = g.grab_data()
t = Importer()
t.insert_data('penalties', json)