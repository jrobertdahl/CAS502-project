import tweepy
import json
# set up docker to install tweepy

with open('x_auth.json') as json_file:
    auth_keys = json.load(json_file)
 
client = tweepy.Client(
    consumer_key=auth_keys['consumer_key'], consumer_secret=auth_keys['consumer_secret'],
    access_token=auth_keys['access_token'], access_token_secret=auth_keys['access_token_secret']
)

response = client.create_tweet(
    text="dockerfile test"
)

print(f"https://twitter.com/user/status/{response.data['id']}")

# def testPostFunction(name, milesTraveled):
    # print(f'{name} traveled {milesTraveled} miles the other day')


