"""
    Script to write CSV file to Mongo Database:
"""
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
import csv
from mdb import db, players

with open("all_player_data.csv", newline="") as csvfile:
    player_meta_data = csv.DictReader(csvfile)
    for row in player_meta_data:
        if (players.find_one({'_id': row['Player ID']})):
            players.update_one({
                '_id': row['Player ID']
            },
            {
                '$push': {
                    'team_ids': row['Team ID']
                }
            })
        else:
            player = {
                '_id': row['Player ID'],
                'name': row['Player'],
                'team_ids': [row['Team ID']]
            }
            db.players.insert_one(player)