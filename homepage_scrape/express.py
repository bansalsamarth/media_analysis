import requests, time
from bs4 import BeautifulSoup
from get_current_time import *

publication = "express"

EXPRESS_URL = "http://www.indianexpress.com"

express_data = {
	'lead_story': [],
	'lead_bottom': [],
	'lead_right': [],
	'lead_two_left': [],
	'lead_two_right': []
}

homepage = requests.get(EXPRESS_URL)
scrape_time = get_time()

page = BeautifulSoup(homepage.content)

lead_story = page.find('div', class_="ie-first-story").find('a')['href']
express_data['lead_story'].append(lead_story)

lead_bottom = page.find('div', class_='left-part').find('div', class_="news").find('a')['href']
express_data['lead_bottom'].append(lead_bottom)

lead_right = page.find('div', class_='right-part').find('div', class_='top-news').findAll('a')
for i in lead_right:
	express_data['lead_right'].append(i['href'])

lead_two_left = page.find('div', attrs={'data-vr-zone':'Lead Story Two'}).findAll('h3')

for i in lead_two_left:
	express_data['lead_two_left'].append(i.find('a')['href'])

lead_two_right = page.find('div', class_="right-part bg").findAll('li')

for i in lead_two_right:
	express_data['lead_two_right'].append(i.find('a')['href'])

#save to database
from save_db import *
save_data_db(express_data, "news_stories", publication, scrape_time)