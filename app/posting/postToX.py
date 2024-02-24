import tweepy
import json

def post_to_x(post_text):
    # the keys in x_auth.json are currently associated with https://twitter.com/CAS502_Project
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


