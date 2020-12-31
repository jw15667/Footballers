from bs4 import BeautifulSoup
import csv
import requests


all_seasons = [s for s in range(1992, 2021)]
clubs_to_years_map = {
    'arsenal' : all_seasons,
    'aston-villa': [s for s in all_seasons if s not in (2016, 2017, 2018)],
    'barnsley':[1997],
    'birmingham-city': [2002, 2003, 2004, 2005, 2007, 2009, 2010],
    'blackburn-rovers': [s for s in range(1992, 2000)] + [s for s in range(2001, 2012)],
    'blackpool': [2010],
    'bolton-wanderers': [1995, 1997] + [s for s in range(2001, 2012)],
    'afc-bournemouth': [s for s in range(2015, 2020)],
    'bradford-city': [1999, 2000],
    'brighton-and-hove-albion': [s for s in range(2017, 2021)],
    'burnley': [2009, 2014] + [s for s in range(2016, 2021)],
    'cardiff-city': [2013, 2018],
    'charlton-athletic': [1998] + [s for s in range(2000, 2007)],
    'chelsea': all_seasons,
    'coventry-city': [s for s in range(1992, 2001)],
    'crystal-palace': [1992, 1994, 1997, 2004] + [s for s in range(2013, 2021)],
    'derby-county': [s for s in range(1992, 2002)] + [2007],
    'everton': all_seasons,
    'fulham': [s for s in range(2001, 2014)] + [2018, 2020],
    'huddersfield-town': [2017, 2018],
    'hull-city': [2008, 2009, 2013, 2014, 2016],
    'ipswich-town': [s for s in range(1992, 1995)] + [2000, 2001],
    'leeds-united': [s for s in range(1992, 2004)] + [2020],
    'leicester-city': [1994] + [s for s in range(1996, 2002)] + [2003] + [s for s in range(2014, 2021)],
    'liverpool': all_seasons,
    'manchester-city': [s for s in range(1992, 1996)] + [2000] + [s for s in range(2002, 2021)],
    'manchester-united': all_seasons,
    'middlesbrough': [1992, 1995, 1996] + [s for s in range(1998, 2009)] + [2016],
    'newcastle-united': [s for s in all_seasons if s not in (1992, 2009, 2016)],
    'norwich-city': [1992, 1993, 1994, 2004, 2011, 2012, 2013, 2015, 2019],
    'nottingham-forest': [1992, 1994, 1995, 1996, 1998],
    'oldham-athletic': [1992, 1993],
    'portsmouth': [s for s in range(2003, 2010)],
    'queens-park-rangers': [s for s in range(1992, 1996)] + [2011, 2012, 2014],
    'reading': [2006, 2007, 2012],
    'sheffield-united': [1992, 1993, 2006, 2019, 2020],
    'sheffield-wednesday': [s for s in range(1992, 2000)],
    'southampton': [s for s in range(1992, 2005)] + [s for s in range(2012, 2021)],
    'stoke-city': [s for s in range(2008, 2018)],
    'sunderland': [1996] + [s for s in range(1999, 2003)] + [2005] +  [s for s in range(2007, 2017)],
    'swansea-city': [s for s in range(2011, 2018)],
    'swindon-town': [1993],
    'tottenham-hotspur': all_seasons,
    'watford': [1999, 2006] + [s for s in range(2015, 2020)],
    'west-bromwich-albion': [2002, 2004, 2005, 2008] + [s for s in range(2010, 2018)] + [2020],
    'west-ham-united': [s for s in all_seasons if s not in (1992, 2003, 2004, 2011)],
    'wigan-athletic': [s for s in range(2005, 2013)],
    'wimbledon': [s for s in range(1992, 2000)],
    'wolverhampton-wanderers': [2003, 2009, 2010, 2011, 2018, 2019, 2020],
}

team_season = []

for club, years in clubs_to_years_map.items():
    for year in years:
        source = requests.get(f"https://www.11v11.com/teams/{club}/tab/players/season/{year}/").text
        soup = BeautifulSoup(source, 'lxml')
        squad = soup.find(class_="squad sortable").find("tbody").find_all("tr")
        for rows in squad:
            hrefs = [(row["href"].split("/")[2]).split("-") for row in rows.find_all("a", href=True)]
            player_meta_data = hrefs[0]
            player_id = player_meta_data.pop(-1)
            player_name = " ".join(player_meta_data)
            if player_id:
                team = {
                    'Player': player_name,
                    'Club': club,
                    'Year': year,
                    'Player ID': player_id,
                    'Team ID': f"{club}{year}",
                }
                team_season.append(team)

csv_columns = ['Club','Year', 'Player', 'Player ID', 'Team ID']
csv_file = "all_player_data.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in team_season:
                writer.writerow(data)
except IOError:
    print("I/O error")