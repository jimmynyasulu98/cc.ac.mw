"""This Module scraps selected information concerning about chancellor college
This include History, Location etc"""

from chanco_web_scrappings.general_methods import get_soup
import itertools


def get_chanco_at_glance():
    try:
        soup = get_soup("https://www.cc.ac.mw/about/chanco-at-a-glance")
        data_chanco_at_glance = soup.find("div", class_="content-case about").find_all('p')
        data_guide = soup.find('div', attrs={'id': 'right_column'}).find('div', class_="holder").find_all('p')

        stringRepresentation1 = ""
        stringRepresentation2 = ""

        data_chanco_at_glance.pop(8)
        data_chanco_at_glance.pop(11)
        for paragraph1, paragraph2 in itertools.zip_longest(data_chanco_at_glance, data_guide):
            if paragraph1 is not None:
                if len(stringRepresentation1) <= 1155:
                    stringRepresentation1 += paragraph1.text + "\n"
            if paragraph2 is not None:
                stringRepresentation2 += paragraph2.text + "\n"
        return "{} {}".format(stringRepresentation1, stringRepresentation2)

    except Exception as _:
        return False


"""Places associated with chancellor college"""


# About Chancellor college library
def get_about_library():
    try:
        soup = get_soup('https://www.cc.ac.mw/library')
        info = soup.find('div', class_="content-inner-wide")
        itemList = []
        for item in info.text.split('\n'):
            if item != '':
                itemList.append(item.replace('\t', '').strip())

        itemList.pop(0)  # remove first row of unnecessary information
        theLibrary = ''
        services = ''
        sectionsInTheLibrary = ''
        studyingInTheLibrary = ''
        underTheHood = ''

        for _ in itemList:

            if itemList[0] == 'Services':
                itemList.pop(0)
                break
            theLibrary += itemList.pop(0) + '\n'

        for _ in itemList:

            if itemList[0] == 'Sections in the Library':
                itemList.pop(0)
                break
            services += itemList.pop(0) + '\n'

        for _ in itemList:

            if itemList[0] != 'Studying in the Library':
                sectionsInTheLibrary += itemList.pop(0) + '\n'
            else:
                itemList.pop(0)
                break
        sectionsInTheLibrary += itemList.pop(0) + '\n'
        sectionsInTheLibrary += itemList.pop(0) + '\n'
        itemList.pop(0)

        for _ in itemList:

            if itemList[0] != 'Under the Hood':
                studyingInTheLibrary += itemList.pop(0) + '\n'
            else:
                itemList.pop(0)
                break

        for item in itemList:
            underTheHood += itemList.pop(0)

        return '{}{}{}{}{}'.format('\t\t*The Library*\n ' + theLibrary, '\t\t*Services*\n' + services,
                                   '\t\t*Sections*\n' + sectionsInTheLibrary,
                                   '\t\t*Studying In The Library*\n' + studyingInTheLibrary,
                                   '\t\t*Under The Hood*\n' + underTheHood)

    except Exception as _:
        return False


# About Chancellor college the great hall
def get_about_the_great_hall():
    try:
        soup = get_soup('https://www.cc.ac.mw/great-hall')
        info = soup.find('div', class_="content-inner-wide")
        itemList = []
        for item in info.text.split('\n'):
            if item != '':
                itemList.append(item.replace('\t', '').strip())
        stringRepresentation = ''
        for paragraph in itemList:
            stringRepresentation += paragraph + '\n'

        return stringRepresentation

    except Exception as _:

        return False


# About Chancellor college cafeteria
def get_about_cafeteria():
    try:
        soup = get_soup('https://www.cc.ac.mw/cafetaria')
        info = soup.find('div', class_="content-inner-wide")
        itemList = []
        for item in info.text.split('\n'):
            if item != '':
                itemList.append(item.replace('\t', '').strip())
        stringRepresentation = ''
        for paragraph in itemList:
            stringRepresentation += paragraph + '\n'

        return stringRepresentation

    except Exception as _:

        return False


# About Chancellor college Senior Common Room
def get_about_senior_common_room():
    try:
        soup = get_soup('https://www.cc.ac.mw/senior-common-room')
        info = soup.find('div', class_="content-inner-wide")
        itemList = []
        for item in info.text.split('\n'):
            if item != '':
                itemList.append(item.replace('\t', '').strip())
        stringRepresentation = ''
        for paragraph in itemList:
            stringRepresentation += paragraph + '\n'

        return stringRepresentation

    except Exception as _:

        return False


# About Chancellor college Junior Common Room
def get_about_junior_common_room():

    try:
        soup = get_soup('https://www.cc.ac.mw/junior-common-room')
        info = soup.find('div', class_="content-inner-wide")
        itemList = []
        for item in info.text.split('\n'):
            if item != '':
                itemList.append(item.replace('\t', '').strip())
        stringRepresentation = ''
        for paragraph in itemList:
            stringRepresentation += paragraph + '\n'

        return stringRepresentation

    except Exception as _:

        return False


# About Chancellor college clinic
def get_about_clinic():
    try:
        soup = get_soup('https://www.cc.ac.mw/clinic')
        info = soup.find('div', class_="content-inner-wide")
        itemList = []
        for item in info.text.split('\n'):
            if item != '':
                itemList.append(item.replace('\t', '').strip())
        stringRepresentation = ''
        for paragraph in itemList:
            stringRepresentation += paragraph + '\n'

        return stringRepresentation

    except Exception as _:

        return False

# About Chancellor college sports complex
def get_about_sports_complex():
    try:
        soup = get_soup('https://www.cc.ac.mw/sports-complex')
        info = soup.find('div', class_="content-inner-wide")
        itemList = []
        for item in info.text.split('\n'):
            if item != '':
                itemList.append(item.replace('\t', '').strip())
        stringRepresentation = ''
        for paragraph in itemList:
            stringRepresentation += paragraph + '\n'

        return stringRepresentation

    except Exception as _:

        return False

# About Chancellor college  Radio
def get_about_chanco_radio():
    pass


# About Chancellor college Chapel
def get_about_chapel():
    pass


# About chancellor college Nbs
def get_about_chanco_nbs():
    pass


if __name__ == "__main__":
    print(get_chanco_at_glance())
