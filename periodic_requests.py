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
    scheduler.add_job(send_request, 'cron', day_of_week='mon-fri', hour='22', minute='0', jitter=120)
    scheduler.start()
    reactor.run()