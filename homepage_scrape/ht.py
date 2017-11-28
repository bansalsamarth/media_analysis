import requests, time
from bs4 import BeautifulSoup
from get_current_time import *

publication = "hindustantimes"

HT_URL = "http://www.hindustantimes.com"

ht_data = {
	'top_three': [],
	'latest_news': [],
	'dont_miss': [],
	'video_news':[],
	'editors_pick': []
}


homepage = requests.get(HT_URL)

scrape_time = get_time()

page = BeautifulSoup(homepage.content)

top = page.findAll('ul', class_="top-story-coll clearfix")[0].findAll('li')

for li in top:
	ht_data['top_three'].append(li.find('a')['href'])

latest_news = page.find('div', class_="row breaking-news-area").find('div', class_="col-md-9").find('ul').findAll('li')

for i in latest_news:
	ht_data['latest_news'].append(i.find('a')['href'])

dont_miss = page.find('div', class_='new-assembly-elections').findAll('ul')

for i in dont_miss:
	li = i.findAll('li')
	for l in li:
		ht_data['dont_miss'].append(l.find('div', class_='media-body').find('a')['href'])

videos = page.find('div', class_='new-video-news').findAll('li')
for v in videos:
	ht_data['video_news'].append(v.find('a')['href'])

editor_pick = page.find('div', class_='editor-pick-section').find('div', class_='row').findAll('div', class_='headingfour')
for ep in editor_pick:
	ht_data['editors_pick'].append(ep.find('a')['href'])

#save to database
from save_db import *
save_data_db(ht_data, "news_stories", publication, scrape_time)