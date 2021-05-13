"""This Module scraps selected information  about chancellor college
 administration. This include , The Principal,  Registrar etc."""

from chanco_web_scrappings.general_methods import get_soup
import itertools

""" 
The principal and vice principal details
"""


def get_principals_office_overview():
    try:
        soup = get_soup('https://www.cc.ac.mw/office/principal')
        data = soup.find('div', class_="content-case-wide").find_all('p')
        stringRepresentation = ''
        for paragraph in data:
            stringRepresentation += paragraph.text + "\n"

        return stringRepresentation
    except Exception as _:
        return False


def get_principal_details():
    try:
        soup = get_soup('https://www.cc.ac.mw/office/principal/biography')
        data = soup.find('div', class_="col-xs-7 content-inner-principal")
        stringRepresentation = ''
        for word in data.text.split(' '):
            if len(stringRepresentation) < 1530:
                stringRepresentation += word + ' '
        return stringRepresentation + 'for more visit https://www.cc.ac.mw/office/principal/biography'

    except Exception as _:
        return False


def get_vice_principal_details():
    try:
        soup = get_soup('https://www.cc.ac.mw/office/principal/biography-vice')
        data = soup.find('div', class_="col-xs-7 content-inner-principal")
        stringRepresentation = ''
        for word in data.text.split(' '):
            if len(stringRepresentation) < 1520:
                stringRepresentation += word + ' '
        return stringRepresentation + '..for more visit https://www.cc.ac.mw/office/principal/biography-vice'
    except Exception as _:
        return False


def get_principals_office_history():
    try:
        soup = get_soup("https://www.cc.ac.mw/office/principal/history")
        data = soup.find('div', attrs={"style": "padding:0 20px"})
        frontMessage = soup.find('div', attrs={"style": "margin-bottom:20px"}).text
        dataList = []
        for item in data.text.split('\n'):
            if item != "":
                dataList.append(item)

        stringRepresentation = ''
        for index, item in enumerate(dataList, start=1):
            stringRepresentation += "{:<20} ".format(item)
            if index % 2 == 0:
                stringRepresentation += "\n\n "
        return "{} {}".format(frontMessage.replace('\t', '').strip() + '\n\n', stringRepresentation)
    except Exception as _:
        return False


def get_principal_contact_details():
    try:
        soup = get_soup("https://www.cc.ac.mw/office/principal/contact")
        data = soup.find('div', class_="col-xs-6").find_all('div', class_="row office-contact", recursive=False)
        workingHours = soup.find('div', class_="col-xs-4").find_all('div', class_="row office-contact", recursive=False)
        stringRepresentation = ''
        workingHoursStringRepresentation = ''

        for rowItem, workingHoursRow in itertools.zip_longest(data, workingHours):
            row = rowItem.find_all('div', class_='row')
            stringRepresentation += '*' + row[0].text + '*' + '\n ' + row[1].text + '\n\n'

            if workingHoursRow is not None:
                row_1 = workingHoursRow.find_all('div', class_='row')
                workingHoursStringRepresentation += '*' + row_1[0].text + '*' + '\n ' + row_1[1].text + '\n\n'

        return "{}{}".format(stringRepresentation, workingHoursStringRepresentation)
    except Exception as _:
        return False


"""Dean of students office details"""


def get_dean_of_students_office_overview():
    try:
        soup = get_soup("https://www.cc.ac.mw/office/dean-of-students")
        paragraphs = soup.find('div', class_="content-inner-wide").find_all('p')
        overview = ''
        for paragraph in paragraphs:
            overview += paragraph.text + '\n'
        stringRepresentation = ''
        for word in overview.split(' '):
            if len(stringRepresentation) < 1520:
                stringRepresentation += word + ' '
        return stringRepresentation + '..for more visit https://www.cc.ac.mw/office/dean-of-students'

    except Exception as _:
        return False


def get_dean_of_students_details():
    try:
        soup = get_soup('https://www.cc.ac.mw/office/dean-of-students/staff')
        paragraphs = soup.find('div', class_="col-xs-7 content-inner-principal").find_all('p')
        stringRepresentation = ''
        for paragraph in paragraphs:
            stringRepresentation += paragraph.text + '\n\n'
        return stringRepresentation

    except Exception as _:
        return False


