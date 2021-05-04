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


""" Chancellor college student portal display messages"""


def get_invalid_input_message():
    return "_*oops*! It seems like your selection didn't match any of the options provided_. Please Try again! \n\n"


def get_login_credentials_format_message():
    return "\U0001F6AA' _Provide your login information in the following format to login. Make sure to include a " \
           "space between registration number and password._ \n\n\t\t*bsc-23-14   Ywz9FzU2* \n\n \U000026A0 *Please " \
           "make sure to delete your login credentials after finishing to prevent others from seeing them*\n\n "


def get_validate_login_credentials(msg):
    try:
        a, b = msg.replace("\n", " ").split(' ', 1)
        return [a, b]

    except ValueError:
        return False


def get_invalid_login_credentials_message():
    return "\U000026D4 _Sorry! You didn't provide your login information in a correct format. Please try again_ " \
           "Make sure to include a space between your Registration number and Password\n\n"


def get_login_unsuccessful_login_message():
    return '\U000026D4 _Sorry your login was Unsuccessful. Make sure your login details are correct or try again ' \
           'later _ \n\n'


def get_portal_home_message(session):
    return "Welcome  " + "*" + student_portal.get_student_name(
        session) + "*" + ". You have Successfully logged in. Please " \
                         "proceed by selecting an option below \n\n1.\U0001F468 My profile \n\n2.\U0001F4C3 Exam " \
                         "Results \n\n3.\U0001F4D1 Assessments \n\n4.\U0001F5C4 My courses\n\n5.\U0001F4C5 Exam " \
                         "Timetable \n\n6.\U0001F3D8 Accommodation "


def get_back_to_cc_home_or_previous_page_message():
    return "\n\n.0 \U00002B05 Back  \n\n.## \U00002196 Go to CC main menu \n\n Type exit or cancel to exit the session"


def get_back_to_portal_home_or_previous_page_message():
    return "\n\n.0 \U00002B05 Back \n\n.00 \U000021A9 Portal main menu \n\n.## \U00002196 Logout and go to CC main menu"


# Message to be displayed when a profile option is selected
def get_profile_option_display_message(session):
    return student_portal.get_profile_welcome_message(session) + "\n\n1. Bio data \n\n2. Academic details " \
                                                                 "\n\n3.Financial details \n\n.4 Contact details \n\n"


# Display message when exam result option is selected
def get_balance_massage(session):
    return "\U000026D4 _Sorry you can't see your results at the moment because you have an outstanding balance of " \
           "*MK{}*. Settle this balance first to see your results_".format(student_portal.get_student_balance(session))


def get_exam_results_option_message():
    return "1. Current year exam results \n\n2.Previous years results"


def get_current_year_exam_result_message():
    return "1. First semester exam results \n\n2.Second semester exam results"


# Display message when assessment option is selected
def get_assessment_message():
    return "1. First semester assessments \n\n2.Second semester assessments \n\n3.User manual for continuous assessment"


# Display message for my courses option
def get_my_course_message():
    return "1. Current year courses \n\n 2. Previous years courses "


def get_current_year_display_message():
    return "1. First semester courses \n\n2. Second semester courses"


# Display message for accommodation option
def get_accommodation_display_message():
    return "1. Accommodation Rules \n\n2. Allocation History \n\n3. Booking history \n\n4. Notifications"


""" About chanco option messages"""


def get_chanco_display_message():
    return "1. Chanco at glance  \n\n2. Library \n\n3. Great hall \n\n4. Cafeteria \n\n.5 Senior commons room \n\n5. " \
           "Junior commons room \n\n6. Chanco clinic \n\n7. Sports complex "


"""About administration option messages"""


# Front display message
def get_about_administration_message():
    return "1. Principal \n\n2. Dean of students \n\n3. Registrar \n\n5. Finance "


# principal option display message
def get_principal_option_display_message():
    return "1. Office Overview \n\n.2 Principal \n\n.3 vice principal \n\n.4 History \n\n.5 Contacts"


# dean of students or registrars option display message
def get_dean_of_students_registrar_option_message():
    return "1. Office overview \n\n2. Officers \n\n3. Contacts"


# Finance display message
def get_finance_display_message():
    return "1. Office overview \n\n2. Contacts"


"""About news and events option display messages"""


def get_about_news_and_events_display_message():
    return "1. News \n\n.2 Articles \n\n3. Events \n\n4. Vacancies"


"""About Faculties option display message"""


# Front display message
def get_about_faculties_display_message():
    return "1. Faculty of science \n\n2. Faculty of law \n\n3. Faculty of education \n\n4. Faculty of social science" \
           " \n\n5. Faculty of humanities"

# faculty display message
def get_faculty_display_message():
    return "1. Faculty overview \n\n2. Faculty dean details \n\n3. Faculty departments \n\n4. Faculty contacts"
