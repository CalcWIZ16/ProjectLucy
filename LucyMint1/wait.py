#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import lucy as lucy
from config import *

activated = True

while activated:
    if speech_mode == 'true':
        userIn = input("Click enter to enable: ")
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio)
        except:
            lucy.speakError()
            print("Error")

        try:
            if text.lower() == 'turn off':
                activated = False
            else:
                lucy.parseQuestion(text)
        except:
            lucy.speakError()
    else:
        userIn = input("Click enter to enable: ")
        print("Say something!")
        text = input()

        if text.lower() == 'turn off':
            activated = False
        else:
            lucy.parseQuestion(text)
            
