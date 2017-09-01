# -*- coding: utf-8 -*-

import json
import config
#import local_config as config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

TWITTER_STATUS_FOLLOWERS = {}
TWITTER_STATUS_TWEETS = {}
TWITTER_STATUS_FAVOURITES = {}

for user_id_key in config.USER_ID:
    params ={'count' : 1,'user_id' : config.USER_ID[user_id_key]}
    req = twitter.get(url, params = params)

    if req.status_code == 200:
        timeline = json.loads(req.text)
        for tweet in timeline:
            TWITTER_STATUS_FOLLOWERS[tweet['user']['screen_name']] = tweet['user']['followers_count']
            TWITTER_STATUS_TWEETS[tweet['user']['screen_name']] =  tweet['user']['statuses_count']
            TWITTER_STATUS_FAVOURITES[tweet['user']['screen_name']] =  tweet['user']['favourites_count']
    else:
        print("ERROR: %d" % req.status_code)