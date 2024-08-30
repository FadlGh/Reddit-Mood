import tweepy
import pandas as pd
import auth

client = tweepy.Client(auth.bearer_token, auth.api_key, auth.api_secret, auth.access_token, auth.access_secret)

auth = tweepy.OAuth1UserHandler(auth.api_key, auth.api_secret, auth.access_token, auth.access_secret)
api = tweepy.API(auth)

