# text_to_speech.py

import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Ajustar a velocidade da fala se necessário

def speak(text):
    engine.say(text)
    engine.runAndWait()
