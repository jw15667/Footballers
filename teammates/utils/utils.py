from pymongo import MongoClient

class TeammateService():
    """
        Get mutual teammates from mongo
        + other functionality
        todo: make players a list so form can be extended
    """
    mongo_client = MongoClient('localhost', 27017)
    db = mongo_client['teammates']
    players = db['players']

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
    
    def calculate_mutual_teammates(self):
        player_docs = self.players.find({
            "name": {
                '$in': [self.player1_name, self.player2_name]
            }
        })

        p1_doc = player_docs[0]
        p2_doc = player_docs[1]

        player1_tmtes_ids = set([p1['teammate_id'] for p1 in p1_doc['teammates']])
        player2_tmtes_ids = set([p2['teammate_id'] for p2 in p2_doc['teammates']])
        mutual_team_ids = player1_tmtes_ids.intersection(player2_tmtes_ids)

        mutual_teammate_docs = self.players.find({
            "_id": {
                "$in": list(mutual_team_ids)
            }
        })

        return [mt["name"] for mt in mutual_teammate_docs]

"""
    temp stuff rn just to check logic...

    player 1 - player 2 mutual teammates


    loop through player 1 teammates.
    for pl in pl1.teammates:
        get the pl[pl_id]
        for pl2 in pl2.teammates:
            check the pl_id
            if its a match:
                store the pl name in a set
"""
