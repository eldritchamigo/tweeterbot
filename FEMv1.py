
# Fuck Elon Musk
import tweepy

# Place holder API keys and tokens
api_key = "[REDACTED]"
api_secret = "[REDACTED]"
access_token = "[REDACTED]"
access_token_secret = "[REDACTED]"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status("I AM ALIVE!!!!!!")

