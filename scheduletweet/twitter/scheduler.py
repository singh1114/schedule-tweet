from twitter.tweet_handlers import tweet_scheduler
from apscheduler.schedulers.background import BackgroundScheduler


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        tweet_scheduler, 'interval', minutes=5)
    scheduler.start()