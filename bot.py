#!/usr/bin/env python
import random

import tweepy
import time

##########################################################################################
CONSUMER_KEY = "6mSyB2uW4IwKz5CjAjjL9WQwj"  #
CONSUMER_SECRET = "Si1qhCgYHmWoumgarYqwDXziwxgntOKmfmeOSCCdEg4YRk77fN"  #
ACCESS_TOKEN = "1467936284190535688-w93m4ODXI0ReUixLG6cC1cX3YC1fkI"  #
ACCESS_TOKEN_SECRET = "xiSjPFMZVi3wF69MnLXIa9bor4J6jUWxP4JG3WdusSNPB"  #
HASHTAG = "#crypto"  #
NUMBER_OF_TWEETS_TO_REPLY = 5  #
TWEETS_TYPE = "recent"  # can be set to "mixed" or "popular" as well                       #
BTOKEN = "AAAAAAAAAAAAAAAAAAAAAEP0cwEAAAAAd7l5gMyD4qLRlNkV3LCWvRLARI4%3DeB0hj2vejcLKoYu7XmJDsbn0ADKI2tfHqSoqalhbfFlraSuN3D"
CLIENTID = "R1FjSXo5WDFEaEFPcEl6SEF3c3o6MTpjaQ"
CLIENTSECRET = "ICWvxJ1hUrSholq_MkMnzeO8TXVz27TfmoZjCXSMl4vSjS0bHK"
##########################################################################################
tweetList = ["Yea crypto is crazy! Have you seen this new website? https://seedphisher.com/ I saw people talking about "
             "it on reddit. Seems sort of unethical idk.",
             "That is so cool! I love this new website! https://seedphisher.com/",
             "Its crazy that so much has happened in the crypto world. I saw people talking about "
             "https://seedphisher.com/ and it just makes me wonder how safe it truly is.",
             "I wonder how secure this kind of thing actually is. I saw people talking about https://seedphisher.com/ "
             "It seems kind of worrying.",
             "Its amazing what people can do with crypto. But it makes me nervous. I saw people talking about "
             "https://seedphisher.com/ and it makes me worried about how safe my assets really are."]


def bot_login():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api


def tweet_search():
    return bot_login().search_tweets(HASHTAG)


print(tweet_search())


def main():
    client = tweepy.Client(bearer_token=BTOKEN, consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                           access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
    api = bot_login()
    tweets = tweet_search()
    i = 0

    # Run for 4 hours then sleep for 2 hours


    while 1 > 0:
        for tweet in tweets:
            if tweet.user.screen_name not in open("tweets.txt").read():
                client.create_tweet(in_reply_to_tweet_id=tweets[i].id, text=tweetList[random.randint(0, 4)])
                print("Tweeted reply to: " + tweet.user.screen_name)
                with open("tweets.txt", "a") as f:
                    f.write(tweet.user.screen_name + "\n")
                i += 1
                time.sleep(60 * 15)
                if i > 16:
                    i = 0
                    time.sleep(60 * 60 * 2)
                    tweets = tweet_search()
                    print("Sleeping for 2 hours")




if __name__ == "__main__":
    main()
