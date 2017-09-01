import json
#import config
import local_config
from requests_oauthlib import OAuth1Session


CK = local_config.CONSUMER_KEY
CS = local_config.CONSUMER_SECRET
AT = local_config.ACCESS_TOKEN
ATS = local_config.ACCESS_TOKEN_SECRET

twitter = OAuth1Session(CK, CS, AT, ATS)

url_get = "https://api.twitter.com/1.1/statuses/user_timeline.json"
url_post = "https://api.twitter.com/1.1/statuses/update.json"

for user_id_key in local_config.USER_ID:
    params ={'count' : 1,'user_id' : local_config.USER_ID[user_id_key]}
    req = twitter.get(url_get, params = params)

    if req.status_code == 200:
        timeline = json.loads(req.text)
        for tweet in timeline:
            if tweet['user']['followers_count']%1000 == 0:
                tweet = "@"+tweet['user']['screen_name']+" "+"さん"+"\r\n"+"フォロワーが"+str(tweet['user']['followers_count'])+"人を超えました!"+"\r\n"+"おめでとうございます🎉"+'\r\n'+"#つくコレ"+'\r\n'+"#つくコレ2017"+'\r\n'
                params_tweet = {"status" : tweet}
                req_post = twitter.post(url_post, params = params_tweet)
                if req_post.status_code == 200:
                    print("Succeed!")
                else:
                    print("ERROR : %d"% req.status_code)
            else:
                print("not over : {0} now {1}".format(tweet['user']['screen_name'],tweet['user']['followers_count']))

    else:
        print("ERROR: %d" % req.status_code)