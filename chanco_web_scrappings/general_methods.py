import requests
from bs4 import BeautifulSoup
from requests import HTTPError, ConnectionError, Timeout


def get_soup(url):
    try:
        page = requests.get(url)
        return BeautifulSoup(page.content, 'html.parser')

    except (HTTPError, ConnectionError, Timeout):
        return False
