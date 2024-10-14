import tweepy

api_key = "eOlHfSX20URjTE8j444KIivSi"
api_secret = "MOParXv44hvMo6GpS6hstIcMPfiioRBxX883LurdGUPUKoS8Dm"
access_token = "1843448968899895296-aLPZVHu2S9mp2Sw6EgOgQSRRCREr99"
access_token_secret = "v0qtWkRQN1mEZb6EopHQ8cLjWca4vLa6LN5q2tuwfr80V"

auth = tweepy.oAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status("I AM ALIVE!!!!!!")