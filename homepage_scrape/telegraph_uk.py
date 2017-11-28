import requests, time
from bs4 import BeautifulSoup
from get_current_time import *

def get_full_link(url):
    #if returned link like "/news/world-us-canada-41936594" convert to "http://www.bbc.com/news/world-us-canada-41936594"

    if '.co.uk' in url:
        return url
    else:
        return 'http://www.telegraph.co.uk' + url


publication = "telegraph_uk"

URL = "http://www.telegraph.co.uk/"

data = {
	'headlines_upper': [],
	'headlines_below': [],
	'opinion': []
}

homepage = requests.get(URL)
scrape_time = get_time()

page = BeautifulSoup(homepage.content)

#Whats News

col = page.find('section', class_='p_hub__section_1 container container--1').find('article', class_='col col_1')

headlines_upper = col.select('div.curatedList2')[0].findAll('a')
links = []
for i in headlines_upper:
		links.append(i['href'])
for link in set(links):
        data['headlines_upper'].append(get_full_link(link))


headlines_below = col.select('div.splitter.section')[0].findAll('a')
links = []
for i in headlines_below:
		links.append(i['href'])
for link in set(links):
        data['headlines_below'].append(get_full_link(link))

opinion = page.select('div.opinion.section')[0].select('div.segment-container__content')[0].findAll('a')
links = []
for i in opinion:
		links.append(i['href'])
for link in set(links):
        data['opinion'].append(get_full_link(link))


#save to database
from save_db import *
save_data_db(data, "news_stories", publication, scrape_time)
