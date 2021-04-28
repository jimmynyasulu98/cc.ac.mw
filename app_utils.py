import datetime
from chanco_web_scrappings import *


def get_welcoming_message():
    currentTime = datetime.datetime.now()
    greeting = ""
    if currentTime.hour < 12:
        greeting = '*Good morning*'
    elif currentTime.hour > 16:
        greeting = '*Good evening*'

    else:
        greeting = '*Good afternoon*'

    msg = '\U0001F3EB ' + str(
        greeting) + '\n_I am *CHANCO* whatsApp service assistant \U0001F469. Choose an option below to proceed_\n'
    services = '\n1.\U0001F3EB About Chanco \n\n2.\U0001F3E2 Administration \n\n3.\U0001F3EC Departments ' \
               '\n\n4.\U0001F3DB Faculties ' \
               '\n\n5.\U0001F509 News And Events \n\n6.\U0001F393 Student Portal \n\n7.\U0001F449 Others '
    return '{} {}'.format(msg, services)


def get_invalid_input_message():
    return "_*oops*! It seems like your selection didn't match any of the options provided_. Please Try again! \n\n"


def get_back_to_cc_home_or_previous_page_message():
    return "\n\n.0 \U00002B05 Back  \n\n.## \U00002196 Go to CC main menu"


def get_back_to_portal_home_or_previous_page_message():
    return "\n\n.0 \U00002B05 Back \n\n.00 \U000021A9 Portal main menu \n\n.## \U00002196 Logout and go to CC main menu"


def get_validate_login_credentials(msg):
    try:
        a, b = msg.replace("\n", " ").split(' ', 1)
        return [a, b]

    except ValueError:
        return False


def get_portal_home_page_message(session):
    return "Welcome  "+"*"+student_portal.get_student_name(session)+"*"+". You have Successfully logged in. Please " \
            "proceed by selecting an option below \n\n1.\U0001F468 My profile \n\n2.\U0001F4C3 Exam Results " \
            "\n\n3.\U0001F4D1 Assessments \n\n4.\U0001F5C4 My courses\n\n5.\U0001F4C5 Exam Timetable " \
            "\n\n6.\U0001F3D8 Accommodation "


def get_login_credentials_format_message():
    return "\U0001F6AA' _Provide your login information in the following format to login. Make sure to include a " \
           "space between registration number and password._ \n\n\t\t*bsc-23-14   Ywz9FzU2* \n\n \U000026A0 *Please " \
           "make sure to delete your login credentials after finishing to prevent others from seeing them*\n\n "


def get_invalid_login_credentials_message():
    return "\U000026D4 _Sorry! You didn't provide your login information in a correct format. Please try again_ " \
           "Make sure to include a space between your Registration number and Password\n\n"


def get_login_unsuccessful_login_message():
    return '\U000026D4 _Sorry your login was Unsuccessful. Make sure your login details are correct or try again ' \
           'later _ \n\n'


"""Profile messages"""
def get_profile_option_display_message(session):
    return student_portal.get_profile_welcome_message(session) + "\n\n1. Bio data \n\n2. Academic details " \
                                                                 "\n\n3.Financial details \n\n.4 Contact details \n\n"
