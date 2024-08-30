
import tweepy
'''
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

text = "I am gonna fucking die from this bullshit."
result = classifier(text)

print(result)'''

api_key = 'tGUsDJtO93azUBK5PjBjZFHIA'
api_secret = 'FvkGvw13z5X6o2BQi2T1sIvzCmrCmgBn23Ne1CR5odDClefprv'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAA6EvgEAAAAABaA4n0OJHFAu75g1UUY1HghiFFI%3DfhQFKCqtzkRJigpaYFGZJnPsW272UGJCPfE1JqV6Vu753k329B'
access_token = '1772960619139854336-9RkdHcFCfUXBB6eZmxeDgBf5ziJsYK'
access_secret = 'uuDJAgNhb4SCVkO8KJ2K82ZPgkw8tT5FJWKi8ElhZZ9Hf'

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

client.create_tweet(text="Testing going fine")