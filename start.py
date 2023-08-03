#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import lucy as lucy
from config import *
from lucy import parseQuestion

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
            print('4')
            if text.lower() == 'turn off':
                activated = False
                print('1')
            else:
                lucy.parseQuestion(text)
                print('2')
        except:
            print('3')
            # lucy.speakError()
    elif speech_mode=='false':
        print("Say something!")
        userIn = input()

        if userIn.lower() == 'turn off' or 'exit':
            activated = False
        else:
            lucy.parseQuestion(userIn)
            