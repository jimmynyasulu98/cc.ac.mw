import requests
from bs4 import BeautifulSoup
from requests import HTTPError, ConnectionError, Timeout
import itertools

"""class used to get a session for a student accessing 
chancellor college student portal
"""


class LoginSession:
    def __init__(self, username, password, session):
        self.loginData = {"username": username, "password": password, "login": ""}
        self.session = session

    def get_session(self):
        url = "https://portal.cc.ac.mw/students/login.php"
        self.session.post(url, data=self.loginData)
        return self.session


def get_soup(session, url):
    try:
        page = session.get(url)
        return BeautifulSoup(page.content, 'html.parser')

    except HTTPError:
        return False

    except ConnectionError:

        return False

    except Timeout:

        return False


def is_user_logged_in(session):
    soup = get_soup(session, "https://portal.cc.ac.mw/students/")
    try:
        _ = soup.find('nav', attrs={'role': 'navigation'}).find('span', class_="hidden-xs").string
        return True
    except Exception as _:
        return False


""" 
The following functions scrape profile information
for a student 
"""


def get_profile_welcome_message(session):
    soup = get_soup(session, "https://portal.cc.ac.mw/students/pages/profile/")
    welcomeMessage = soup.find('div', class_='col-md-12', attrs={"style": "border:1px solid white;"}).string.replace(
        '\t', '')
    return welcomeMessage


def get_bio_data(session):
    soup = get_soup(session, "https://portal.cc.ac.mw/students/pages/profile/")
    bioData = soup.find('div', class_='box box-biodata').find('div', class_="box-body")
    # data = BioData.find('div', class_="box-body")
    allData = ''
    for i in bioData.text.split('\n'):
        if i != "":
            allData += (i.replace('\t', '').strip()) + '\n'

    return allData


def get_academic_details(session):
    soup = get_soup(session, "https://portal.cc.ac.mw/students/pages/profile/")
    academicDetails = soup.find('div', class_='box box-academic').find('div', class_="box-body")
    academicDetailsStringRepresentation = ''
    for i in academicDetails.text.split('\n'):
        if i != "":
            academicDetailsStringRepresentation += (i.replace('\t', '').strip()) + '\n'

    return academicDetailsStringRepresentation


def get_financial_details(session):
    soup = get_soup(session, "https://portal.cc.ac.mw/students/pages/profile/")
    if get_soup("https://portal.cc.ac.mw/students/pages/profile/") is not False:
        financialDetails = soup.find_all('div', class_='box box-academic')[1].find('div', class_="box-body")

        return financialDetails.text.replace('\t', '')
    else:
        return 'we could not fetch the requested data'


def get_contact_details(session):
    soup = get_soup(session, "https://portal.cc.ac.mw/students/pages/profile/")

    contactDetails = soup.find('div', class_='box box-contacts').find('div', class_="box-body")

    return contactDetails.text.replace('\t', '')


def get_incase_of_emergency(session):
    pass


"""Exam results"""


def get_semester_results(html_tag_location):
    semesterExamResults = ['#']
    for rowItem in html_tag_location.text.split('\n'):
        if rowItem != "":
            semesterExamResults.append(rowItem.replace('\t', '').strip())

    itemsToBeRemoved = []
    try:
        for index in range(2, len(semesterExamResults), 7):
            itemsToBeRemoved.append(semesterExamResults[index])
    except IndexError:
        pass

    for index in range(len(itemsToBeRemoved)):
        semesterExamResults.remove(itemsToBeRemoved[index])

    stringRepresentation = ""
    for index, item in enumerate(semesterExamResults, start=1):
        # formatting results to be displayed to user
        if index <= 6:
            stringRepresentation += "{:<12} ".format(item)
        else:
            stringRepresentation += "{:<14} ".format(item)

        if index % 6 == 0:
            stringRepresentation = stringRepresentation + "\n"

    return stringRepresentation


