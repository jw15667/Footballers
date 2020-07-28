from bs4 import BeautifulSoup
import requests
import csv


club_list = ['arsenal', 'aston-villa', 'barnsley', 'birmingham-city', 'blackburn-rovers', 'blackpool',
             'bolton-wanderers', 'afc-bournemouth', 'bradford-city', 'brighton-and-hove-albion', 'burnley',
             'cardiff-city', 'charlton-athletic', 'chelsea', 'coventry-city', 'crystal-palace', 'derby-county',
             'everton', 'fulham', 'huddersfield-town', 'hull-city', 'ipswich-town', 'leeds-united', 'leicester-city',
             'liverpool', 'manchester-city', 'manchester-united', 'middlesbrough', 'newcastle-united', 'norwich-city',
             'nottingham-forest', 'oldham-athletic', 'portsmouth', 'queens-park-rangers', 'reading', 'sheffield-united',
             'sheffield-wednesday', 'southampton', 'stoke-city', 'sunderland', 'swansea-city', 'swindon-town', 'tottenham-hotspur',
             'watford', 'west-bromwich-albion', 'west-ham-united', 'wigan-athletic', 'wimbledon', 'wolverhampton-wanderers']
season = ['1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005',
          '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']


team_season = []
for club, year in [(club, year) for club in club_list for year in season]:
    website = 'https://www.11v11.com/teams/{}/tab/players/season/{}/'.format(club, year)

    source = requests.get(website).text
    soup = BeautifulSoup(source, 'lxml')
    squad = soup.find(class_="squad sortable").find("tbody").find_all("tr")


    for rows in squad:
            cells = rows.find_all("td")
            player_name = cells[1].get_text()
            for name in player_name:
                full_name = name.strip(' ')
                first_part = club.join(year)
                playa = first_part.join(self, __full_name)
            team = {}
            team['Player'] = player_name
            team['Club'] = club
            team['Year'] = year
            team['Player ID'] = playa
            team_season.append(team)

csv_columns = ['Club','Year', 'Player', 'Player ID']
csv_file = "Football_squads.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in team_season:
                writer.writerow(data)
except IOError:
    print("I/O error")

