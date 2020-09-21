from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


club_list = ['arsenal', 'aston-villa', 'barnsley', 'birmingham-city', 'blackburn-rovers', 'blackpool',
             'bolton-wanderers', 'afc-bournemouth', 'bradford-city', 'brighton-and-hove-albion', 'burnley',
             'cardiff-city', 'charlton-athletic', 'chelsea', 'coventry-city', 'crystal-palace', 'derby-county',
             'everton', 'fulham', 'huddersfield-town', 'hull-city', 'ipswich-town', 'leeds-united', 'leicester-city',
             'liverpool', 'manchester-city', 'manchester-united', 'middlesbrough', 'newcastle-united', 'norwich-city',
             'nottingham-forest', 'oldham-athletic', 'portsmouth', 'queens-park-rangers', 'reading', 'sheffield-united',
             'sheffield-wednesday', 'southampton', 'stoke-city', 'sunderland', 'swansea-city', 'swindon-town', 'tottenham-hotspur',
             'watford', 'west-bromwich-albion', 'west-ham-united', 'wigan-athletic', 'wimbledon', 'wolverhampton-wanderers']

season = ['1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005',
          '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']


team_season = []

for club, year in [(club, year) for club in club_list for year in season]:
    website = 'https://www.11v11.com/teams/{}/tab/players/season/{}/'.format(club, year)

    source = requests.get(website).text
    soup = BeautifulSoup(source, 'lxml')
    squad = soup.find(class_="squad sortable").find("tbody").find_all("tr")

    for rows in squad:
        hrefs = [(row["href"].split("/")[2]).split("-") for row in rows.find_all("a", href=True)]
        for element in hrefs:
            try:

                first_name = element [0]
                surname = element [1]
                player_id = element [2]

                team = {}
                team['Player'] = first_name + ' ' + surname
                team['Club'] = club
                team['Year'] = year
                team['Player ID'] = player_id
                team['Team ID'] = "{0}{1}".format(club, year)
                team_season.append(team)

            except:
                pass


csv_columns = ['Club','Year', 'Player', 'Player ID', 'Team ID']
csv_file = "Football_squads.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in team_season:
                writer.writerow(data)
except IOError:
    print("I/O error")


    # for rows in squad:
    #         cells = rows.find_all("td")
    #         player_name = cells[1].get_text()
    #         player_name_no_spaces = player_name.replace(" ", "")
    #         strip_club = club.replace(" ", "").replace("-", "")
    #         playa = player_name_no_spaces + strip_club + year
    #         team = {}
    #         team['Player'] = player_name
    #         team['Club'] = club
    #         team['Year'] = year
    #         team['Player ID'] = playa.lower()
    #         team_season.append(team)