def get_current_year_exam_results(session, semester=1):
    soup = get_soup(session, "https://portal.cc.ac.mw/students/pages/results/")
    if str(semester) == "1":
        firstSemiResults = soup.find('div', class_='box').find('div', class_='box-body table-responsive no-padding')
        return get_semester_results(firstSemiResults)
    else:
        secondSemiResults = soup.find('div', class_='box').next_sibling.find('div',
                                                                             class_='box-body table-responsive '
                                                                                    'no-padding')
        return get_semester_results(secondSemiResults)


# def is_previous_year_exam_result_available(session):
#     soup = get_soup(session ,"https://portal.cc.ac.mw/students/pages/results/")
#     try:
#         soup.find('section', class_="content").find('span', class_='data pull-right')
#         return True
#     except Exception as _:
#         return False


# Generator function to yield previous years results.
def get_previous_year_exam_results(session):
    soup = get_soup(session, "https://portal.cc.ac.mw/students/pages/results/prev.php")
    listOfPreviousYears = soup.find('div', class_='tab-content').find_all('div', recursive=False)

    # form a two dimensional list to hold two semester results for each of the previous years
    yearResults = []
    for year in range(len(listOfPreviousYears)):  # looping using number of previous years

        yearResults.append([])
        for semester in range(2):  # range 2 because only two semesters/year
            # 0 stands for semi 1, and 1 semi 2.
            if semester == 0:
                yearResults[year].append(listOfPreviousYears[year].
                                         find('div', class_='box').find('div',
                                                                        class_='box-body table-responsive no-padding'))

            else:
                yearResults[year].append(listOfPreviousYears[year].
                                         find('div', class_='box').next_sibling.find('div', class_='box-body '
                                                                                                   'table-responsive '
                                                                                                   'no-padding'))
    # looping through the two dimensional list and yield each semester results
    for year in range(len(yearResults)):
        for semester in range(2):
            yield "*YEAR* \t " + str(year + 1) + "\t*SEMESTER*\t" + str(
                semester + 1) + "\t*RESULTS* \n" + '{}'.format(get_semester_results(
                yearResults[year][semester]))


"""Scrapping Assessments details"""


def get_assessment_dictionary(tag):
    assessmentsDictionary = {}
    for item in tag:
        dictionaryKey = item.find('div', class_="row")
        dickValuesForASingleKey = []
        for value in item.find('ol', attrs={"style": "list-style-type: lower-roman; background: none; padding-left: "
                                                     "15px;"}).find_all('div', class_="row"):
            dickValuesForASingleKey.append(value.text)

        assessmentsDictionary[dictionaryKey.text] = dickValuesForASingleKey
    return assessmentsDictionary


def get_assessments_details(session, semester=1):
    soup = get_soup(session, "https://portal.cc.ac.mw/students/pages/assessment/")
    if str(semester) == "1":
        divs = soup.find('section', class_="content").find('div', attrs={'id': 'accordion'}).find_all('div',
                                                                                                      class_="panel panel-default",
                                                                                                      recursive=False)
        for key in get_assessment_dictionary(divs):
            stringRepresentation = str(key) + " "
            for listValue in get_assessment_dictionary(divs)[key]:
                stringRepresentation += " \n" + str(listValue)

            yield stringRepresentation
    else:
        divItem = soup.find('section', class_="content").find('div', class_="panel-group") \
            .find('div', class_="panel-group")
        divs = divItem.find_all('div', class_="panel panel-default", recursive=False)
        for key in get_assessment_dictionary(divs):
            stringRepresentation = str(key) + " "
            for listValue in get_assessment_dictionary(divs)[key]:
                stringRepresentation += " \n" + str(listValue)

            yield stringRepresentation


if __name__ == "__main__":
    username = ""
    password = ''
    sess = LoginSession(username, password, requests.session()).get_session()
    print(is_user_logged_in(sess))
    asse = get_assessments_details(sess, 2)
    print(next(asse))
