from datetime import datetime
from pytz import timezone    

def get_time():
	india = timezone('Asia/Kolkata')
	ind_time = datetime.now(india)
	return ind_time.strftime('%Y-%m-%d %H:%M:%S')
