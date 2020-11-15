"""
    main.py: acts like runner module
"""
import json
import pprint
import random
from retrying import retry
import sys

from consts.player_id_to_name_map import PLAYER_ID_TO_NAME_MAP
from consts.player_list import PLAYERS
from player import (
    get_mutual_teammates,
    Player,
)

class Runner:

    def __init__(self, pl_names):
        self.pl_names = pl_names

    @retry
    def question(self):
        self.player_one = Player(random.choice(self.pl_names))
        self.player_two = Player(random.choice(self.pl_names))
        self.answer = get_mutual_teammates(self.player_one, self.player_two)
        answer_length = len(self.answer)
        if answer_length < 5:
            raise Exception("No players")

        return f"Can you name all {answer_length} player(s) who have played with {self.player_one.player_name} and {self.player_two.player_name}"

    def answers(self):
        # print(a for a in self.answer)
        answer_nb = ', '.join(self.answer)
        return f"The players who played with {self.player_one.player_name} and {self.player_two.player_name}: {answer_nb}"

# runner = Runner(PLAYERS)
# runner.question()
# runner.answers()