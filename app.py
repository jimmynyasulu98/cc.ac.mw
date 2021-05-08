from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from chanco_web_scrappings import *
import app_utils
import requests
from serialiser import *

SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def hello():
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
                resp.message('Welcome to chanco about')
                session['key1'] = '1'
            elif msg == '2':
                resp.message('Administration')
                session['key1'] = '2'
            elif msg == '3':
                resp.message('Departments')
                session['key1'] = '3'
            elif msg == '4':
                resp.message('Faculties')
                session['key1'] = '4'
            elif msg == '5':
                resp.message('News and events')
                session['key1'] = '5'
            elif msg == '6':
                resp.message(app_utils.get_login_credentials_format_message())
                session['key1'] = '6'
            elif msg == '7':
                resp.message('Others')
                session['key1'] = '7'
            else:
                resp.message(str(app_utils.get_invalid_input_message()) + str(app_utils.get_welcoming_message()))
            session['key2'] = ''
            return str(resp)

        else:
            # Start of About chanco services
            if session['key1'] == '1':
                pass
            # End of about chanco services

            # Start of administration services
            elif session['key1'] == '2':
                pass
            # End of administration services

            # Start of department services
            elif session['key1'] == '3':
                pass
            # End of Department services

            # start of faculties services
            elif session['key1'] == '4':
                pass
            # End of faculties services

            # Start news and Events services
            elif session['key1'] == '5':
                pass
            # End of news and Events services

            # Start of Chanco student portal Services
            elif session['key1'] == '6':

                if session['key2'] != '1':
                    if app_utils.get_validate_login_credentials(msg) is not False:
                        log = app_utils.get_validate_login_credentials(msg)
                        username = log[0]
                        password = log[1]

                        user_session = student_portal.LoginSession(username, password, requests.Session()).get_session()
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
                                resp.message(app_utils.get_login_credentials_format_message())

                        else:
                            resp.message('Login was unsuccessful try later\n\n')
                            resp.message(app_utils.get_welcoming_message())
                            session.pop('key1')
                            session['key1'] = ''

                    else:
                        resp.message(app_utils.get_invalid_login_credentials_message())
                        resp.message(app_utils.get_login_credentials_format_message())
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
                                resp.message("Exam timetable currently not available" +
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
                                                if results is not False:
                                                    for semi in results:
                                                        resp.message(semi)
                                                else:
                                                    resp.message(app_utils.get_previous_exam_not_available() +
                                                                 app_utils.get_exam_results_option_message() +
                                                                 app_utils.get_portal_home_or_previous_page_message())
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
                                    if assessments is not False:
                                        for value in assessments:
                                            resp.message(value)
                                    else:
                                        resp.message(app_utils.get_assessment_not_available_message('1') +
                                                     app_utils.get_assessment_message())
                                    resp.message(app_utils.get_portal_home_or_previous_page_message())
                                # semester 2
                                elif msg == '2':
                                    assessments = student_portal.get_assessments_details(user_session, '2')
                                    if assessments is not False:
                                        for value in assessments:
                                            resp.message(value)
                                    else:
                                        resp.message(app_utils.get_assessment_not_available_message('2') +
                                                     app_utils.get_assessment_message())
                                    resp.message(app_utils.get_portal_home_or_previous_page_message())

                                elif msg == '3':
                                    pass  # revisit
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

                            # end of exam timetable
                            # start of accommodation option
                            if session['key3'] == '6':
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
                pass
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
