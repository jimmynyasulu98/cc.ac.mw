"""
This modules craps all necessary information concerning all faculties at chancellor.
it includes overview of the faculty ,departments, dean , and  the contact details

"""
import itertools

from chanco_web_scrappings.general_methods import get_soup


class Faculty:

    def __init__(self, link):
        self.link = link

    def get_overview(self):
        try:
            soup = get_soup(self.link)
            return soup.find('div', class_="content-falc-dep")

        except Exception  as _:
            return False

    def get_faculty_dean_details(self):
        try:
            soup = get_soup(self.link)
            link_to_dean_web_page = soup.find('ul', class_="sidenav").find_all('a')

            link = 'https://www.cc.ac.mw/{}'.format(link_to_dean_web_page[3]['href'])

            soup_1 = get_soup(link)
            return soup_1.find('div', class_="col-xs-0 content-inner-principal")

        except Exception as _:

            return False

    def get_faculty_departments(self):
        try:
            soup = get_soup(self.link)
            link_to_departments_web_page = soup.find('ul', class_="sidenav").find_all('a')

            link = 'https://www.cc.ac.mw/{}'.format(
                link_to_departments_web_page[2]['href'])

            soup_1 = get_soup(link)
            departments = soup_1.find('div', class_="col-xs-11")
            stringRepresentation = ''

            for index, paragraph in enumerate(departments.text.split('\n')):
                if paragraph != '':
                    if index < 2:
                        stringRepresentation += paragraph.replace('\t', '').strip() + ' '
                    else:
                        stringRepresentation += paragraph.replace('\t', '').strip() + '\n'

            return stringRepresentation

        except Exception as _:

            return False

    def get_faculty_contact_details(self):

        try:
            soup = get_soup(self.link)
            link_to_contact_web_page = soup.find('ul', class_="sidenav").find_all('a')

            link = 'https://www.cc.ac.mw/{}'.format(link_to_contact_web_page[4]['href'])

            soup_1 = get_soup(link)
            data = soup_1.find('div', class_="col-xs-6").find_all('div', class_="row office-contact", recursive=False)
            workingHours = soup_1.find('div', class_="col-xs-4").find_all('div', class_="row office-contact",
                                                                          recursive=False)
            stringRepresentation = ''
            workingHoursStringRepresentation = ''

            for rowItem, workingHoursRow in itertools.zip_longest(data, workingHours):
                row = rowItem.find_all('div', class_='row')
                stringRepresentation += '*' + row[0].text.strip() + '*' + row[1].text.replace('\t', ''.strip())

                if workingHoursRow is not None:
                    row_1 = workingHoursRow.find_all('div', class_='row')
                    workingHoursStringRepresentation += '*' + row_1[0].text + '*' + '\n ' + row_1[1].text + '\n\n'

            return "{}{}".format(stringRepresentation, workingHoursStringRepresentation)

        except Exception as _:

            return False


"""Faculty of science custom functions"""

faculty_of_science = Faculty('https://www.cc.ac.mw/faculty/science')


def get_faculty_of_science_overview():
    if faculty_of_science.get_overview() is not False:
        paragraph = faculty_of_science.get_overview().find_all('p')
        # formatting the string in a form to be displayed to user
        background = paragraph[0].text + '\n'
        staff = paragraph[1].text + '\n'
        centers = paragraph[2].text + '\n'
        publication = paragraph[3].text + '\n'
        collaborations = paragraph[4].text + '\n'

        return '{}{}{}'.format('\t\t*Background*\n ' + background, '\t\t*Staff*\n' + staff,
                               '\t\t*Centers*\n' + centers + '.. for more visit cc.ac.mw')

    else:
        return False


def get_faculty_of_science_dean_details():
    if faculty_of_science.get_faculty_dean_details() is not False:
        stringRepresentation = ''
        for word in faculty_of_science.get_faculty_dean_details().text.split(' '):
            if len(stringRepresentation) < 1520:
                stringRepresentation += word + ' '
        return stringRepresentation + '..for more visit https://www.cc.ac.mw/faculty/science/dean'
    else:
        return False


