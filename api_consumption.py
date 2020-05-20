import os
import tweepy as tw
import pandas as pd
class api_consumption():


    def __init__(self):
        consumer_key = 'SpC8t4fTuwY9JUSMP24GEqz2q'
        consumer_secret = 'fwnC15x2Ts35quo5Hc0LW1atQIlQ9jcwhTW6s6dKdor7Vrbsvq'
        access_token_key = '750495828-qZSbCVvsAgcvuz6jaNssog82B0wmgAgcS28A3Amo'
        access_token_secret = 'HCDmltDx24AMumS2DvA3UZLNTJX9HfujVI2mtApIeexS2'
        auth= tw.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token_key, access_token_secret)
        self.api= tw.API(auth, wait_on_rate_limit=True)


    def query_search_api(self,query_term,date_query,number_items):
        return tw.Cursor(self.api.search,q=query_term,lang='es',since=date_query).items(number_items)
        #Para probar que traiga algo [tweet.text for tweet in tweets] https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/

    def convert_into_csv_file(self):
        return 0