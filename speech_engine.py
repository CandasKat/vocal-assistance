from email.mime import audio
import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text



USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('espeak')

engine.setProperty('rate', 115)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')[29]
engine.setProperty('voice', voices.id)
print(voices)

#Text to speech conversion

def speak(text):
    """Utilisé pour prononcer le texte qui lui est transmis"""
    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Accueille l'utilisateur en fonction de l'heure"""
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 16):
        speak(f"Bonjour {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Bonsoir {USERNAME}")
    speak(f"Je suis {BOTNAME}. Comment puis-je vous aider?")

def take_user_input():
    """Prend l'entrée de l'utilisateur, la reconnaît à l'aide du module de reconnaissance vocale et la convertit en texte"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Écoute....')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print('Reconnaître...')
        query = r.recognize_google(audio, language='fr-FR')
        if not 'stop' in query or 'arrêt' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 22 and hour < 6:
                speak("Bonne nuit monsieur, prenez soin de vous ! Au revoir!")
            else:
                speak('Passez une bonne journée monsieur! Au revoir!')
            exit()
        
    except Exception:
        speak("Désolé, je ne pouvais pas comprendre. Pourriez-vous répéter cela, s'il vous plaît ?")
        query = 'None'
    return query

