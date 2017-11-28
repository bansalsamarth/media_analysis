import requests, time
from bs4 import BeautifulSoup
from get_current_time import *

def get_full_link(url):
    #if returned link like "/news/world-us-canada-41936594" convert to "http://www.bbc.com/news/world-us-canada-41936594"

    if '.com' in url:
        return url
    else:
        return 'http://www.bbc.com' + url


publication = "bbc"

URL = "http://www.bbc.com/"

data = {
	'top_box': [],
	'news': [],
	'editors_pick': [],
}

homepage = requests.get(URL)
scrape_time = get_time()

page = BeautifulSoup(homepage.content)

top = page.find('section', class_='module module--promo module--highlight').findAll('li')

for i in top:
    link = i.find('h3').find('a')['href']
    data['top_box'].append(get_full_link(link))

news = page.find('section', class_='module module--news module--collapse-images').findAll('li')

for i in news:
    link = i.find('h3').find('a')['href']
    data['news'].append(get_full_link(link))

ed_pick =  page.find('div', class_='editors-picks ').findAll('li') #page.find('section', class_='module module--collapse-images module--collapse-images module--highlight module--editors-picks').find('div', _class='editors-picks ').findAll('li')

for i in ed_pick:
    link = i.find('h3').find('a')['href']
    data['editors_pick'].append(get_full_link(link))

#save to database
from save_db import *
save_data_db(data, "news_stories", publication, scrape_time)
