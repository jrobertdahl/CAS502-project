import tweepy
import json
# set up docker to install tweepy

def post_to_x(post_text):
    with open('posting/x_auth.json') as json_file:
        auth_keys = json.load(json_file)
    
        client = tweepy.Client(
            consumer_key=auth_keys['consumer_key'], consumer_secret=auth_keys['consumer_secret'],
            access_token=auth_keys['access_token'], access_token_secret=auth_keys['access_token_secret']
        )

        response = client.create_tweet(
            text=post_text
        )

        print(f"https://twitter.com/user/status/{response.data['id']}")


