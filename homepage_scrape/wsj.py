import requests, time
from bs4 import BeautifulSoup
from get_current_time import *

publication = "wsj"

URL = "https://www.wsj.com/"

data = {
	'whats_news': [],
	'featured_strip': [],
	'opinion': []
}

homepage = requests.get(URL)
scrape_time = get_time()

page = BeautifulSoup(homepage.content)

#Whats News
whats_news = page.select('div.wsj-list.lead-story')[0].select('div.cb-col')

links = []
for i in whats_news:
	a = i.findAll('a')
	for i in a:
		links.append(i['href'])

for link in set(links):
        data['whats_news'].append(link)

#Featured Strip
featured_strip = page.select('div.wsj-list.featured-strip')[0].select('div.cb-col')

links = []
for i in featured_strip:
	a = i.findAll('a')
	for i in a:
		links.append(i['href'])

for link in set(links):
        data['featured_strip'].append(link)

#Opinion
opinion = page.select('div.wsj-list.opinion')[0].select('div.cb-col')

links = []
for i in opinion[1]:
	a = i.findAll('a')
	for i in a:
		links.append(i['href'])

for link in set(links):
        data['opinion'].append(link)


#save to database
from save_db import *
save_data_db(data, "news_stories", publication, scrape_time)
