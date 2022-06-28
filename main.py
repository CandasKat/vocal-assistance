from ipaddress import ip_address
import requests
from functions.online_ops import find_my_ip, get_random_advice, get_random_joke, get_weather_report, search_on_wikipedia
from functions.os_ops import light_led
from pprint import pprint
from speech_engine import greet_user, speak, take_user_input

if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()
        
        if 'ip address' in query:
            ip_address = find_my_ip()
            speak(f"Votre Adresse IP est {ip_address}.\nPour votre commodité, je l'imprime sur l'écran monsieur.")
            print(f"Votre Adresse IP est {ip_address}")
        
        elif 'wikipédia' in query:
            speak("Que voulez-vous rechercher sur Wikipédia, monsieur ?")
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"Selon Wikipédia, {results}")
            speak(f"Pour votre commodité, je l'imprime sur l'écran monsieur.")
            print(results)

        elif 'joke' in query:
            speak(f"J'espère que vous aimez celui-ci monsieur")
            joke = get_random_joke()
            speak(joke)
            speak("Pour votre commodité, je l'imprime sur l'écran monsieur.")
            pprint(joke)

        elif 'advice' in query:
            speak(f"Voici un conseil pour vous, monsieur.")
            advice = get_random_advice()
            speak(advice)
            speak("Pour votre commodité, je l'imprime sur l'écran monsieur.")
            pprint(advice)

        elif 'température' in query:
            speak("Vous voulez connaître la température de quelle ville ?")
            city = take_user_input().lower()
            temperature = get_weather_report(city)
            speak(temperature)
            speak("Pour votre commodité, je l'imprime sur l'écran monsieur.")
            pprint(temperature)

        elif 'led' in query:
            speak("Vous voulez que je fasse quoi monsieur?")
            led = take_user_input().lower()
            if led == "allumer" :
                light_led(led)
            elif led == "éteindre" :
                light_led(led)
            else :
                speak("Désolé, je n'ai pas compris monsieur.")