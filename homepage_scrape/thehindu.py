import requests,time
from bs4 import BeautifulSoup
from get_current_time import *

publication = "thehindu"

THEHINDU_URL = "http://www.thehindu.com"

the_hindu_data = {
	'lead_story': [],
	'main_top': [],
	'main_bottom': [],
	'just_in': [],
	'top_picks': []
}

homepage = requests.get(THEHINDU_URL)
scrape_time = get_time()

page = BeautifulSoup(homepage.content)

#Get the first main div on the hompage
first_main = page.find("div", class_="main")

#lead story on the page
lead_story = first_main.find('a', class_="ls50x3Bluebg-img focuspoint")
the_hindu_data['lead_story'].append(lead_story['href'])

#main stories in the top section
main_stories = first_main.findAll('a', class_="story-card-img focuspoint ")
for i in main_stories:
	the_hindu_data['main_top'].append(i['href'])

#two main stories after 'Just In'
main_bottom_two = page.findAll('div', class_="main")[1].findAll('h3')
for i in main_bottom_two:
	the_hindu_data['main_bottom'].append(i.find('a')['href'])

#just in section on the homepage.
just_in_section = page.find("div", class_="justin-100x3-container hidden-xs").findAll('a')
for i in just_in_section:
	the_hindu_data['just_in'].append(i['href'])

#Top Picks
top_picks_section = page.find('div', class_="main section-carousel-full").findAll('h3')
for i in top_picks_section:
	the_hindu_data['top_picks'].append(i.find('a')['href'])

#save to database
from save_db import *
save_data_db(the_hindu_data, "news_stories", publication, scrape_time)