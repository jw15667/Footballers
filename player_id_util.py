"""
    Utility module to preprocess player ids
"""
import csv
import pprint

preprocess_player_id = []
numeric_id = [] #final list of dicts
player_ids = []
MAX_PLAYER_ID = 265594
temp = []

def is_unique(player_id, player_name, players_list):
    for player in players_list:
        if player_id == player['Player ID'] and player_name == player['Player']:
            return False
    return True

def generate_player_ids(preprocess_players_list):
    """
        Generate player ids for players which do not have ids
    """
    id_to_add = MAX_PLAYER_ID
    player_id_map = {}
    for player in preprocess_players_list:
        full_player_name = player['Player'] + ' ' + player['Player ID']
        player['Player'] = full_player_name
        if not (full_player_name in player_id_map.keys()):
            player['Player ID'] = id_to_add
            numeric_id.append(player)
            temp.append(player)
            player_id_map[full_player_name] = id_to_add
            id_to_add += 1
        else:
            player['Player ID'] = player_id_map[full_player_name]
            numeric_id.append(player)
            temp.append(player)
    return temp

with open('Football_squads.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Player ID'].isalpha() or row['Player ID'] == '':
            preprocess_player_id.append(row)
            del row
        else:
            row['Player ID'] = int(row['Player ID'])
            numeric_id.append(row)
            player_ids.append(row['Player ID'])

pprint.pprint(generate_player_ids(preprocess_player_id))
