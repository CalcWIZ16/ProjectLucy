#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import lucy as lucy

activated = True

while activated:
    userIn = input("Click enter to enable: ")
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    
    try:
        dictatedText = r.recognize_google(audio)
    except:
        lucy.speakError()
        print("Error")

    if dictatedText.lower() == 'turn off':
        activated = False
    else:
        lucy.parseQuestion(dictatedText)