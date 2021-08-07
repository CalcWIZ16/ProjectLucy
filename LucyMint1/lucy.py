# import requests
import speech_recognition as sr
# import pyttsx3
import spotipy
import pyjokes
from spotipy.oauth2 import SpotifyOAuth

from config import *
from speak import *

import spotify as spotify

def tts(string):
    i = 0
    speakText(string)

def parseQuestion(string):
    userIn = string.lower()
    print("<"+your_name+"> "+userIn)

    #Gimmics
    if 'hello' in userIn:
        tts("Hello "+your_name)

    if 'tell' in userIn and 'joke' in userIn:
        tts(pyjokes.get_joke())

    if 'on spotify' in userIn:
        spotify.parseQuestion(userIn)
