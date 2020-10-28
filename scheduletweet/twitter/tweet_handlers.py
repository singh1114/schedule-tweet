import logging
import arrow
import os
import tweepy
import pandas as pd

# from twitter.models import TwitterSchedulerModel

logger = logging.getLogger(__name__)


def send_tweets(consumer_key, consumer_secret, access_token,
                access_token_secret, tweet):
    # expired_tweets = TwitterSchedulerModel.objects.filter(
    #     sent=False, tweet_at__lte=arrow.utcnow().datetime)
    expired_tweets = get_non_sent_tweets()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    if expired_tweets.count() == 0:
        logging.info("No tweet to send as of now")
    for db_tweet in expired_tweets:
        logging.info('sending tweet')
        api.update_status(tweet)
        logging.info('tweet sent')


def switch_to_arrow(df):
    df['tweet_at'] = arrow.get(df['tweet_at'])
    return df


def get_non_sent_tweets(consumer_key, consumer_secret, access_token, access_token_secret):
    df = pd.read_csv('tweets.csv')
    new_df = df.apply(switch_to_arrow, axis=1)
    applicable_rows = new_df[(new_df['sent']==False) & (new_df['tweet_at'] < arrow.utcnow())]
    for index, data in applicable_rows.iterrows():
        send_tweets(
            consumer_key, consumer_secret, access_token, access_token_secret, data['tweet'])
        new_df.loc[new_df['sno'] == data['sno'], 'sent'] = True
    new_df.to_csv()


def tweet_scheduler():
    if (os.environ.get('CONSUMER_KEY') or os.environ.get('CONSUMER_SECRET') or
       os.environ.get('ACCESS_TOKEN') or os.environ.get('TOKEN_SECRET')):
        consumer_key = os.environ.get('CONSUMER_KEY')
        consumer_secret = os.environ.get('CONSUMER_SECRET')
        access_token = os.environ.get('ACCESS_TOKEN')
        access_token_secret = os.environ.get('TOKEN_SECRET')
        get_non_sent_tweets(consumer_key, consumer_secret, access_token, access_token_secret)
    else:
        raise NotImplementedError('Set environment variables correctly')
