"""
    main.py: acts like runner module
"""
import json
import pprint

import maps
import player_id_util

def get_team_ids(player_name, player_name_to_player_id, player_id_to_team_ids):
    player_id = player_name_to_player_id.get(player_name)
    player_team_ids = player_id_to_team_ids.get(player_id)
    return player_team_ids

def get_teammate_ids(player_team_ids, player_id_to_team_ids):
    teammates_ids = set()
    for player_id, team_ids in player_id_to_team_ids.items():
        if not player_team_ids.isdisjoint(team_ids):
            teammates_ids.add(player_id)
    return teammates_ids

def get_mutual_teammates(mutual_teammates_ids, player_id_to_name_map):
    teammates = []
    for player_id in mutual_teammates_ids:
        teammate = player_id_to_name_map.get(player_id)
        teammates.append(teammate)
    return teammates


if __name__ == "__main__":
    squads = player_id_util.complete_squads_dataset()
    player_id_to_name_map = maps.player_id_to_name(squads)
    player_name_to_team_ids_map = maps.name_to_team_ids(squads)
    player_name_to_player_id = maps.player_name_to_ids(squads)
    player_id_to_team_ids = maps.player_ids_to_team_ids(squads)

    print("Enter first player:")
    player1 = input()
    # player1 = "kevin nolan"

    print("Enter second player:")
    player2 = input()
    # player2 = "mark noble"

    player1_team_ids = get_team_ids(player1, player_name_to_player_id, player_id_to_team_ids)
    player2_team_ids = get_team_ids(player2, player_name_to_player_id, player_id_to_team_ids)

    player1_teammate_ids = get_teammate_ids(player1_team_ids, player_id_to_team_ids)
    player2_teammate_ids = get_teammate_ids(player2_team_ids, player_id_to_team_ids)

    mutual_teammate_ids = player1_teammate_ids.intersection(player2_teammate_ids)

    mutual_teammates = get_mutual_teammates(mutual_teammate_ids, player_id_to_name_map)

    if player1 in mutual_teammates: mutual_teammates.remove(player1)
    if player2 in mutual_teammates: mutual_teammates.remove(player2)

    print("mutual teammates are:")
    pprint.pprint(mutual_teammates)
