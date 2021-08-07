# import requests
import speech_recognition as sr
# import pyttsx3
import spotipy
import pyjokes
from spotipy.oauth2 import SpotifyOAuth

from config import *
from speak import *

import spotify as spotify
import timers as timers
import timeanddate as timeanddate
import stopwatch as stopwatch

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

    if 'timer' in userIn:
        timers.parseQuestion(userIn)

    if ('tell' in userIn or 'whats' in userIn) and ('time' in userIn or 'date' in userIn or 'day' in userIn):
        timeanddate.parseQuestion(userIn)

    if 'stopwatch' in userIn:
        stopwatch.parseQuestion(userIn)
