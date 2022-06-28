from unittest import result
from flask import redirect
import requests
from soupsieve import Iterable
import wikipedia
from decouple import config
import http.client, urllib.parse
from newscatcherapi import NewsCatcherApiClient

NEWS_API_KEY = config("NEWS_API_KEY")
def get_latest_news():
    news = NewsCatcherApiClient(x_api_key=NEWS_API_KEY)
    all_articles = news.get_latest_headlines(lang='fr', countries='ch',topic="politics", ranked_only=False)
    return (x["title"] for x in all_articles["articles"])
    
print(get_latest_news())