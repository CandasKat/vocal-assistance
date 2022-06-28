from ipaddress import ip_address
from pprint import pprint
from turtle import title
import requests
import wikipedia
from decouple import config

from speech_engine import speak, take_user_input

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def search_on_wikipedia(query):
    try:
        listSearch = wikipedia.search(query)
        speak(f"Voici la résultat de recherche sur wikipedia")
        speak(f"Pour votre commodité, je l'imprime sur l'écran monsieur. Voulez-vous aller sur quelle page?")
        for i in range(len(listSearch)):
            speak(f"{i+1}  {listSearch[i]}")
            pprint(f"{i+1}  {listSearch[i]}")
        while True:
            page = take_user_input().lower()
            if page.isdigit():
                page = int(page)
                if page <= len(listSearch):
                    results = wikipedia.summary(listSearch[page],sentences=3 ,auto_suggest=False)
                    break
            else:
                speak("Veuillez me donner une chiffre !")        
        return results
    except:
        speak(f"Page id {query} does not match any pages. Try another id!")


OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")

def get_weather_report(city):
    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric&lang=fr").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

def get_random_joke():
    headers = {
        'Accept' : 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']
