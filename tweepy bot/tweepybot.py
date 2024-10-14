import tweepy

api_key = "-"
api_secret = "-"
access_token = "-"
access_token_secret = "-"

auth = tweepy.oAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status("I AM ALIVE!!!!!!")
