"""
Twitter_Scrape.py — Walmart Tweet Scraper
==========================================
Scrapes tweets matching a user-supplied hashtag using the Twitter API (Tweepy).
Extracted fields: username, description, location, following/followers count,
total tweets, retweet count, full text, hashtags, and account creation date.

Output: GFG_tweets.csv — one row per tweet, ready for SQL ingestion.

Authors: Sneha Giranje, Arundhati Pathrikar, Sahil Gothoskar
Course : DAMG 6210
"""

import pandas as pd
import tweepy


# ---------------------------------------------------------------------------
# Helper — pretty-print a single tweet to the console
# ---------------------------------------------------------------------------

def printtweetdata(n, ith_tweet):
    """Display tweet number *n* and its key fields."""
    print()
    print(f"Tweet {n}:")
    print(f"Username:{ith_tweet[0]}")
    print(f"Description:{ith_tweet[1]}")
    print(f"Location:{ith_tweet[2]}")
    print(f"Following Count:{ith_tweet[3]}")
    print(f"Follower Count:{ith_tweet[4]}")
    print(f"Total Tweets:{ith_tweet[5]}")
    print(f"Retweet Count:{ith_tweet[6]}")
    print(f"Tweet Text:{ith_tweet[7]}")
    print(f"Hashtags Used:{ith_tweet[8]}")
    print(f"Created At:{ith_tweet[9]}")


# ---------------------------------------------------------------------------
# Core — search Twitter and collect tweets into a DataFrame
# ---------------------------------------------------------------------------

def scrape(words, date_since, numtweet):
    """
    Search for *numtweet* tweets matching *words* since *date_since*.

    Each tweet's metadata is appended to a DataFrame and exported to
    GFG_tweets.csv at the end.
    """
    # DataFrame to accumulate extracted tweet data
    db = pd.DataFrame(columns=[
        'username', 'description', 'location', 'following',
        'followers', 'totaltweets', 'retweetcount', 'text',
        'hashtags', 'createdat',
    ])

    # Use Tweepy Cursor to paginate through search results
    tweets = tweepy.Cursor(
        api.search_tweets,
        words,
        lang="en",
        since_id=date_since,
        tweet_mode='extended',
    ).items(numtweet)

    list_tweets = [tweet for tweet in tweets]

    # Iterate and extract relevant fields from each tweet
    i = 1
    for tweet in list_tweets:
        username     = tweet.user.screen_name
        description  = tweet.user.description
        location     = tweet.user.location
        following    = tweet.user.friends_count
        followers    = tweet.user.followers_count
        totaltweets  = tweet.user.statuses_count
        retweetcount = tweet.retweet_count
        hashtags     = tweet.entities['hashtags']
        createdat    = tweet.user.created_at

        # Retweets expose full text via retweeted_status;
        # fall back to the tweet's own full_text otherwise
        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text

        # Flatten hashtag dicts into a plain list of strings
        hashtext = [hashtags[j]['text'] for j in range(len(hashtags))]

        # Append to DataFrame and print to console
        ith_tweet = [
            username, description, location, following, followers,
            totaltweets, retweetcount, text, hashtext, createdat,
        ]
        db.loc[len(db)] = ith_tweet
        printtweetdata(i, ith_tweet)
        i += 1

    # Export all scraped tweets to CSV
    filename = 'GFG_tweets.csv'
    db.to_csv(filename)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == '__main__':

    # Twitter API credentials (replace with your own)
    consumer_key    = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    access_key      = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    access_secret   = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    # Authenticate with the Twitter API via OAuth 1.0a
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # Prompt user for search parameters
    print("Enter Twitter HashTag to search for")
    words = input()
    print("Enter Date since The Tweets are required in yyyy-mm--dd")
    date_since = input()

    # Number of tweets to extract per run
    numtweet = 100
    scrape(words, date_since, numtweet)
    print('Scraping has completed!')
