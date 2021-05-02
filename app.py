from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from chanco_web_scrappings import *
import app_utils
import requests
from serialiser import *

SECRET_KEY = 'a secret ke'
app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def hello():
    return "cc.ac.mw services"


@app.route("/sms", methods=['POST'])
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

                if session['key2'] == '':
                    if app_utils.get_validate_login_credentials(msg) is not False:
                        log = app_utils.get_validate_login_credentials(msg)
                        username = log[0]
                        password = log[1]

                        try:
                            user_session = student_portal.LoginSession(username, password,
                                                                       requests.Session()).get_session()
                            if student_portal.is_user_logged_in(user_session):
                                mess = app_utils.get_portal_home_message(user_session)
                                session['mySession'] = serialize_session(user_session)
                                resp.message(mess)
                                session['key2'] = '1'
                            else:
                                resp.message('Your login was unsuccessful')
                                resp.message(app_utils.get_login_credentials_format_message())

                        except Exception as _:
                            resp.message('Login was unsuccessful try later')

                    else:
                        resp.message("Sorry! It seems like you didn't provide info in a correct format")
                        resp.message(app_utils.get_login_credentials_format_message())
                else:
                    if msg == "1":
                        resp.message("Profile")
                    elif msg == "2":
                        resp.message("Exam Results")
                    elif msg == '3':
                        resp.message("Assessments")
                    elif msg == '4':
                        resp.message("My courses")
                    elif msg == '5':
                        resp.message("Exam Timetable")
                    elif msg == '6':
                        resp.message("Accommodation")
                    else:
                        resp.message("Invalid input")
                return str(resp)
            # end of chanco student portal services

            else:
                pass

    else:
        counter += 1
        session['counter'] = counter
        session['key1'] = ''
        resp.message(app_utils.get_welcoming_message())
        return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
