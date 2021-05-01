import requests
from bs4 import BeautifulSoup
from requests import HTTPError, ConnectionError, Timeout

defaultImage = "https://freepikpsd.com/wp-content/uploads/2019/10/no-image-png-5-Transparent-Images.png"


def get_soup(url):
    try:
        page = requests.get(url)
        return BeautifulSoup(page.content, 'html.parser')

    except (HTTPError, ConnectionError, Timeout):
        return False


def get_about_chanco_places_image(url):
    try:
        soup = get_soup(url)
        imgLink = soup.find('div', class_="content-inner-wide")
        return imgLink.img['src']

    except Exception as _:
        return defaultImage

def get_dean_of_faculty_image(url):
    try:
        soup = get_soup(url)

        return soup.find('div', class_="col-xs-3 principal").img['src']


    except Exception as _:

        return defaultImage


def get_faculty_image(url):
    try:
        soup = get_soup(url)
        return soup.find('div', class_="content-inner-wide").img['src']

    except Exception as _:

        return defaultImage


def get_faculty_image_2(url):
    try:
        soup = get_soup(url)
        imageLink = soup.find('div', class_="content-inner-wide").img['src']
        stringImageLink = ''
        for item in imageLink.split('/'):
            if item != '..':
                stringImageLink += '/' + item
        return 'http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/{}'.format(stringImageLink)

    except Exception as _:

        return defaultImage


if __name__ == '__main__':
    print(get_faculty_image_2('http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/faculty/humanities.html'))
