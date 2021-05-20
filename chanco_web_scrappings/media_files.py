"""This Module contains all files ie images , pdf , docs  etc , from chancellor college
Official website.
 """
from chanco_web_scrappings.general_methods import *

defaultImage = "https://freepikpsd.com/wp-content/uploads/2019/10/no-image-png-5-Transparent-Images.png"


# Student portal image
def get_portal_display_image(reg_number):
    return "https://portal.cc.ac.mw/students/images/scripts/display_image.php?id={}".format(reg_number)


"""Chancellor college adimistration officers images"""


def get_principal_image():
    try:
        soup = get_soup('https://www.cc.ac.mw/office/principal/biography')
        return soup.find('div', class_="col-xs-3 principal").img['src']
    except Exception as _:
        return defaultImage


def get_vice_principal_image():
    try:
        soup = get_soup('https://www.cc.ac.mw/office/principal/biography-vice')
        return soup.find('div', class_="col-xs-3 principal").img['src']
    except Exception as _:
        return defaultImage


def get_dean_of_students_image():
    try:
        soup = get_soup('https://www.cc.ac.mw/office/dean-of-students/staff')
        return soup.find('div', class_="col-xs-3 principal").img['src']
    except Exception as _:
        return defaultImage


def get_registrars_image():
    try:
        soup = get_soup('https://www.cc.ac.mw/office/registrar/staff')
        return soup.find('div', class_="col-xs-3 principal").img['src']
    except Exception as _:
        return defaultImage


# news images
def get_news_image():
    try:
        soup = get_soup("https://www.cc.ac.mw/news")
        news = soup.find('div', class_="col-xs-12").find_all('div', class_='news')
        for item in news:
            item_1 = item.find('div', class_="row news-snippet").find('a')['href']
            soup_1 = get_soup("https://www.cc.ac.mw/{}".format(item_1))
            newsImageLInk = soup_1.find('div', class_="col-xs-11").find('div', class_="news-image").find('img')[
                'src']
            yield newsImageLInk

    except Exception:
        return False


# Article images
def get_article_image():
    try:
        soup = get_soup("https://www.cc.ac.mw/news/articles")
        news = soup.find('div', class_="col-xs-12").find_all('div', class_='news')
        for item in news:
            item_1 = item.find('div', class_="row news-snippet").find('a')['href']
            soup_1 = get_soup("https://www.cc.ac.mw/{}".format(item_1))
            newsImageLInk = soup_1.find('div', class_="col-xs-11").find('div', class_="news-image").find('img')[
                'src']
            yield newsImageLInk

    except Exception:
        return False


"""Images about chancellor college places"""

# library image
about_library_image = get_about_chanco_places_image("https://www.cc.ac.mw/library")

# The great hall image
about_great_hall_image = get_about_chanco_places_image('https://www.cc.ac.mw/great-hall')

# Cafeteria image
about_cafeteria_image = get_about_chanco_places_image('https://www.cc.ac.mw/cafetaria')

# About senior commons room image
about_senior_commons_room = get_about_chanco_places_image('https://www.cc.ac.mw/senior-common-room')

# About clinic image
about_clinic_image = get_about_chanco_places_image('https://www.cc.ac.mw/clinic')

# About Junior commons room image
about_junior_commons_room_image = get_about_chanco_places_image('https://www.cc.ac.mw/junior-common-room')

about_sports_complex_image = get_about_chanco_places_image('https://www.cc.ac.mw/sports-complex')

"""Images about Faculties and Deans of Faculties"""
# faculty of science
faculty_of_science_image = get_faculty_image('https://www.cc.ac.mw/faculty/science')
dean_of_science_image = get_dean_of_faculty_image('https://www.cc.ac.mw/faculty/science/dean')
# Faculty of law
faculty_of_law_image = get_faculty_image('https://www.cc.ac.mw/faculty/law')
dean_of_law_image = get_dean_of_faculty_image('https://www.cc.ac.mw/faculty/law/dean')

# Faculty of education
faculty_of_education_image = get_faculty_image('https://www.cc.ac.mw/faculty/education')
dean_of_education_image = get_dean_of_faculty_image('https://www.cc.ac.mw/faculty/education/dean')
# Faculty of social science
faculty_social_science_image = get_faculty_image_2('https://www.cc.ac.mw/faculty/social-science')

dean_of_social_science_image = get_dean_of_faculty_image('https://www.cc.ac.mw/faculty/social-science/dean')

# Faculty of humanities
faculty_of_humanities_image = get_faculty_image_2('https://www.cc.ac.mw/faculty/humanities')
dean_of_humanities_image = get_dean_of_faculty_image('https://www.cc.ac.mw/faculty/humanities/dean')


# prospectus
def get_prospectus():
    soup = get_soup('https://www.cc.ac.mw/')
    if soup is not False:
        try:
            return soup.find('div', class_="unima_selection").a['href']
        except Exception as _:
            return False
    else:
        return False


def get_international_student_image():
    soup = get_soup('https://www.cc.ac.mw/people/students/students-international')
    if soup is not False:
        try:
            return 'https://www.cc.ac.mw' + soup.find('div', class_="content-inner-wide").p.img['src']
        except Exception as _:
            return False
    else:
        return False


if __name__ == '__main__':
    print(about_clinic_image)
