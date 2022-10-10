import tweepy

def twitter_api():
    # input your twitter API credentials
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""
    # authentication of consumer key and secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # authentication of access token and secret
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api
