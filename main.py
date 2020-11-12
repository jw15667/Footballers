"""
    main.py: acts like runner module
"""
import json
import pprint

from consts.player_id_to_name_map import PLAYER_ID_TO_NAME_MAP
from player import (
    get_mutual_teammates,
    Player,
)

if __name__ == "__main__":
    print("Enter first player:")
    first_player_name = input()
    # player1 = "kevin nolan"

    print("Enter second player:")
    second_player_name = input()
    # player2 = "mark noble"

    player1 = Player(first_player_name)
    player2 = Player(second_player_name)

    mutual_teammates = get_mutual_teammates(player1, player2)

    print("mutual teammates are:")
    pprint.pprint(mutual_teammates)
