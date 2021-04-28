import requests
from bs4 import BeautifulSoup
from requests import HTTPError, ConnectionError, Timeout
import itertools

"""class used to get a session for a student accessing 
chancellor college student portal
"""

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/90.0.4430.85 Safari/537.36"}


class LoginSession:
    def __init__(self, username, password, session):
        self.loginData = {"username": username, "password": password, "login": ""}
        self.session = session

    def get_session(self):
        url = "https://portal.cc.ac.mw/students/login.php"
        self.session.post(url, data=self.loginData, headers=headers)
        return self.session


def get_soup(session, url):
    try:
        page = session.get(url)
        return BeautifulSoup(page.content, 'html.parser')

    except (HTTPError, ConnectionError, Timeout):
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


def get_student_name(session):
    soup = get_soup(session, "https://portal.cc.ac.mw/students/")
    return soup.find('nav', attrs={'role': 'navigation'}).find('span', class_="hidden-xs").string


def get_student_registration_number(session):
    soup = get_soup(session, "https://portal.cc.ac.mw/students/pages/profile/")

    return soup.find('div', class_="box box-academic").find('span', class_="data").string


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
    if get_soup(session, "https://portal.cc.ac.mw/students/pages/profile/") is not False:
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
                            class_="panel panel-default",recursive=False)

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


"""Scrapping students courses registration history"""


def get_current_year_registered_courses(session, semester):
    soup = get_soup(session, "https://portal.cc.ac.mw/students/pages/courses/")

    courses = soup.find('table', class_="table table-condensed")  # locating courses for two semesters

    allCourses = ['#']
    for rowItem in courses.text.split('\n'):  # loop for appending the courses to the list
        if rowItem != "":
            allCourses.append(rowItem.replace('\t', '').strip())
    semesterOneRegisteredCourses = []
    semesterTwoRegisteredCourses = []

    def get_formatted_string(semestercourses):

        stringRepresentation = ""

        for indexValue, item in enumerate(semestercourses, start=1):
            # formatting registered courses into a string to be displayed to user
            if indexValue <= 5:
                stringRepresentation += "{:<16} ".format(item)
            else:
                stringRepresentation += "{:<10} ".format(item)

            if indexValue % 5 == 0:
                stringRepresentation = stringRepresentation + "\n"

        return stringRepresentation

    # check if semester two courses exist in the list
    if "Semester 2 Courses" in allCourses:
        index = 0
        # if semi 2 courses exist in the list, separate the lists in to two lists otherwise all are semi one courses
        while allCourses[index] != "Semester 2 Courses":
            semesterOneRegisteredCourses.append(allCourses.pop(index))

        semesterTwoRegisteredCourses = allCourses  # remaining are semester 2 courses
    else:
        semesterOneRegisteredCourses = allCourses

    if semester == "1":
        return get_formatted_string(semesterOneRegisteredCourses)
    else:
        if len(semesterTwoRegisteredCourses) <= 0:
            return "*You are not registered for second semester*"
        else:
            headings = ['#', 'Code', 'Title', 'Credits', 'Type']
            semesterTwoRegisteredCourses.remove('Semester 2 Courses')
            semesterTwoRegisteredCourses = headings + semesterTwoRegisteredCourses
            return get_formatted_string(semesterTwoRegisteredCourses)


def get_current_year_semester_courses():
    pass


def get_courses_registered_in_previous_years():
    pass


""" The following functions scraps Accommodation details"""


def get_allocation_history(session):
    soup = get_soup(session, "https://portal.cc.ac.mw/rbas/student/studentsHistory/index.php")

    try:
        data = soup.find('table', class_="t1").find_all("tr")
        tableHeadings = []
        tableBodyData = []
        for row in data:
            for head, body in (itertools.zip_longest(row.find_all("th"), row.find_all("td"))):
                if body is not None:
                    tableBodyData.append(body.text)
                if head is not None:
                    tableHeadings.append(head.text)

        allData = tableHeadings + tableBodyData
        stringRepresentation = ''
        for index, item in enumerate(allData, start=1):
            # formatting results to be displayed to user

            stringRepresentation += "{:<16} ".format(item)

            if index % 4 == 0:
                stringRepresentation = stringRepresentation + "\n"

        return stringRepresentation

    except Exception as _:
        return None


def get_booking_history():
    pass


def get_accommodation_rules():
    pass


def get_notification():
    pass


if __name__ == "__main__":
    username = ""
    password = ''
    sess = LoginSession(username, password, requests.Session()).get_session()
    print(get_allocation_history(sess))
