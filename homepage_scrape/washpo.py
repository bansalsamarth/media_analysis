import requests, time
from bs4 import BeautifulSoup
from get_current_time import *

publication = "washpo"

URL = "https://www.washingtonpost.com/"

data = {
	'main_right': [],
	'main_left': [],
	'opinion': [],
    'more_stories': []
}

homepage = requests.get(URL)
scrape_time = get_time()

page = BeautifulSoup(homepage.content)

#Whats News

main_content = page.find('section', id='main-content').find('div', class_='no-skin')

main_content_left = main_content.find('div', class_='top-table-col-left')
main_content_right = main_content.find('div', class_='top-table-col-right')

for headline in main_content_right.find_all('div', class_='headline'):
    link = headline.find('a')['href']
    data['main_right'].append(link)

for rel_link in main_content_right.find_all('ul', class_='related-links'):
    li = rel_link.find_all('li')
    for l in li:
        link = l.find('a')['href']
        data['main_right'].append(link)

for headline in main_content_left.find_all('div', class_='headline'):
    link = headline.find('a')['href']
    data['main_left'].append(link)

for rel_link in main_content_left.find_all('ul', class_='related-links'):
    li = rel_link.find_all('li')
    for l in li:
        link = l.find('a')['href']
        data['main_left'].append(link)

opinion = page.find('div', class_='opinions-chain').findAll('div', class_='headline')
for i in opinion:
     link = i.find('a')['href']
     data['opinion'].append(link)


more_stories_tags = ['hp-more-top-stories','hp-more-top-stories-2']

for tag in more_stories_tags:
    more_stories = page.find('div', {'data-chain-name': tag})

    for headline in more_stories.find_all('div', class_='headline'):
        link = headline.find('a')['href']
        data['more_stories'].append(link)

    for rel_link in more_stories.find_all('ul', class_='related-links'):
        li = rel_link.find_all('li')
        for l in li:
            link = l.find('a')['href']
            data['more_stories'].append(link)


#save to database
from save_db import *
save_data_db(data, "news_stories", publication, scrape_time)
