
# Elon Musk Should Be Shot

# Tweepy library needed. If not installed, use command line or terminal. 
import tweepy

# Place holder API keys and tokens, can be generated via twitter developer account. API Keys and Tokens must be secret at all times. Expired account is used for this.
api_key = "[REDACTED]"
api_secret = "[REDACTED]"
access_token = "[REDACTED]"
access_token_secret = "[REDACTED]"


# Twitter Authenticate, allow interaction with twitter user account
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

# API Object, allows creation for tweets
api = tweepy.API(auth)

api.create_tweet(text="I AM ALIVE!!!!!!")

