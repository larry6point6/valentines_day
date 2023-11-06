import logging
import os

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

base = os.getenv("BASE_URL")
league = os.getenv("LEAGUE")
season = os.getenv("SEASON")
url = f"{base}/{league}/{season}"


def download_data(base=url):
    r = requests.get(url)
    if r.status_code == 200:
        logging.info(f"Request succeeded with status code: {r.status_code}")
    else:
        logging.info(f"Request failed with status code: {r.status_code}")

    return r


def create_soup(data):
    soup = BeautifulSoup(
        data.content,
        "lxml",
    )

    scripts = soup.find_all("script")

    return scripts
