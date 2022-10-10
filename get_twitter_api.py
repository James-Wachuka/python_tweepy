import tweepy

def twitter_api():
    # input your twitter API credentials
    consumer_key = "CvZaGFcvsOdgg1vOr7kClZAgQ"
    consumer_secret = "NYedUoy4ksrlVyAo47EJnF5ZHY45spl3tW43U38LCkv0SitLmO"
    access_token = "1357221708541939714-SDICyG3wVh6BbnZ73voX1vqPeMpk1l"
    access_token_secret = "prqlcC2XzVfbZs3YUasg3IhSWYrcDoGZgcvqdjJubHYol"
    # authentication of consumer key and secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # authentication of access token and secret
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api
