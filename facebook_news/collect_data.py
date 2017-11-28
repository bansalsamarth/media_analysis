import sys, os

from functions import *

#Facebook Auth Credentials
APP_ID = os.environ['NEWS_FB_APP_ID']
APP_SECRET = os.environ['NEWS_FB_APP_SECRET']
ACCESS_TOKEN = APP_ID + "|" + APP_SECRET

#Get page id form command line arguments
PAGE_ID = sys.argv[-1]

scrapeFacebookPageFeedStatus(PAGE_ID, ACCESS_TOKEN)
