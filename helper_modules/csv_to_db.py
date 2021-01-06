"""
    Script to write CSV file to Mongo Database:
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