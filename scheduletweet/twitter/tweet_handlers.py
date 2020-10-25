import logging
import arrow
import os
import tweepy

from twitter.models import TwitterSchedulerModel

logger = logging.getLogger(__name__)


def send_tweets(consumer_key, consumer_secret, access_token,
                access_token_secret):
    expired_tweets = TwitterSchedulerModel.objects.filter(
        sent=False, tweet_at__lte=arrow.utcnow().datetime)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    if expired_tweets.count() == 0:
        logging.info("No tweet to send as of now")
    for db_tweet in expired_tweets:
        logging.info('sending tweet')
        api.update_status(db_tweet.tweet)
        logging.info('tweet sent')
        db_tweet.sent = True
        db_tweet.save()


def tweet_scheduler():
    if (os.environ.get('CONSUMER_KEY') or os.environ.get('CONSUMER_SECRET') or
       os.environ.get('ACCESS_TOKEN') or os.environ.get('TOKEN_SECRET')):
        consumer_key = os.environ.get('CONSUMER_KEY')
        consumer_secret = os.environ.get('CONSUMER_SECRET')
        access_token = os.environ.get('ACCESS_TOKEN')
        access_token_secret = os.environ.get('TOKEN_SECRET')
        send_tweets(
            consumer_key, consumer_secret, access_token, access_token_secret)
    else:
        raise NotImplementedError('Set environment variables correctly')
