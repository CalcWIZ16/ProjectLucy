import speech_recognition as sr
import lucymain as lucy
from config import *

active = True

while active:
    if speech_mode == 'true':
        userIn = input("Click enter to enable: ")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("I'm listening...")
            audio = r.listen(source)

        try: