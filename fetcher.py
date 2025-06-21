# This code is repsonsible for fetching the tweets from the Reputable Sources, in this case the sources are :
# Fabrizio Romano, David Ornstein, Hand of Arsenal, Sami Mokbel

import tweepy

keywords = ["arsenal", "afc", "gunners"]

 # Twitter token for requests and how many posts to retrieve
BEARER_TOKEN = "your token must be here"
client = tweepy.Client(bearer_token = BEARER_TOKEN)

# Fetching the news 
def fetch_latest_news(pUsername, num_posts):
    try:
        user = client.get_user(username=pUsername)
        user_id = user.data.id
        tweets = client.get_users_tweets(id=user_id, 
                                         max_results = num_posts, 
                                         tweet_fields=["created_at"])

        if tweets and tweets.data:
            # I need to filter here for only Arsenal based Transfer News
            for tweet in tweets.data:
                tweet_content = tweet.text.lower()
                if any (keyword in tweet_content for keyword in keywords):
                    return [(tweet.created_at, tweet.text) ]
       
        return []
        
    except Exception as e:
        print(f"There was an error when fetching tweets for @{pUsername}: {e}")
        return []
