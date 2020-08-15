import time
import requests
import schedule
import datetime

# Replace this variable with your own Heroku App URL and custom variable
warbler = "https://warbler-rithm14.herokuapp.com/" 

sixteen_hours = 33 # sixteen hours divided into half-hours 

def job():
    """ 
        Calls Warbler App on Heroku every 29 minutes
        for 16 hours per day to keep the server from
        going to sleep. Heroku limits free uptime to
        550 hours per week.

        This should keep Warbler "awake" from 7am-11pm 
        midnight pacific time and 10am-2am eastern.
    """
    for every_half_hour in range(sixteen_hours):
        response = requests.get(warbler)
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        print("Waking up Warbler at " + dt, response)
        time.sleep(1740) # sleep for 29 minutes

# Sta17:59rts the loop every morning at 07:00AM pacific
schedule.every().day.at("07:00").do(job) 

while True: 
    schedule.run_pending()
    time.sleep(1)