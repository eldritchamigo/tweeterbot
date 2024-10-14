
# Elon Musk Should Be Shot
import tweepy

# Place holder API keys and tokens
api_key = "[REDACTED]"
api_secret = "[REDACTED]"
access_token = "[REDACTED]"
access_token_secret = "[REDACTED]"


#Twitter Authenticate
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

#API Object
api = tweepy.API(auth)

api.create_tweet(text="I AM ALIVE!!!!!!")

