"""This module craps all news and events , announcements from chanco official
 website"""
from chanco_web_scrappings.general_methods import get_soup


# scrapping news
def get_news():
    try:
        soup = get_soup("https://www.cc.ac.mw/news")
        news = soup.find('div', class_="col-xs-12").find_all('div', class_='news')

        for index, item in enumerate(news, start=1):
            # make sure to only print few news items in this case 7
            if index > 7:
                break
            item_1 = item.find('div', class_="row news-snippet").find('a')['href']

            soup_1 = get_soup("https://www.cc.ac.mw/{}".format(item_1))
            newsHeading = soup_1.find('div', class_="col-xs-11").h3
            newsItem = soup_1.find('div', class_="col-xs-11").find('div', class_="news-content")

            newsBody = ''
            for word in newsItem.text.split(' '):
                if len(newsBody) < 1500:
                    if word != None:
                        newsBody += word.strip() + ' '

            yield "{} {}".format('*' + newsHeading.text + '*',
                                 newsBody + '.. for more news visit https://www.cc.ac.mw/news')
    except Exception as _:
        return False


# scrapping articles
def get_articles():
    try:
        soup = get_soup("https://www.cc.ac.mw/news/articles")
        articles = soup.find('div', class_="col-xs-12").find_all('div', class_='news')

        for item in articles:
            item_1 = item.find('div', class_="row news-snippet").find('a')['href']

            soup_1 = get_soup("https://www.cc.ac.mw/{}".format(item_1))

            articleHeading = soup_1.find('div', class_="col-xs-11").h3
            articleSubHeading = soup_1.find('div', class_="news-snippet-head")
            soupBody = soup_1.find('div', class_="col-xs-11").find('div', class_="news-content")
            articleBody = ''
            for word in soupBody.text.split(' '):
                if len(articleBody) < 1100:
                    if word is not None:
                        articleBody += word.strip() + ' '

            yield "{} {} {}".format('*' + articleHeading.text + '*' + '\n', '*' + articleSubHeading.text + '*' + '\n',
                                    articleBody + '.. visit cc.ac.mw for more')

    except Exception as _:
        return False


# crapping events
def get_events():
    try:
        soup = get_soup("https://www.cc.ac.mw/events")
        events = soup.find('div', class_="col-xs-12").find_all('a')

        # crap link for each event and visit its page for more details
        for index, item in enumerate(events, start=1):
            # make sure to only print few events items in this case 7
            if index > 7:
                break
            eventLink = item['href']
            soup_1 = get_soup("https://www.cc.ac.mw/{}".format(eventLink))

            # crap each part and yield it as a tuple
            eventHeading = soup_1.find('div', class_="col-xs-11").h3
            eventDetails = soup_1.find('div', class_="col-xs-11").find('div', class_="row event-details")
            soupBody = soup_1.find('div', class_="col-xs-11").find('div', class_="news-content")
            eventBody = ''
            for word in soupBody.text.split(' '):
                if len(eventBody) < 1340:
                    if word is not None:
                        eventBody += word.strip() + ' '

            yield "{} {} {}".format('*' + eventHeading.text + '*', eventDetails.text, eventBody)

    except Exception as _:

        return False


# crapping vacancies
def get_vacancies():
    try:
        soup = get_soup("https://www.cc.ac.mw/vacancies")
        vacancies = soup.find('div', class_="col-xs-12").find_all('a')

        # scrap link for each vacancy and visit its page for more details
        for index, item in enumerate(vacancies, start=1):
            # make sure to only print few vacancy items in this case 7
            if index > 7:
                break
            eventLink = item['href']
            soup_1 = get_soup("https://www.cc.ac.mw/{}".format(eventLink))

            vacancyHeading = soup_1.find('div', class_="col-xs-11").h3
            vacancyDetails = ''
            soupBody = soup_1.find('div', class_="col-xs-11").find('div', class_="news-content")
            vacancyBody = ''

            for word in soupBody.text.split(' '):
                if len(vacancyBody) < 1300:
                    if word is not None:
                        vacancyBody += word.strip() + ' '

            # formatting vacancy detail body to a string displayable to whatsApp
            vacancyDetailSoup = soup_1.find('div', class_="col-xs-11").find('div', class_="row event-details")
            vacancyDetailList = []

            for vacancyDetail in vacancyDetailSoup.text.split('\n'):  # converting details to list
                if vacancyDetail != '':
                    vacancyDetailList.append(vacancyDetail.replace('\t', '').strip())

            # appending items from the list to a formatted string
            for index_1, detailItem in enumerate(vacancyDetailList, start=1):
                vacancyDetails += '*' + detailItem + '*'
                if index_1 % 2 == 0:  # making sure two items exist in a single row
                    vacancyDetails += '\n'

            yield '{}{}{}'.format('*' + vacancyHeading.text.strip() + '*\n\n', vacancyDetails + '\n\n',
                                  vacancyBody + '.visit https://www.cc.ac.mw for more')  # yield a tuple

    except Exception as _:

        return False

