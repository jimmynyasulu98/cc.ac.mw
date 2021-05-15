from chanco_web_scrappings.general_methods import get_soup


def get_departments():
    soup = get_soup('https://www.cc.ac.mw/department')
    if soup is not False:
        try:
            title = soup.find('div', attrs={'id': 'content'}).find('div', class_="col-xs-11")
            return title.text

        except Exception as _:
            return False
    else:
        return False


if __name__ == '__main__':
    print(get_departments())
