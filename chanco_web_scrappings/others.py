from chanco_web_scrappings.general_methods import get_soup


def get_international_students():
    soup = get_soup('https://www.cc.ac.mw/people/students/students-international')
    if soup is not False:
        try:
            return soup.find('div', class_="content-case-wide").text

        except Exception as _:
            return False
    else:
        return False


def get_masters_degree_programs():
    soup = get_soup('https://www.cc.ac.mw/studies/programmes-masters')
    if soup is not False:
        try:
            programs = soup.find('div', class_="content-case-wide").find_all('ul')
            masterOfArts = programs[0].text
            masterOfEducation = programs[1].text
            masterOfLaw = programs[2].text
            masterOfScience = programs[3].text
            return masterOfArts + masterOfEducation + masterOfLaw + masterOfScience
        except Exception as _:
            return False
    else:
        return False


def get_doctorate_degrees():
    soup = get_soup('https://www.cc.ac.mw/studies/programmes-doctorate')
    if soup is not False:
        try:
            return soup.find('div', class_="content-case-wide").text

        except Exception as _:
            return False
    else:
        return False


