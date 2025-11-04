from flask_apscheduler import APScheduler
from flask import current_app
import time


scheduler = APScheduler()




def scheduled_job():
    current_app.logger.info("Scheduled job çalıştı - zaman: %s", time.strftime("%Y-%m-%d %H:%M:%S"))



def init_scheduler(app):
    scheduler.init_app(app)
    scheduler.start()
