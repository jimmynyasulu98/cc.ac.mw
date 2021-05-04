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
                                    student_portal.get_student_registration_number(user_session))+'')

                                session['key2'] = '1'
                                session['key3'] = ''
                            else:
                                resp.message(app_utils.get_login_unsuccessful_message())
                                resp.message(app_utils.get_login_credentials_format_message())

                        else:
                            resp.message('Login was unsuccessful try later')

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
                                resp.message(app_utils.get_my_course_message())
                                session['key3'] = '4'
                            elif msg == '5':
                                # exam timetable message
                                resp.message("Exam timetable currently not available")
                                session['key3'] = '5'
                            elif msg == '6':
                                # Accommodation message
                                resp.message(app_utils.get_accommodation_display_message())
                                session['key3'] = '6'
                            else:
                                resp.message(
                                    app_utils.get_invalid_input_message() + app_utils.get_portal_home_message(
                                        user_session))

                            # session['key4'] = ''
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
                                    resp.message(app_utils.get_portal_home_message(user_session))

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
