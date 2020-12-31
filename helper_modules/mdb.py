from pymongo import MongoClient

"""
Saved in mongo:

test = {
    "_id": -2,
    "name": "Test Player",
    "team_ids: ['team1992', ...]
    "teammates": [{
        "t_id": 1,
        "t_name": "Test Player-Teammate"
    },...]
}
"""

mongo_client = MongoClient('localhost', 27017)
db = mongo_client['teammates']
players = db['players']
# collection: 'players'