def get_faculty_of_science_departments():
    if faculty_of_science.get_faculty_departments() is not False:
        return faculty_of_science.get_faculty_departments()

    else:
        return False


def get_faculty_of_science_contact_details():
    if faculty_of_science.get_faculty_contact_details() is not False:
        return faculty_of_science.get_faculty_contact_details()
    else:
        return False


"""Faculty of law custom functions"""
faculty_of_law = Faculty('https://www.cc.ac.mw/faculty/law')


def get_faculty_of_law_overview():
    if faculty_of_law.get_overview() is not False:
        paragraph = faculty_of_law.get_overview().find_all('p')
        # formatting the string in a form to be displayed to user
        mission = paragraph[0].text
        focus = paragraph[1].text
        departments = paragraph[3].text
        staffValues = paragraph[4].text

        return '{}{}{}{}'.format('\t\t*Mission*\n ' + mission + '\n', '\t\t*Focus*\n' + focus + '\n',
                                 '\t\t*Departments*\n' + departments + '\n',
                                 '\t\t*Staff Values*\n' + staffValues + '\n')

    else:
        return False


def get_faculty_of_law_dean_details():
    if faculty_of_law.get_faculty_dean_details() is not False:
        stringRepresentation = ''
        for word in faculty_of_law.get_faculty_dean_details().text.split(' '):
            if len(stringRepresentation) < 1520:
                stringRepresentation += word.replace("'", '\'') + ' '
        return stringRepresentation + '..for more https://www.cc.ac.mw/faculty/law/dean'

    else:
        return False


def get_faculty_of_law_departments():
    if faculty_of_law.get_faculty_departments() is not False:
        return faculty_of_law.get_faculty_departments()

    else:
        return False


def get_faculty_of_law_contact_details():
    if faculty_of_law.get_faculty_contact_details() is not False:
        return faculty_of_law.get_faculty_contact_details()
    else:
        return False


"""Faculty of education custom functions"""
faculty_of_education = Faculty('https://www.cc.ac.mw/faculty/education')


def get_faculty_of_education_overview():
    if faculty_of_education.get_overview() is not False:
        paragraphs = faculty_of_education.get_overview().find_all('p')
        unorderedLists = faculty_of_education.get_overview().find_all('ul')

        # formatting string to be displayed to user
        unorderedListString = ''
        for listValue in unorderedLists[1].find_all('li'):
            unorderedListString += listValue.text + '\n'
        background = ''
        for word in paragraphs[0].text.split(' '):
            if len(background) < 720:
                background += word + ' '
        departments = paragraphs[1].text + '\n' + unorderedLists[0].text
        partnerships = paragraphs[2].text + '\n' + paragraphs[3].text
        postgraduate_programs = paragraphs[4].text + '\n' + unorderedListString

        return '{}{}{}'.format('\t\t*Background*\n ' + background + '\n', '\t\t*Departments*\n' + departments + '\n',
                               '\t\t*Postgraduate Programs*\n' + postgraduate_programs + '\n')

    else:
        return False


def get_faculty_of_education_dean_details():
    if faculty_of_education.get_faculty_dean_details() is not False:
        stringRepresentation = ''
        for word in faculty_of_education.get_faculty_dean_details().text.split(' '):
            if len(stringRepresentation) < 1520:
                stringRepresentation += word + ' '
        return stringRepresentation + '..for more visit https://www.cc.ac.mw/faculty/education/dean'
    else:
        return False


def get_faculty_of_education_departments():
    if faculty_of_education.get_faculty_departments() is not False:
        return faculty_of_education.get_faculty_departments()
    else:
        return False


def get_faculty_of_education_contact_details():
    if faculty_of_education.get_faculty_contact_details() is not False:
        return faculty_of_education.get_faculty_contact_details()
    else:
        return False


"""Faculty of social science custom functions"""
faculty_of_social_science = Faculty('https://www.cc.ac.mw/faculty/social-science')


