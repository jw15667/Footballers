"""
    maps.py - create mappings:

    player id to player name
    name (or player id) to list of seasons
"""
from collections import defaultdict

#TODO squash all of these into one function!

def player_id_to_name(squads):
    player_ids_to_name = {}
    for player_meta_data in squads:
        player_id = player_meta_data['Player ID']
        player_name = player_meta_data['Player']
        player_ids_to_name[player_id] = player_name
    return player_ids_to_name

def name_to_team_ids(squads):
    player_name_to_team_ids = defaultdict(set)
    for player_meta_data in squads:
        player_name = player_meta_data['Player']
        team_id = player_meta_data['Team ID']
        player_name_to_team_ids[player_name].add(team_id)
    return player_name_to_team_ids

def player_name_to_ids(squads):
    player_names_to_ids = {}
    for player_meta_data in squads:
        player_name = player_meta_data['Player']
        player_id = player_meta_data['Player ID']
        player_names_to_ids[player_name] = player_id
    return player_names_to_ids

def player_ids_to_team_ids(squads):
    player_id_to_team_ids = defaultdict(set)
    for player_meta_data in squads:
        player_id = player_meta_data['Player ID']
        team_id = player_meta_data['Team ID']
        player_id_to_team_ids[player_id].add(team_id)
    return player_id_to_team_ids

