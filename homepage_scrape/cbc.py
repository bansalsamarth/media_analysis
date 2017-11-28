import requests, time
from bs4 import BeautifulSoup
from get_current_time import *

def get_full_link(url):
    if '.ca' in url:
        return url
    else:
        return 'http://www.cbc.ca/' + url


publication = "cbc"

URL = "http://www.cbc.ca/"

data = {
	'sidebar': [],
	'top': [],
	'more_news': [],
}

homepage = requests.get(URL)
scrape_time = get_time()

page = BeautifulSoup(homepage.content)

home = page.find('div', class_='homepage')

top = home.select('div.pageContentWrap.viewportLarge')[0].find('div',class_='contentArea').find_all('a', class_='card')
for i in top:
	link = i['href']
	data['top'].append(get_full_link(link))

sidebar = home.select('div.pageContentWrap.viewportLarge')[0].find('div',class_='sidebar').find_all('a', class_='card')
for i in sidebar:
	link = i['href']
	data['sidebar'].append(get_full_link(link))

more_news = home.find('section', class_='moreStoriesList').find('div', class_='contentListCards').find_all('a', class_='card')
for i in more_news:
	link = i['href']
	data['more_news'].append(get_full_link(link))

#save to database
from save_db import *
save_data_db(data, "news_stories", publication, scrape_time)
