import requests, time
from bs4 import BeautifulSoup
from get_current_time import *

def get_full_link(url):
    if '.ca' in url:
        return url
    else:
        return 'http://nationalpost.com' + url


publication = "nationalpost"

URL = "http://nationalpost.com/"

data = {
	'featured': [],
	'second_section': [],
}

homepage = requests.get(URL)
scrape_time = get_time()

page = BeautifulSoup(homepage.content)

top_section = page.find('section', id='section_1')
articles = top_section.find_all('article')

for article in articles:
    link = article.find('a')['href']
    data['featured'].append(get_full_link(link))


second_section = page.find('section', id='section_2')
articles = second_section.find_all('article')

for article in articles:
    link = article.find('a')['href']
    data['second_section'].append(get_full_link(link))

#save to database
from save_db import *
save_data_db(data, "news_stories", publication, scrape_time)
