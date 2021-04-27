"""This Module scraps selected information concerning about chancellor college
This include History, Location etc"""

from chanco_web_scrappings.general_methods import get_soup
import itertools


def get_chanco_at_glance():
    try:
        soup = get_soup("http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/about/chanco-at-a-glance.html")
        data_chanco_at_glance = soup.find("div", class_="content-case about").find_all('p')
        data_guide = soup.find('div', attrs={'id': 'right_column'}).find('div', class_="holder").find_all('p')

        stringRepresentation1 = ""
        stringRepresentation2 = ""

        data_chanco_at_glance.pop(8)
        data_chanco_at_glance.pop(11)
        for paragraph1, paragraph2 in itertools.zip_longest(data_chanco_at_glance, data_guide):
            if paragraph1 is not None:
                stringRepresentation1 += paragraph1.text + "\n\n"
            if paragraph2 is not None:
                stringRepresentation2 += paragraph2.text + "\n\n"
        return "{} {}".format(stringRepresentation1, stringRepresentation2)

    except Exception as _:
        return False


if __name__ == "__main__":
    print(get_chanco_at_glance())
