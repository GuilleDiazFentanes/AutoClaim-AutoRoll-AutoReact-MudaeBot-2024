import vars
import time
import schedule
from Function import simpleRoll

timeString = ':'+ str(vars.repeatMinute)
schedule.every().hour.at(timeString).do(simpleRoll)

while True:
    schedule.run_pending()
    time.sleep(1)