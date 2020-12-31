"""
    Script to generate and save a player's teammates
"""
from mdb import db, players

for player in players.find():
    for ref_player in players.find():
        if player['_id'] != ref_player['_id']:
            mutual_teams = set(player['team_ids']).intersection(set(ref_player['team_ids']))
            if mutual_teams:
                players.update_one({
                    '_id': player['_id']
                },
                {
                    '$push': {
                        'teammates': {
                            'teammate_id': ref_player['_id'],
                            'teammate_name': ref_player['name'],
                            'mutual_team_ids': [team for team in mutual_teams]
                        }
                    }
                })
