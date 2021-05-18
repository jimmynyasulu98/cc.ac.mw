from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from chanco_web_scrappings import *
import app_utils
import requests
from serialiser import *

SECRET_KEY = b'_5#y2L"F4Q8z/nxec]/'
app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def welcome():
    return "cc.ac.mw services"


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    user_session = None
    msg = request.form.get('Body')
    counter = session.get('counter', 0)
    resp = MessagingResponse()

    if counter > 0:
        if session['key1'] == '':

            if msg == '1':
                resp.message(app_utils.get_about_chanco_display_message())
                session['key1'] = '1'
            elif msg == '2':
                resp.message(app_utils.get_about_administration_message())
                session['key1'] = '2'
            elif msg == '3':
                resp.message(departments.get_departments() + app_utils.get_courses_on_departments_message())
                resp.message(app_utils.get_back_to_home_page_message())
                session['key1'] = '3'
            elif msg == '4':
                resp.message(app_utils.get_about_faculties_display_message())
                session['key1'] = '4'
            elif msg == '5':
                resp.message(app_utils.get_about_news_and_events_display_message())
                session['key1'] = '5'
            elif msg == '6':
                resp.message(app_utils.get_login_credentials_format_message())
                session['key1'] = '6'
            elif msg == '7':
                resp.message(app_utils.get_about_others_message())
                session['key1'] = '7'
            else:
                resp.message(app_utils.get_invalid_input_message() + app_utils.get_welcoming_message())
            session['key2'] = ''
            return str(resp)

        else:
            # Start of About chanco services
            if session['key1'] == '1':
                if msg == '1':
                    info, imageLink = about.get_chanco_at_glance(), media_files.about_great_hall_image
                    if info is not False and imageLink is not False:
                        resp.message(info).media(imageLink)
                        resp.message(app_utils.get_back_to_home_page_message())
                    else:
                        resp.message(
                            app_utils.get_could_not_fetch_message() + app_utils.get_back_to_home_page_message())

                elif msg == '2':
                    info, imageLink = about.get_about_library(), media_files.about_library_image
                    if info is not False and imageLink is not False:
                        resp.message(info).media(imageLink)
                        resp.message(app_utils.get_back_to_home_page_message())
                    else:
                        resp.message(
                            app_utils.get_could_not_fetch_message() + app_utils.get_back_to_home_page_message())

                elif msg == '3':
                    info, imageLink = about.get_about_the_great_hall(), media_files.about_great_hall_image
                    if info is not False and imageLink is not False:
                        resp.message(info + app_utils.get_back_to_home_page_message()).media(imageLink)
                    else:
                        resp.message(
                            app_utils.get_could_not_fetch_message() + app_utils.get_back_to_home_page_message())

                elif msg == '4':
                    info, imageLink = about.get_about_cafeteria(), media_files.about_cafeteria_image
                    if info is not False and imageLink is not False:
                        resp.message(info + app_utils.get_back_to_home_page_message()).media(imageLink)
                    else:
                        resp.message(
                            app_utils.get_could_not_fetch_message() + app_utils.get_back_to_home_page_message())

                elif msg == '5':
                    info, imageLink = about.get_about_senior_common_room(), media_files.about_senior_commons_room
                    if info is not False and imageLink is not False:
                        resp.message(info + app_utils.get_back_to_home_page_message()). \
                            media(imageLink)
                    else:
                        resp.message(
                            app_utils.get_could_not_fetch_message() + app_utils.get_back_to_home_page_message())

                elif msg == '6':
                    info, imageLink = about.get_about_junior_common_room(), media_files.about_junior_commons_room_image
                    if info is not False and imageLink is not False:
                        resp.message(info + app_utils.get_back_to_home_page_message()).media(imageLink)
                    else:
                        resp.message(
                            app_utils.get_could_not_fetch_message() + app_utils.get_back_to_home_page_message())

                elif msg == '7':
                    info, imageLink = about.get_about_clinic(), media_files.media_files.about_clinic_image
                    if info is not False and imageLink is not False:
                        resp.message(info + app_utils.get_back_to_home_page_message()).media(imageLink)
                    else:
                        resp.message(
                            app_utils.get_could_not_fetch_message() + app_utils.get_back_to_home_page_message())

                elif msg == '8':
                    info, imageLink = about.get_about_sports_complex(), media_files.about_sports_complex_image
                    if info is not False and imageLink is not False:
                        resp.message(info + app_utils.get_back_to_home_page_message()).media(imageLink)
                    else:
                        resp.message(
                            app_utils.get_could_not_fetch_message() + app_utils.get_back_to_home_page_message())

                elif msg == "##":
                    for key in list(session.keys()):
                        if key != '_flashes':
                            session.pop(key)
                    session['key1'] = ''
                    counter += 1
                    session['counter'] = counter
                    resp.message(app_utils.get_welcoming_message())
                elif msg.lower() == 'exit' or msg.lower() == 'cancel':
                    for key in list(session.keys()):
                        session.pop(key)
                    resp.message(app_utils.get_good_bye_message())
                else:
                    resp.message(app_utils.get_invalid_input_message())
                    resp.message(app_utils.get_about_chanco_display_message())
            # End of about chanco services

            # Start of administration services
            elif session['key1'] == '2':
                if session['key2'] == '':
                    if msg == '1':
                        resp.message(app_utils.get_principal_option_display_message())
                        session['key2'] = '1'
                    elif msg == '2':
                        resp.message(app_utils.get_dean_of_students_registrar_option_message())
                        session['key2'] = '2'
                    elif msg == '3':
                        resp.message(app_utils.get_dean_of_students_registrar_option_message())
                        session['key2'] = '3'
                    elif msg == '4':
                        resp.message(app_utils.get_finance_display_message())
                        session['key2'] = '4'
                    else:
                        resp.message(
                            app_utils.get_invalid_input_message() + app_utils.get_about_administration_message())
                else:
                    if session['key2'] == '1':
                        if msg == '1':
                            overview = administration.get_principals_office_overview()
                            if overview is not False:
                                resp.message(overview)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_page_message())
                        elif msg == '2':
                            principal = administration.get_principal_details()
                            if principal is not False:
                                resp.message(principal)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_page_message())
                        elif msg == '3':
                            vicePrincipal = administration.get_vice_principal_details()
                            if vicePrincipal is not False:
                                resp.message(vicePrincipal)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_page_message())
                        elif msg == '4':
                            history = administration.get_principals_office_history()
                            if history is not False:
                                resp.message(history + app_utils.get_back_to_home_page_message())
                            else:
                                resp.message(app_utils.get_could_not_fetch_message() +
                                             app_utils.get_back_to_home_page_message())
                        elif msg == '5':
                            contacts = administration.get_principal_contact_details()
                            if contacts is not False:
                                resp.message(contacts + app_utils.get_back_to_home_page_message())
                            else:
                                resp.message(app_utils.get_could_not_fetch_message() +
                                             app_utils.get_back_to_home_page_message())

                        elif msg == "##":
                            for key in list(session.keys()):
                                if key != '_flashes':
                                    session.pop(key)
                            session['key1'] = ''
                            counter += 1
                            session['counter'] = counter
                            resp.message(app_utils.get_welcoming_message())
                        elif msg.lower() == 'exit' or msg.lower() == 'cancel':
                            for key in list(session.keys()):
                                session.pop(key)
                            resp.message(app_utils.get_good_bye_message())
                        else:
                            resp.message(app_utils.get_invalid_input_message() +
                                         app_utils.get_principal_option_display_message())

                    elif session['key2'] == '2':
                        if msg == '1':
                            overview = administration.get_dean_of_students_office_overview()
                            if overview is not False:
                                resp.message(overview)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_page_message())
                        elif msg == '2':
                            deanDetails = administration.get_dean_of_students_details()
                            if deanDetails is not False:
                                resp.message(deanDetails)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_page_message())
                        elif msg == '3':
                            contacts = administration.get_dean_of_students_contact_details()
                            if contacts is not False:
                                resp.message(contacts + app_utils.get_back_to_home_page_message())
                            else:
                                resp.message(app_utils.get_could_not_fetch_message() +
                                             app_utils.get_back_to_home_page_message())

                        elif msg == "##":
                            for key in list(session.keys()):
                                if key != '_flashes':
                                    session.pop(key)
                            session['key1'] = ''
                            counter += 1
                            session['counter'] = counter
                            resp.message(app_utils.get_welcoming_message())

                        elif msg.lower() == 'exit' or msg.lower() == 'cancel':
                            for key in list(session.keys()):
                                session.pop(key)
                            resp.message(app_utils.get_good_bye_message())
                        else:
                            resp.message(
                                app_utils.get_invalid_input_message() +
                                app_utils.get_dean_of_students_registrar_option_message())
                    elif session['key2'] == '3':
                        if msg == '1':
                            overview = administration.get_registrars_office_overview()
                            if overview is not False:
                                resp.message(overview)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_page_message())
                        elif msg == '2':
                            registrarsDetails = administration.get_registrars_details()
                            if registrarsDetails is not False:
                                resp.message(registrarsDetails)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_page_message())
                        elif msg == '3':
                            contacts = administration.get_registrars_contact_details()
                            if contacts is not False:
                                resp.message(contacts + app_utils.get_back_to_home_page_message())
                            else:
                                resp.message(app_utils.get_could_not_fetch_message() +
                                             app_utils.get_back_to_home_page_message())
                        elif msg == "##":
                            for key in list(session.keys()):
                                if key != '_flashes':
                                    session.pop(key)
                            session['key1'] = ''
                            counter += 1
                            session['counter'] = counter
                            resp.message(app_utils.get_welcoming_message())
                        elif msg.lower() == 'exit' or msg.lower() == 'cancel':
                            for key in list(session.keys()):
                                session.pop(key)
                            resp.message(app_utils.get_good_bye_message())
                        else:
                            resp.message(app_utils.get_invalid_input_message() +
                                         app_utils.get_dean_of_students_registrar_option_message())
                    else:
                        if msg == '1':
                            finance = administration.get_finance_office_details()
                            if finance is not False:
                                resp.message(finance)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_page_message())
                        elif msg == '2':
                            contacts = administration.get_finance_office_contact_details()
                            if contacts is not False:
                                resp.message(contacts + app_utils.get_back_to_home_page_message())
                            else:
                                resp.message(app_utils.get_could_not_fetch_message()
                                             + app_utils.get_back_to_home_page_message())
                        elif msg == "##":
                            for key in list(session.keys()):
                                if key != '_flashes':
                                    session.pop(key)
                            session['key1'] = ''
                            counter += 1
                            session['counter'] = counter
                            resp.message(app_utils.get_welcoming_message())
                        elif msg.lower() == 'exit' or msg.lower() == 'cancel':
                            for key in list(session.keys()):
                                session.pop(key)
                            resp.message(app_utils.get_good_bye_message())
                        else:
                            resp.message(app_utils.get_invalid_input_message() +
                                         app_utils.get_dean_of_students_registrar_option_message())
            # End of administration services

            # Start of department services
            elif session['key1'] == '3':
                if msg == "##":
                    for key in list(session.keys()):
                        if key != '_flashes':
                            session.pop(key)
                    session['key1'] = ''
                    counter += 1
                    session['counter'] = counter
                    resp.message(app_utils.get_welcoming_message())

                elif msg.lower() == 'exit' or msg.lower() == 'cancel':
                    for key in list(session.keys()):
                        session.pop(key)
                    resp.message(app_utils.get_good_bye_message())
            # End of Department services

            # start of faculties services
            elif session['key1'] == '4':
                if session['key2'] == '':
                    if msg == '1':
                        resp.message(app_utils.get_faculty_display_message())
                        session['key2'] = '1'
                    elif msg == '2':
                        resp.message(app_utils.get_faculty_display_message())
                        session['key2'] = '2'
                    elif msg == '3':
                        resp.message(app_utils.get_faculty_display_message())
                        session['key2'] = '3'
                    elif msg == '4':
                        resp.message(app_utils.get_faculty_display_message())
                        session['key2'] = '4'
                    elif msg == '5':
                        resp.message(app_utils.get_faculty_display_message())
                        session['key2'] = '5'
                    elif msg == '0':
                        resp.message(app_utils.get_about_faculties_display_message())
                    elif msg == "##":
                        for key in list(session.keys()):
                            if key != '_flashes':
                                session.pop(key)
                        session['key1'] = ''
                        counter += 1
                        session['counter'] = counter
                        resp.message(app_utils.get_welcoming_message())

                    elif msg.lower() == 'exit' or msg.lower() == 'cancel':
                        for key in list(session.keys()):
                            session.pop(key)
                        resp.message(app_utils.get_good_bye_message())

                    else:
                        resp.message(
                            app_utils.get_invalid_input_message() + app_utils.get_about_faculties_display_message())
                else:
                    # faculty of science
                    if session['key2'] == '1':
                        if msg == '1':
                            overview = faculties.get_faculty_of_science_overview()
                            if overview is not False:
                                resp.message(overview)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''

                        elif msg == '2':
                            details, imageLink = faculties.get_faculty_of_science_dean_details(), \
                                                 media_files.dean_of_science_image
                            if details is not False and imageLink is not False:
                                resp.message(details).media(imageLink)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''

                        elif msg == '3':
                            department = faculties.get_faculty_of_science_departments()
                            if department is not False:
                                resp.message(department)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''

                        elif msg == '4':
                            contacts = faculties.get_faculty_of_science_contact_details()
                            if contacts is not False:
                                resp.message(contacts)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''
                        else:
                            resp.message(
                                app_utils.get_invalid_input_message() + app_utils.get_faculty_display_message())
                    # faculty of law
                    elif session['key2'] == '2':
                        if msg == '1':
                            overview = faculties.get_faculty_of_law_overview()
                            if overview is not False:
                                resp.message(overview)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''

                        elif msg == '2':
                            details, imageLink = faculties.get_faculty_of_law_dean_details(), \
                                                 media_files.dean_of_law_image
                            if details is not False and imageLink is not False:
                                resp.message(details).media(imageLink)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''

                        elif msg == '3':
                            department = faculties.get_faculty_of_law_departments()
                            if department is not False:
                                resp.message(department)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''

                        elif msg == '4':
                            contacts = faculties.get_faculty_of_law_contact_details()
                            if contacts is not False:
                                resp.message(contacts)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''
                        else:
                            resp.message(
                                app_utils.get_invalid_input_message() + app_utils.get_faculty_display_message())
                    # faculty of education
                    elif session['key2'] == '3':
                        if msg == '1':
                            overview = faculties.get_faculty_of_education_overview()
                            if overview is not False:
                                resp.message(overview)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''

                        elif msg == '2':
                            details, imageLink = faculties.get_faculty_of_education_dean_details(), \
                                                 media_files.dean_of_education_image
                            if details is not False and imageLink is not False:
                                resp.message(details).media(imageLink)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''

                        elif msg == '3':
                            department = faculties.get_faculty_of_education_departments()
                            if department is not False:
                                resp.message(department)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''

                        elif msg == '4':
                            contacts = faculties.get_faculty_of_education_contact_details()
                            if contacts is not False:
                                resp.message(contacts)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''
                        else:
                            resp.message(
                                app_utils.get_invalid_input_message() + app_utils.get_faculty_display_message())
                    # faculty of social science
                    elif session['key2'] == '4':
                        if msg == '1':
                            overview = faculties.get_faculty_of_social_science_overview()
                            if overview is not False:
                                resp.message(overview)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''

                        elif msg == '2':
                            details, imageLink = faculties.get_faculty_of_social_science_dean_details(), \
                                                 media_files.dean_of_social_science_image
                            if details is not False and imageLink is not False:
                                resp.message(details).media(imageLink)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''

                        elif msg == '3':
                            department = faculties.get_faculty_of_social_science_departments()
                            if department is not False:
                                resp.message(department)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''

                        elif msg == '4':
                            contacts = faculties.get_faculty_of_social_science_contact_details()
                            if contacts is not False:
                                resp.message(contacts)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''
                        else:
                            resp.message(
                                app_utils.get_invalid_input_message() + app_utils.get_faculty_display_message())
                    # faculty of humanities
                    else:
                        if msg == '1':
                            overview = faculties.get_faculty_of_humanities_overview()
                            if overview is not False:
                                resp.message(overview)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''

                        elif msg == '2':
                            details, imageLink = faculties.get_faculty_of_humanities_dean_details(), \
                                                 media_files.dean_of_humanities_image
                            if details is not False and imageLink is not False:
                                resp.message(details).media(imageLink)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''

                        elif msg == '3':
                            department = faculties.get_faculty_of_humanities_departments()
                            if department is not False:
                                resp.message(department)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''

                        elif msg == '4':
                            contacts = faculties.get_faculty_of_humanities_contact_details()
                            if contacts is not False:
                                resp.message(contacts)
                            else:
                                resp.message(app_utils.get_could_not_fetch_message())
                            resp.message(app_utils.get_back_to_home_of_previous_message())
                            session.pop('key2')
                            session['key2'] = ''
                        else:
                            resp.message(
                                app_utils.get_invalid_input_message() + app_utils.get_faculty_display_message())
            # End of faculties services

            # Start news and Events services
            elif session['key1'] == '5':
                if msg == '1':
                    news = news_and_events.get_news()
                    numOfItems = 0
                    for newsItem in news:
                        numOfItems += 1
                        resp.message(newsItem)
                    if numOfItems <= 0:
                        resp.message(app_utils.get_could_not_fetch_message())
                    resp.message(app_utils.get_back_to_home_of_previous_message())

                elif msg == '2':
                    articles = news_and_events.get_articles()
                    numOfItems = 0
                    for articleItem in articles:
                        numOfItems += 1
                        resp.message(articleItem)
                    if numOfItems <= 0:
                        resp.message(app_utils.get_could_not_fetch_message())
                    resp.message(app_utils.get_back_to_home_of_previous_message())
                elif msg == '3':
                    events = news_and_events.get_events()
                    numOfItems = 0
                    for eventsItem in events:
                        numOfItems += 1
                        resp.message(eventsItem)
                    if numOfItems <= 0:
                        resp.message(app_utils.get_could_not_fetch_message())
                    resp.message(app_utils.get_back_to_home_of_previous_message())
                elif msg == '4':
                    vacancies = news_and_events.get_vacancies()
                    numOfItems = 0
                    for vacancyItem in vacancies:
                        numOfItems += 1
                        resp.message(vacancyItem)
                    if numOfItems <= 0:
                        resp.message(app_utils.get_could_not_fetch_message())
                    resp.message(app_utils.get_back_to_home_of_previous_message())
                elif msg == '0':
                    resp.message(app_utils.get_about_news_and_events_display_message())
                elif msg == "##":
                    for key in list(session.keys()):
                        if key != '_flashes':
                            session.pop(key)
                    session['key1'] = ''
                    counter += 1
                    session['counter'] = counter
                    resp.message(app_utils.get_welcoming_message())

                elif msg.lower() == 'exit' or msg.lower() == 'cancel':
                    for key in list(session.keys()):
                        session.pop(key)
                    resp.message(app_utils.get_good_bye_message())
                else:
                    resp.message(app_utils.get_invalid_input_message() +
                                 app_utils.get_about_news_and_events_display_message())

            # End of news and Events services

            # Start of Chanco student portal Services
            elif session['key1'] == '6':

                if session['key2'] != '1':

                    if msg == "##":
                        for key in list(session.keys()):
                            if key != '_flashes':
                                session.pop(key)
                        session['key1'] = ''
                        counter += 1
                        session['counter'] = counter
                        resp.message(app_utils.get_welcoming_message())

                    elif msg.lower() == 'exit' or msg.lower() == 'cancel':
                        for key in list(session.keys()):
                            session.pop(key)
                        resp.message(app_utils.get_good_bye_message())

                    else:
                        if app_utils.get_validate_login_credentials(msg) is not False:
                            log = app_utils.get_validate_login_credentials(msg)
                            username = log[0]
                            password = log[1]

                            user_session = student_portal.LoginSession(username, password,
                                                                       requests.Session()).get_session()
                            if user_session is not False:

                                if student_portal.is_user_logged_in(user_session):
                                    mess = app_utils.get_portal_home_message(user_session)
                                    session['mySession'] = serialize_session(user_session)
                                    resp.message(mess)
                                    resp.message('Your image').media(media_files.get_portal_display_image(
                                        student_portal.get_student_registration_number(user_session)))

                                    session['key2'] = '1'
                                    session['key3'] = ''
                                else:
                                    resp.message(app_utils.get_login_unsuccessful_message())
                                    resp.message(app_utils.get_login_credentials_format_message() +
                                                 app_utils.get_back_to_home_page_message())

                            else:
                                resp.message('Login was unsuccessful try later\n\n')
                                resp.message(app_utils.get_welcoming_message())
                                session.pop('key1')
                                session['key1'] = ''

                        else:
                            resp.message(app_utils.get_invalid_login_credentials_message()
                                         + app_utils.get_login_credentials_format_message())
                else:
                    user_session = deserialize_session(session['mySession'])
                    if student_portal.is_user_logged_in(user_session):
                        if session['key3'] == '':
                            if msg == "1":
                                # profile message
                                resp.message(app_utils.get_profile_option_display_message(user_session))
                                session['key3'] = '1'
                            elif msg == "2":
                                # Exam results main message
                                resp.message(app_utils.get_exam_results_option_message())
                                session['key3'] = '2'
                            elif msg == '3':
                                # Assessments main message
                                resp.message(app_utils.get_assessment_message())
                                session['key3'] = '3'
                            elif msg == '4':
                                # my courses message
                                resp.message(app_utils.get_my_courses_message())
                                session['key3'] = '4'
                            elif msg == '5':
                                # exam timetable message
                                resp.message("Exam timetable currently not available\n\n" +
                                             app_utils.get_portal_home_message_2(user_session))
                            elif msg == '6':
                                # Accommodation message
                                resp.message(app_utils.get_accommodation_display_message())
                                session['key3'] = '6'
                            else:
                                resp.message(
                                    app_utils.get_invalid_input_message() + app_utils.get_portal_home_message_2(
                                        user_session))

                            session['key4'] = ''
                        else:
                            # start of profile option
                            if session['key3'] == "1":
                                if msg == '1':
                                    response = student_portal.get_bio_data(user_session)
                                    if response is not False:
                                        resp.message(response)
                                    else:
                                        resp.message(app_utils.get_could_not_fetch_message())
                                    resp.message(app_utils.get_portal_home_or_previous_page_message())

                                elif msg == '2':
                                    response = student_portal.get_academic_details(user_session)
                                    if response is not False:
                                        resp.message(response)
                                    else:
                                        resp.message(app_utils.get_could_not_fetch_message())
                                    resp.message(app_utils.get_portal_home_or_previous_page_message())

                                elif msg == '3':
                                    response = student_portal.get_financial_details(user_session)
                                    if response is not False:
                                        resp.message(response)
                                    else:
                                        resp.message(app_utils.get_could_not_fetch_message())
                                    resp.message(app_utils.get_portal_home_or_previous_page_message())

                                elif msg == '4':
                                    response = student_portal.get_contact_details(user_session)
                                    if response is not False:
                                        resp.message(response)
                                    else:
                                        resp.message(app_utils.get_could_not_fetch_message())
                                    resp.message(app_utils.get_portal_home_or_previous_page_message())

                                elif msg == '0':
                                    resp.message(app_utils.get_profile_option_display_message(user_session))
                                elif msg == '00':
                                    for key in list(session.keys()):
                                        if key != 'mySession' and key != '_flashes':
                                            session.pop(key)
                                    counter += 1
                                    session['counter'] = counter
                                    session['key1'] = '6'
                                    session['key2'] = '1'
                                    session['key3'] = ''
                                    resp.message(app_utils.get_portal_home_message_2(user_session))

                                elif msg == '##':
                                    for key in list(session.keys()):
                                        if key != '_flashes':
                                            session.pop(key)
                                    session['key1'] = ''
                                    counter += 1
                                    session['counter'] = counter
                                    resp.message(app_utils.get_welcoming_message())

                                else:
                                    resp.message(app_utils.get_invalid_input_message() + app_utils.
                                                 get_profile_option_display_message(user_session) +
                                                 app_utils.get_portal_home_or_previous_page_message())

                            # end of profile option
                            # start of exam results option
                            elif session['key3'] == '2':
                                balance = student_portal.get_student_balance(user_session)
                                if balance is not False:
                                    if balance <= 0.00:
                                        if session["key4"] == '':
                                            if msg == '1':
                                                resp.message(app_utils.get_current_year_exam_result_message())
                                                session['key4'] = '1'
                                            elif msg == '2':
                                                results = student_portal.get_previous_year_exam_results(user_session)
                                                numOfItems = 0
                                                for item in results:
                                                    numOfItems += 1
                                                    resp.message(item)
                                                if numOfItems <= 0:
                                                    resp.message(app_utils.get_previous_exam_not_available() +
                                                                 app_utils.get_exam_results_option_message())
                                                resp.message(app_utils.get_portal_home_or_previous_page_message())
                                            elif msg == '0':
                                                resp.message(app_utils.get_portal_home_message_2(user_session))
                                                session.pop('key3')
                                                session.pop('key4')
                                                session['key3'] = ''

                                            elif msg == '00':
                                                resp.message(app_utils.get_portal_home_message_2(user_session))
                                                session.pop('key3')
                                                session.pop('key4')
                                                session['key3'] = ''

                                            elif msg == '##':
                                                for key in list(session.keys()):
                                                    if key != '_flashes':
                                                        session.pop(key)
                                                session['key1'] = ''
                                                counter += 1
                                                session['counter'] = counter
                                                resp.message(app_utils.get_welcoming_message())
                                            else:
                                                resp.message(app_utils.get_invalid_input_message() +
                                                             app_utils.get_exam_results_option_message())  # revisit

                                        else:
                                            if msg == '1':
                                                results = student_portal.get_current_year_exam_results(user_session)
                                                if results is not False:
                                                    resp.message(results)
                                                else:
                                                    resp.message(app_utils.get_exam_not_available('1')
                                                                 + app_utils.get_exam_results_option_message())

                                            elif msg == '2':
                                                results = student_portal.get_current_year_exam_results(user_session,
                                                                                                       '2')
                                                if results is not False:
                                                    resp.message(results)
                                                else:
                                                    resp.message(app_utils.get_exam_not_available('2')
                                                                 + app_utils.get_exam_results_option_message())

                                            else:
                                                resp.message(app_utils.get_invalid_input_message() +
                                                             app_utils.get_exam_results_option_message())

                                            resp.message(app_utils.get_portal_home_or_previous_page_message())
                                            session.pop('key4')
                                            session['key4'] = ''

                                    else:
                                        resp.message(app_utils.get_balance_massage(user_session))
                                        resp.message(app_utils.get_portal_home_message_2(user_session))
                                        session.pop('key3')
                                        session['key3'] = ''

                                else:
                                    resp.message(app_utils.get_could_not_fetch_message())
                                    resp.message(app_utils.get_portal_home_message_2(user_session))
                                    session.pop('key3')
                                    session['key3'] = ''

                            # end of exam results option
                            # start of assessments details
                            elif session['key3'] == '3':
                                # semester 1
                                if msg == '1':
                                    assessments = student_portal.get_assessments_details(user_session, '1')
                                    numOfItems = 0
                                    for item in assessments:
                                        numOfItems += 1
                                        resp.message(item)
                                    if numOfItems <= 0:
                                        resp.message(app_utils.get_assessment_not_available_message('1') +
                                                     app_utils.get_assessment_message())
                                    resp.message(app_utils.get_portal_home_or_previous_page_message())
                                # semester 2
                                elif msg == '2':
                                    assessments = student_portal.get_assessments_details(user_session, '2')
                                    numOfItems = 0
                                    for item in assessments:
                                        numOfItems += 1
                                        resp.message(item)
                                    if numOfItems <= 0:
                                        resp.message(app_utils.get_assessment_not_available_message('2') +
                                                     app_utils.get_assessment_message())
                                    resp.message(app_utils.get_portal_home_or_previous_page_message())

                                elif msg == '3':
                                    resp.message(app_utils.get_option_under_construction() +
                                                 app_utils.get_portal_home_or_previous_page_message())
                                elif msg == '0':
                                    resp.message(app_utils.get_portal_home_message_2(user_session))
                                    session.pop('key3')
                                    session['key3'] = ''
                                elif msg == '00':
                                    resp.message(app_utils.get_portal_home_message_2(user_session))
                                    session.pop('key3')
                                    session['key3'] = ''
                                elif msg == '##':
                                    for key in list(session.keys()):
                                        if key != '_flashes':
                                            session.pop(key)
                                    session['key1'] = ''
                                    counter += 1
                                    session['counter'] = counter
                                    resp.message(app_utils.get_welcoming_message())
                                else:
                                    resp.message(app_utils.get_invalid_input_message() +
                                                 app_utils.get_assessment_message())
                            # end of assessments details
                            # start of my courses option
                            elif session['key3'] == '4':
                                if session['key4'] == '':
                                    if msg == '1':
                                        resp.message(app_utils.get_current_year_courses_display_message())
                                        session['key4'] = '1'
                                    elif msg == '2':
                                        resp.message(app_utils.get_option_under_construction() +
                                                     app_utils.get_my_courses_message())
                                    elif msg == '0':
                                        resp.message(app_utils.get_portal_home_message_2(user_session))
                                        session.pop('key3')
                                        session.pop('key4')
                                        session['key3'] = ''

                                    elif msg == '00':
                                        resp.message(app_utils.get_portal_home_message_2(user_session))
                                        session.pop('key3')
                                        session.pop('key4')
                                        session['key3'] = ''

                                    elif msg == '##':
                                        for key in list(session.keys()):
                                            if key != '_flashes':
                                                session.pop(key)
                                        session['key1'] = ''
                                        counter += 1
                                        session['counter'] = counter
                                        resp.message(app_utils.get_welcoming_message())
                                    else:
                                        resp.message(app_utils.get_invalid_input_message() +
                                                     app_utils.get_current_year_courses_display_message())
                                else:
                                    if msg == '1':
                                        courses = student_portal.get_current_year_registered_courses(user_session, '1')
                                        if courses is not False:
                                            resp.message(courses)
                                        else:
                                            resp.message(app_utils.get_semester_courses_not_available('1')
                                                         + app_utils.get_my_courses_message())

                                    elif msg == '2':
                                        courses = student_portal.get_current_year_registered_courses(user_session, '2')
                                        if courses is not False:
                                            resp.message(courses)
                                        else:
                                            resp.message(app_utils.get_semester_courses_not_available('2')
                                                         + app_utils.get_my_courses_message())
                                    else:
                                        resp.message(app_utils.get_invalid_input_message() +
                                                     app_utils.get_my_courses_message())
                                    resp.message(app_utils.get_portal_home_or_previous_page_message())
                                    session.pop('key4')
                                    session['key4'] = ''

                            # end of my courses option
                            # start of exam time table
                            elif session['key3'] == '5':
                                resp.message('Exam Timetable currently not available \n\n' + app_utils.
                                             get_portal_home_or_previous_page_message())
                            # end of exam timetable
                            # start of accommodation option
                            elif session['key3'] == '6':
                                if msg == '1':
                                    rules = student_portal.get_accommodation_rules(user_session)
                                    if rules is not False:
                                        resp.message(student_portal.get_accommodation_rules(user_session) + app_utils.
                                                     get_portal_home_or_previous_page_message())
                                    else:
                                        resp.message(app_utils.get_could_not_fetch_message() + app_utils.
                                                     get_portal_home_or_previous_page_message())
                                elif msg == '2':
                                    resp.message(app_utils.get_option_under_construction() + app_utils.
                                                 get_portal_home_or_previous_page_message())
                                elif msg == '3':
                                    resp.message(app_utils.get_option_under_construction() + app_utils.
                                                 get_portal_home_or_previous_page_message())
                                elif msg == '4':
                                    notifications = student_portal.get_notification(user_session)

                                    if notifications is not False:
                                        resp.message(student_portal.get_notification(user_session) + app_utils.
                                                     get_portal_home_or_previous_page_message())
                                    else:
                                        resp.message(app_utils.get_could_not_fetch_message() + app_utils.
                                                     get_portal_home_or_previous_page_message())
                                elif msg == '0':
                                    resp.message(app_utils.get_portal_home_message_2(user_session))
                                    session.pop('key3')
                                    session['key3'] = ''

                                elif msg == '00':
                                    resp.message(app_utils.get_portal_home_message_2(user_session))
                                    session.pop('key3')
                                    session['key3'] = ''

                                elif msg == '##':
                                    for key in list(session.keys()):
                                        if key != '_flashes':
                                            session.pop(key)
                                    session['key1'] = ''
                                    counter += 1
                                    session['counter'] = counter
                                    resp.message(app_utils.get_welcoming_message())
                                else:
                                    resp.message(app_utils.get_invalid_input_message() +
                                                 app_utils.get_accommodation_display_message())

                            # end of accommodation option

                    else:
                        for key in list(session.keys()):
                            if key != '_flashes':
                                session.pop(key)
                        counter += 1
                        session['counter'] = counter
                        session['key1'] = ''
                        resp.message(app_utils.get_welcoming_message())

            # end of chanco student portal services

            # start of others option services
            else:
                if msg == '1':
                    prospectusLink = media_files.get_prospectus()
                    if prospectusLink is not False:
                        resp.message().media(prospectusLink)
                        resp.message(app_utils.get_back_to_home_page_message())
                    else:
                        resp.message(
                            app_utils.get_could_not_fetch_message() + app_utils.get_back_to_home_page_message())
                elif msg == '2':
                    programs = others.get_masters_degree_programs()
                    if programs is not False:
                        resp.message(programs)
                        resp.message(app_utils.get_back_to_home_page_message())
                    else:
                        resp.message(
                            app_utils.get_could_not_fetch_message() + app_utils.get_back_to_home_page_message())
                elif msg == '3':
                    programs = others.get_doctorate_degrees()
                    if programs is not False:
                        resp.message(programs + app_utils.get_back_to_home_page_message())
                    else:
                        resp.message(
                            app_utils.get_could_not_fetch_message() + app_utils.get_back_to_home_page_message())

                elif msg == '4':
                    textBody = others.get_international_students()
                    imageLink = media_files.get_international_student_image()
                    if textBody is not False and imageLink is not False:
                        resp.message(textBody + app_utils.get_back_to_home_page_message()).media(imageLink)
                    else:
                        resp.message(
                            app_utils.get_could_not_fetch_message() + app_utils.get_back_to_home_page_message())

                elif msg == "##":
                    for key in list(session.keys()):
                        if key != '_flashes':
                            session.pop(key)
                    session['key1'] = ''
                    counter += 1
                    session['counter'] = counter
                    resp.message(app_utils.get_welcoming_message())

                elif msg.lower() == 'exit' or msg.lower() == 'cancel':
                    for key in list(session.keys()):
                        session.pop(key)
                    resp.message(app_utils.get_good_bye_message())
                else:
                    resp.message(app_utils.get_invalid_input_message() + app_utils.get_about_others_message())
            # end of others option services

        return str(resp)

    else:
        counter += 1
        session['counter'] = counter
        session['key1'] = ''
        resp.message(app_utils.get_welcoming_message())
        return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
