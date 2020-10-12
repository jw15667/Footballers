"""
    Utility module to preprocess player ids, call complete_squads_dataset to
    obtain a list of all squads of all seasons.
    Also contanis some functions which may be useful to call from other modules
"""
import csv
import json

MAX_PLAYER_ID = 265594


def get_players_ids(player_data):
    """
    Returns two lists, one list of player dictionaries who have a valid ids
    and one list pf player dictionaries which do not have valid ids
    """

    invalid_player_ids = []
    player_ids = []

    for row in player_data:
        if row["Player ID"].isalpha() or row["Player ID"] == "":
            invalid_player_ids.append(row)
            del row
        else:
            row["Player ID"] = int(row["Player ID"])
            player_ids.append(row)

    return invalid_player_ids, player_ids


def is_unique(player_id, player_name, players_list):
    for player in players_list:
        if player_id == player["Player ID"] and player_name == player["Player"]:
            return False
    return True


def generate_players_ids(preprocess_players_list, max_player_id):
    """
    Generate player ids for players which do not have valid ids
    """
    id_to_add = max_player_id
    player_id_map = {}
    corrected_ids = []
    for player in preprocess_players_list:
        full_player_name = player["Player"] + " " + player["Player ID"]
        player["Player"] = full_player_name
        if not (full_player_name in player_id_map.keys()):
            player["Player ID"] = id_to_add
            player_id_map[full_player_name] = id_to_add
            id_to_add += 1
        else:
            player["Player ID"] = player_id_map[full_player_name]
        corrected_ids.append(player)
    return corrected_ids


def complete_squads_dataset():
    with open("Football_squads.csv", newline="") as csvfile:
        # load in player data set as a list of dictionaries
        player_data_set = csv.DictReader(csvfile)
        # generate two lists where invalid ids requires further prepocessing
        invalid_player_ids, valid_player_ids = get_players_ids(player_data_set)
        corrected_player_ids = generate_players_ids(invalid_player_ids, MAX_PLAYER_ID)
        full_squads_with_player_ids = valid_player_ids + corrected_player_ids
        # convert it into json
        return json.loads(json.dumps(full_squads_with_player_ids))