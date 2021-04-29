"""This module craps all news and events , announcements from chanco official
 website"""
from chanco_web_scrappings.general_methods import get_soup


# scrapping news
def get_news():
    try:
        soup = get_soup("http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/news.html")
        news = soup.find('div', class_="col-xs-12").find_all('div', class_='news')

        for item in news:
            item_1 = item.find('div', class_="row news-snippet").find('a')['href']

            soup_1 = get_soup("http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/{}".format(item_1))
            newsHeading = soup_1.find('div', class_="col-xs-11").h3
            newsBody = soup_1.find('div', class_="col-xs-11").find('div', class_="news-content")

            yield "{} {}".format('*' + newsHeading.text + '*', newsBody.text)

    except Exception:
        return False


# scrapping articles
def get_articles():
    try:
        soup = get_soup("http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/news/articles.html")
        articles = soup.find('div', class_="col-xs-12").find_all('div', class_='news')

        for item in articles:
            item_1 = item.find('div', class_="row news-snippet").find('a')['href']

            soup_1 = get_soup("http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/news/{}".format(item_1))

            articleHeading = soup_1.find('div', class_="col-xs-11").h3
            articleSubHeading = soup_1.find('div', class_="news-snippet-head")
            articleBody = soup_1.find('div', class_="col-xs-11").find('div', class_="news-content")

            yield "{} {} {}".format('*' + articleHeading.text + '*' + '\n', '*' + articleSubHeading.text + '*' + '\n',
                                    articleBody.text)

    except Exception as _:
        return False


# crapping events
def get_events():

    try:
        soup = get_soup("http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/events.html")
        events = soup.find('div', class_="col-xs-12").find_all('a')

        # crap link for each event and visit its page for more details
        for item in events:
            eventLink = item['href']
            soup_1 = get_soup("http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/{}".format(eventLink))

            # crap each part and yield it as a tuple
            eventHeading = soup_1.find('div', class_="col-xs-11").h3
            eventDetails = soup_1.find('div', class_="col-xs-11").find('div', class_="row event-details")
            eventBody = soup_1.find('div', class_="col-xs-11").find('div', class_="news-content")

            yield "{} {} {}".format('*' + eventHeading.text + '*', eventDetails.text, eventBody.text)

    except Exception as _:

        return False


# crapping vacancies
def get_vacancies():
    try:
        soup = get_soup("http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/vacancies.html")
        vacancies = soup.find('div', class_="col-xs-12").find_all('a')

        # crap link for each vacancy and visit its page for more details
        for item in vacancies:
            eventLink = item['href']
            soup_1 = get_soup("http://127.0.0.1:8011/cc.ac.mw/www.cc.ac.mw/{}".format(eventLink))

            vacancyHeading = soup_1.find('div', class_="col-xs-11").h3
            vacancyDetails = ''
            vacancyBody = soup_1.find('div', class_="col-xs-11").find('div', class_="news-content")

            # formatting vacancy detail body to a string displayable to whatsApp
            vacancyDetailSoup = soup_1.find('div', class_="col-xs-11").find('div', class_="row event-details")
            vacancyDetailList = []

            for vacancyDetail in vacancyDetailSoup.text.split('\n'):  # converting details to list
                if vacancyDetail != '':
                    vacancyDetailList.append(vacancyDetail.replace('\t', '').strip())

            # appending items from the list to a formatted string
            for index, detailItem in enumerate(vacancyDetailList, start=1):
                vacancyDetails += '*' + detailItem + '*'
                if index % 2 == 0:  # making sure two items exist in a single row
                    vacancyDetails += '\n'

            yield '{}{}{}'.format('*' + vacancyHeading.text + '*\n\n', vacancyDetails + '\n\n',
                                  vacancyBody.text.strip())  # yield a tuple

    except Exception as _:

        return False


if __name__ == "__main__":
    news = get_vacancies()
    print(next(news))
    print(next(news))
