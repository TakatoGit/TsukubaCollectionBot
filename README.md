# つくコレさんBot
---
つくばコレクション2017の候補者のツイッターデータを処理してツイートするBot  
アカウント [@tc_statistics](https://twitter.com/tc_statistics?s=09)

---
### ・status
Twitter REST APIでフォロワー数・ツイート数・お気に入り数を取得

### ・graf_generator
データの追加・グラフの線画＋保存

### ・get_date
データの更新

### ・main_tweet
生成されたグラフ画像をツイートする


## How to use
###  Set up auth
edit `config.py`
```
CONSUMER_KEY = "****************************"
CONSUMER_SECRET = "****************************"
ACCESS_TOKEN = "****************************"
ACCESS_TOKEN_SECRET = "****************************"
```