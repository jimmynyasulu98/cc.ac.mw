"""This Module scraps selected information  about chancellor college
 administration. This include , The Principal,  Registrar etc."""

from chanco_web_scrappings.general_methods import get_soup
import itertools

""" 
The principal and vice principal details
"""


def get_principals_office_overview():
    try:
        soup = get_soup('http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/office/principal.html')
        data = soup.find('div', class_="content-case-wide").find_all('p')
        stringRepresentation = ''
        for paragraph in data:
            stringRepresentation += paragraph.text + "\n"

        return stringRepresentation
    except Exception as _:
        return False


def get_principal_details():
    try:
        soup = get_soup('http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/office/principal/biography.html')
        data = soup.find('div', class_="col-xs-7 content-inner-principal")
        return data.text
    except Exception as _:
        return False


def get_vice_principal_details():
    try:
        soup = get_soup('http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/office/principal/biography-vice.html')
        data = soup.find('div', class_="col-xs-7 content-inner-principal")
        return data.text
    except Exception as _:
        return False


def get_principals_office_history():
    try:
        soup = get_soup("http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/office/principal/history.html")
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
        soup = get_soup("http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/office/principal/contact.html")
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
        soup = get_soup("http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/office/dean-of-students.html")
        paragraphs = soup.find('div', class_="content-inner-wide").find_all('p')
        stringRepresentation = ''
        for paragraph in paragraphs:
            stringRepresentation += paragraph.text + '\n\n'
        return stringRepresentation

    except Exception as _:
        return False


def get_dean_of_students_details():
    try:
        soup = get_soup('http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/office/dean-of-students/staff.html')
        paragraphs = soup.find('div', class_="col-xs-7 content-inner-principal").find_all('p')
        stringRepresentation = ''
        for paragraph in paragraphs:
            stringRepresentation += paragraph.text + '\n\n'
        return stringRepresentation

    except Exception as _:
        return False


def get_dean_of_students_contact_details():
    try:
        soup = get_soup("http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/office/dean-of-students/contact.html")
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
        soup = get_soup("http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/office/registrar.html")
        overviewMessage = soup.find('div', class_="content-inner-wide")
        return overviewMessage.text
    except Exception as _:
        return False


def get_registrars_details():
    try:
        soup = get_soup('http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/office/registrar/staff.html')
        paragraphs = soup.find('div', class_="col-xs-7 content-inner-principal").find_all('p')
        stringRepresentation = ''
        for paragraph in paragraphs:
            stringRepresentation += paragraph.text + '\n\n'
        return stringRepresentation

    except Exception as _:
        return False


def get_registrars_contact_details():
    try:
        soup = get_soup("http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/office/registrar/contact.html")
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
        soup = get_soup('http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/office/finance.html')
        paragraphs = soup.find('div', class_="content-inner-wide").find_all('p')
        stringRepresentation = ''
        for paragraph in paragraphs:
            stringRepresentation += paragraph.text + '\n\n'
        return stringRepresentation
    except Exception as _:
        return False


def get_finance_office_contact_details():
    try:
        soup = get_soup("http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/office/finance/contact.html")
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


if __name__ == "__main__":
    print(get_finance_office_contact_details())
