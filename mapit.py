from csv import reader
import pprint
from collections import defaultdict
player_name_to_player_id_map = {}
player_id_to_team_ids_map = defaultdict(list)
team_id_to_player_name = defaultdict(list)

with open('Football_squads.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            player_name = row[2]
            player_id = row[3]
            team_id = row[4]
            player_name_to_player_id_map[player_name] = player_id
            player_id_to_team_ids_map[player_id].append(team_id)
            team_id_to_player_name[team_id].append(player_name)


searched_club_ids_1 = set([])
searched_club_ids_2 = set([])


name_1 = player_name_to_player_id_map.get('gareth barry')
name_2 = player_name_to_player_id_map.get('ashley young')

if name_1 in player_id_to_team_ids_map:
    search = player_id_to_team_ids_map.get(name_1)
    add_second_player = player_id_to_team_ids_map.get(name_2)
    searched_club_ids_1.update(search)
    searched_club_ids_2.update(add_second_player)

print(searched_club_ids_1)

shared_clubs = (searched_club_ids_1.intersection(searched_club_ids_2))
print(shared_clubs)
total_players = []

for team in shared_clubs:
    player_list = team_id_to_player_name.get(team)
    total_players.append(player_list)

print(total_players)
