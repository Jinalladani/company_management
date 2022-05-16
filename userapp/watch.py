from datetime import timedelta, date
import schedule
import time
from .views import my_scheduleMail

schedule.every(1).minutes.do(my_scheduleMail())
# schedule.every().day.at("").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

