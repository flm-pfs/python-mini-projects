import tweepy
import time

# Replace these with your own credentials
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(
    API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def tweet_message():
    try:
        api.update_status("Hello, this is a scheduled tweet!")
        print("Tweet posted successfully!")
    except tweepy.TweepError as e:
        print(e.reason)


if __name__ == "__main__":
    while True:
        tweet_message()
        time.sleep(3600)  # Sleep for 1 hour