def get_dean_of_students_contact_details():
    try:
        soup = get_soup("https://www.cc.ac.mw/office/dean-of-students/contact")
        data = soup.find('div', class_="col-xs-6").find_all('div', class_="row office-contact", recursive=False)
        workingHours = soup.find('div', class_="col-xs-4").find_all('div', class_="row office-contact", recursive=False)
        stringRepresentation = ''
        workingHoursStringRepresentation = ''

        for rowItem, workingHoursRow in itertools.zip_longest(data, workingHours):
            row = rowItem.find_all('div', class_='row')
            stringRepresentation += '*' + row[0].text + '*' + '\n ' + row[1].text + '\n\n'

            if workingHoursRow is not None:
                row_1 = workingHoursRow.find_all('div', class_='row')
                workingHoursStringRepresentation += '*' + row_1[0].text + '*' + '\n ' + row_1[1].text + '\n\n'

        return "{}{}".format(stringRepresentation, workingHoursStringRepresentation)

    except Exception as _:
        return False


"""Registrars  office details"""


def get_registrars_office_overview():
    try:
        soup = get_soup("https://www.cc.ac.mw/office/registrar")
        overviewMessage = soup.find('div', class_="content-inner-wide")
        stringRepresentation = ''
        for word in overviewMessage.text.split(' '):
            if len(stringRepresentation) < 1530:
                stringRepresentation += word + ' '
        return stringRepresentation + '..for more visit https://www.cc.ac.mw/office/registrar'

    except Exception as _:
        return False


def get_registrars_details():
    try:
        soup = get_soup('https://www.cc.ac.mw/office/registrar/staff')
        paragraphs = soup.find('div', class_="col-xs-7 content-inner-principal").find_all('p')
        stringRepresentation = ''
        for paragraph in paragraphs:
            stringRepresentation += paragraph.text + '\n\n'
        return stringRepresentation

    except Exception as _:
        return False


def get_registrars_contact_details():
    try:
        soup = get_soup("https://www.cc.ac.mw/office/registrar/contact")
        data = soup.find('div', class_="col-xs-6").find_all('div', class_="row office-contact", recursive=False)
        workingHours = soup.find('div', class_="col-xs-4").find_all('div', class_="row office-contact", recursive=False)
        stringRepresentation = ''
        workingHoursStringRepresentation = ''

        for rowItem, workingHoursRow in itertools.zip_longest(data, workingHours):
            row = rowItem.find_all('div', class_='row')
            stringRepresentation += '*' + row[0].text + '*' + '\n ' + row[1].text + '\n\n'

            if workingHoursRow is not None:
                row_1 = workingHoursRow.find_all('div', class_='row')
                workingHoursStringRepresentation += '*' + row_1[0].text + '*' + '\n ' + row_1[1].text + '\n\n'

        return "{}{}".format(stringRepresentation, workingHoursStringRepresentation)

    except Exception as _:
        return False


"""Finance  office details"""


def get_finance_office_details():
    try:
        soup = get_soup('https://www.cc.ac.mw/office/finance')
        paragraphs = soup.find('div', class_="content-inner-wide").find_all('p')
        stringRepresentation = ''
        for paragraph in paragraphs:
            stringRepresentation += paragraph.text + '\n\n'
        return stringRepresentation
    except Exception as _:
        return False


def get_finance_office_contact_details():
    try:
        soup = get_soup("https://www.cc.ac.mw/office/finance/contact")
        data = soup.find('div', class_="col-xs-6").find_all('div', class_="row office-contact", recursive=False)
        workingHours = soup.find('div', class_="col-xs-4").find_all('div', class_="row office-contact", recursive=False)
        stringRepresentation = ''
        workingHoursStringRepresentation = ''

        for rowItem, workingHoursRow in itertools.zip_longest(data, workingHours):
            row = rowItem.find_all('div', class_='row')
            stringRepresentation += '*' + row[0].text + '*' + '\n ' + row[1].text + '\n\n'

            if workingHoursRow is not None:
                row_1 = workingHoursRow.find_all('div', class_='row')
                workingHoursStringRepresentation += '*' + row_1[0].text + '*' + '\n ' + row_1[1].text + '\n\n'

        return "{}{}".format(stringRepresentation, workingHoursStringRepresentation)

    except Exception as _:
        return False

