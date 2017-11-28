import requests, time
from bs4 import BeautifulSoup
from get_current_time import *

publication = "guardian_us"

URL = "https://www.theguardian.com/us"

data = {
	'headlines_top_lead': [],
    'headlines_top_right': [],
    'headlines_top_bottom': [],
	'spotlight': [],
}

homepage = requests.get(URL)
scrape_time = get_time()

page = BeautifulSoup(homepage.content)

#Headlines section
headlines = page.find('section', id='headlines').find('div', class_='fc-container--rolled-up-hide fc-container__body').findAll('div', class_='fc-slice-wrapper')

#headlines has two sections -- top and bottom

#top_lead
top_lead = headlines[0].find('li', class_="fc-slice__item l-row__item l-row__item--span-3 u-faux-block-link").findAll('a')

links = []
for i in top_lead:
    links.append(i['href'])
for link in set(links):
        data['headlines_top_lead'].append(link)

#top_right_lead
top_right_lead = headlines[0].find('li', class_="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link").findAll('a')
links = []
for i in top_right_lead:
    links.append(i['href'])
for link in set(links):
        data['headlines_top_right'].append(link)

#all stories in headlines bottom
top_bottom = headlines[1].find('ul').findAll('a')
links = []
for i in top_bottom:
    links.append(i['href'])
for link in set(links):
        data['headlines_top_bottom'].append(link)



#all stories in spotlight section
spotlight = page.find('section', id='spotlight').find('div', class_='fc-container--rolled-up-hide fc-container__body').findAll('div', class_='fc-slice-wrapper')

for i in spotlight:
    a = i.findAll('a')
    links = []
    for i in a:
        links.append(i['href'])
    for link in set(links):
            data['spotlight'].append(link)


#save to database
from save_db import *
save_data_db(data, "news_stories", publication, scrape_time)
