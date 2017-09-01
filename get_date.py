import status, graf_generator
from datetime import datetime

graf_generator.generate(status.TWITTER_STATUS_FOLLOWERS, "followers")
graf_generator.generate(status.TWITTER_STATUS_FAVOURITES, "favourites")
graf_generator.generate(status.TWITTER_STATUS_TWEETS, "tweets")

date = datetime.now().strftime('%m%d%H')
print(date+"success")