def get_faculty_of_social_science_overview():
    if faculty_of_social_science.get_overview() is not False:
        paragraph = faculty_of_social_science.get_overview().find_all('p')
        # formatting the string in a form to be displayed to user
        mission = paragraph[0].text
        departments = paragraph[1].text
        centers = paragraph[2].text
        focus = ''
        for word in paragraph[3].text.split(' '):
            if len(focus) < 600:
                focus += word + ' '

        return '{}{}{}{}'.format('\t\t*Mission*\n ' + mission + '\n', '\t\t*Departments*\n' + departments + '\n',
                                 '\t\t*Centers*\n' + centers + '\n', '\t\t*Focus*\n' + focus +
                                 '.. Visit cc.ac.mw for more details' '\n')
    else:
        return False


def get_faculty_of_social_science_dean_details():
    if faculty_of_social_science.get_faculty_dean_details() is not False:
        stringRepresentation = ''
        for line in faculty_of_social_science.get_faculty_dean_details().text.split(" "):
            if len(stringRepresentation) < 1564:
                stringRepresentation += line + ' '

        return stringRepresentation + '.. Visit cc.ac.mw for more details'
    else:
        return False


def get_faculty_of_social_science_departments():
    if faculty_of_social_science.get_faculty_departments() is not False:
        return faculty_of_social_science.get_faculty_departments()
    else:
        return False


def get_faculty_of_social_science_contact_details():
    if faculty_of_social_science.get_faculty_contact_details() is not False:
        return faculty_of_social_science.get_faculty_contact_details()
    else:
        return False


"""Faculty of Humanities custom functions"""

faculty_of_humanities = Faculty('https://www.cc.ac.mw/faculty/humanities')


def get_faculty_of_humanities_overview():
    if faculty_of_humanities.get_overview() is not False:
        paragraph = faculty_of_humanities.get_overview().find_all('p')
        # formatting the string in a form to be displayed to user
        overview = paragraph[0].text
        departments = paragraph[1].text
        centers = paragraph[2].text
        programs = paragraph[3].text

        return '{}{}{}{}'.format(overview + '\n', '\t\t*Departments*\n' + departments + '\n', '\t\t*Centers*\n' +
                                 centers + '\n', '\t\t*Programs*\n' + programs + '\n')
    else:
        return False


def get_faculty_of_humanities_dean_details():
    try:
        soup_1 = get_soup('https://www.cc.ac.mw/faculty/humanities/dean')
        return soup_1.find('div', class_="col-xs-0 content-inner-principal").text
    except Exception as _:
        return False


def get_faculty_of_humanities_departments():
    try:
        soup_1 = get_soup('https://www.cc.ac.mw/faculty/humanities/departments')
        departments = soup_1.find('div', class_="col-xs-11")
        stringRepresentation = ''

        for index, paragraph in enumerate(departments.text.split('\n')):
            if paragraph != '':
                if index < 2:
                    stringRepresentation += paragraph.replace('\t', '').strip() + ' '
                else:
                    stringRepresentation += paragraph.replace('\t', '').strip() + '\n'

        return stringRepresentation
    except Exception as _:
        return False


def get_faculty_of_humanities_contact_details():
    try:
        soup_1 = get_soup('https://www.cc.ac.mw/faculty/humanities/contacts')
        data = soup_1.find('div', class_="col-xs-6").find_all('div', class_="row office-contact", recursive=False)
        workingHours = soup_1.find('div', class_="col-xs-4").find_all('div', class_="row office-contact",
                                                                      recursive=False)
        stringRepresentation = ''
        workingHoursStringRepresentation = ''

        for rowItem, workingHoursRow in itertools.zip_longest(data, workingHours):
            row = rowItem.find_all('div', class_='row')
            stringRepresentation += '*' + row[0].text + '*' + '\n ' + row[1].text.replace('\t', ''.strip()) + '\n'

            if workingHoursRow is not None:
                row_1 = workingHoursRow.find_all('div', class_='row')
                workingHoursStringRepresentation += '*' + row_1[0].text + '*' + '\n ' + row_1[1].text + '\n\n'

        return "{}{}".format(stringRepresentation, workingHoursStringRepresentation)
    except Exception as _:
        return False
