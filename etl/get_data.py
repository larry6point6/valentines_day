import requests
from bs4 import BeautifulSoup

# Structure of URL is base + name_of_league + season_start

base = "https://understat.com/league"

# Initially will just use Premier League but
# this list gives us flexibility if we want to look at other leagues
# or later pull all the data
leagues = ["EPL", "La Liga", "Bundesliga", "Serie A", "Ligue 1", "RPFL"]
seasons = ["2014", "2015", "2016", "2017", "2018", "2019", "2021"]

# To select another league/season modify the below line accordingly
url = f"{base}/{leagues[0]}/{seasons[-1]}"


def download_data(base=url):
    r = requests.get(url)
    print(r.raise_for_status)

    return r


def create_soup(data):
    soup = BeautifulSoup(
        data.content,
        "lxml",
    )
    # We know that we're looking for the script tag as this houses our data
    scripts = soup.find_all("script")

    return scripts
