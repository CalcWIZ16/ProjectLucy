import speech_recognition as sr
import lucy as lucy
from config import *
from pynput.keyboard import Key, Listener

def show(key):
    if key == Key.delete:
        # Stop listener
        return False
    if key == Key.shift_r:
        getInput()
  
def getInput():
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

# Collect all event until released
with Listener(on_press = show) as listener:   
    listener.join()