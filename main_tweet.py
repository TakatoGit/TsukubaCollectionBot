# -*- coding: utf-8 -*-

import json, get_date, os
import config
#import local_config as config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET


def tweet_with_image(twitter, tweet_text, path_list_images):

    url_media = "https://upload.twitter.com/1.1/media/upload.json"
    url_text = "https://api.twitter.com/1.1/statuses/update.json"
    current_directory = os.getcwd()

    media_ids = ""

    # 画像の枚数分ループ
    
    for path in path_list_images:
        files = {"media" : open(current_directory+"/graf/"+path, 'rb')}
        req_media = twitter.post(url_media, files = files)

        # レスポンスを確認
        if req_media.status_code != 200:
            print ("Image update failed: {}".format(req_media.text))
            return -1

        media_id = json.loads(req_media.text)['media_id']
        media_id_string = json.loads(req_media.text)['media_id_string']
        print ("Media ID: {} ".format(media_id))
        # メディアIDの文字列をカンマ","で結合
        if media_ids == "":
            media_ids += media_id_string
        else:
            media_ids = media_ids + "," + media_id_string

    print ("media_ids: ", media_ids)
    params = {'status': tweet_text, "media_ids": [media_ids]}
    req_text = twitter.post(url_text, params = params)

    # 再びレスポンスを確認
    if req_text.status_code != 200:
        print ("Text update failed: {}".format(req_text.text))
        return -1
    print ("tweet uploaded\n")
    return 1

def main():
    twitter = OAuth1Session(CK, CS, AT, ATS)
    tweet_str = ""
    tweet_text =  tweet_str + '\r\n' + "#つくコレ" + '\r\n' + "#つくコレ2017" + '\r\n' + "#統計"
    path_list_images = {
        'graf_tweets.png',
        'graf_followers.png',
        'graf_favourites.png',
        }
    tweet_with_image(twitter,tweet_text,path_list_images)

if __name__ == '__main__':
    main()
