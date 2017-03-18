import json
import requests
from lxml import html
from bs4 import BeautifulSoup, NavigableString

def topgames():
    url = 'http://www.metacritic.com/browse/games/release-date/new-releases/ps4/metascore'
    request = requests.get( url, headers={'User-Agent' : "Magic Browser"} )
    soup = BeautifulSoup(request.text, "lxml")

    # Extract the list that we actually need
    games_html= soup.find('ol', class_='list_products list_product_condensed')

    # Create two lists with Game Titles and Game Scores
    titles, scores = [],[]
    for line in games_html.findAll('a'):
        titles.append(line.getText(strip=True))

    for line in games_html.findAll('div', class_="basic_stat product_score brief_metascore"):
        scores.append(line.getText(strip=True))

    # Merge Lists into a List of Dicts
    result= [ { "title": str(t), "score": int(s) } for t, s in zip(titles, scores) ]
    return result

