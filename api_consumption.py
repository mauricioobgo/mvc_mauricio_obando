import os
import tweepy as tw
import pandas as pd
class api_consumption():


    def __init__(self):
        consumer_key = ''
        consumer_secret = ''
        access_token_key = ''
        access_token_secret = ''
        auth= tw.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token_key, access_token_secret)
        self.api= tw.API(auth, wait_on_rate_limit=True)


    def query_search_api(self,query_term,date_query,number_items):
        return tw.Cursor(self.api.search,q=query_term,lang='es',since=date_query).items(number_items)
        #Para probar que traiga algo [tweet.text for tweet in tweets] https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/

    def convert_into_csv_file(self):
        return 0