"""
    player.py module: Contains Player class and helper functions
"""
from consts.all_players import ALL_PLAYERS_MAP
from consts.player_id_to_name_map import PLAYER_ID_TO_NAME_MAP
from consts.player_id_to_team_ids_map import PLAYER_ID_TO_TEAM_IDS_MAP
from consts.player_name_to_player_id_map import PLAYER_NAME_TO_PLAYER_ID_MAP
from consts.player_name_to_team_ids_map import PLAYER_NAME_TO_TEAM_IDS_MAP

class Player:
    """
        Player - attributes:
            player name
            team ids of player (player_team_ids)
            gets ids of all team-mates
    """
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_id = PLAYER_NAME_TO_PLAYER_ID_MAP.get(self.player_name)
        self.get_teammate_ids()

    def get_teammate_ids(self):
        self.teammates_ids = set()
        self.player_team_ids = PLAYER_ID_TO_TEAM_IDS_MAP.get(self.player_id)
        for player_id, team_ids in PLAYER_ID_TO_TEAM_IDS_MAP.items():
            if not self.player_team_ids.isdisjoint(team_ids):
                self.teammates_ids.add(player_id)


def get_mutual_teammates(player1, player2):
    mutual_teammates_ids = player1.teammates_ids.intersection(player2.teammates_ids)
    teammates = []
    for player_id in mutual_teammates_ids:
        teammate = PLAYER_ID_TO_NAME_MAP.get(player_id)
        teammates.append(teammate)
    
    if player1.player_name in teammates and player2.player_name in teammates:
        teammates.remove(player1.player_name)
        teammates.remove(player2.player_name)

    return teammates