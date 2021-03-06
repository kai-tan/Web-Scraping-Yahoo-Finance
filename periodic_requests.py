import requests
import pytz
from apscheduler.schedulers.twisted import TwistedScheduler 
from twisted.internet import reactor 

def send_request():
    requests.post("https://serene-earth-26453.herokuapp.com/schedule.json", data={
        'project': 'default', 
        'spider': 'yahoo_finances'
    })

if __name__ == '__main__': 
    scheduler = TwistedScheduler(timezone=pytz.utc)
    scheduler.add_job(send_request, 'cron', day_of_week='mon-sun', hour='22', minute='30')
    scheduler.start()
    reactor.run()