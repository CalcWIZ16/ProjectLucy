import os
from playsound import playsound

import speech_recognition as sr
import lucy as lucy

from config import *

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/tts-for-messages-354f8a743220.json'

from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    name="en-US-Wavenet-F", language_code="en-US"
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type


def speakText(string):
    if speech_mode == 'true':
        if not os.path.isfile("voice/" + string + ".mp3"):
            synthesis_input = texttospeech.SynthesisInput(text=string)
            response = client.synthesize_speech(
                input=synthesis_input, voice=voice, audio_config=audio_config
            )
            # The response's audio_content is binary.
            with open("voice/" + string + ".mp3", "wb") as out:
                # Write the response to the output file.
                out.write(response.audio_content)
                print('Audio content written to file "output.mp3"')
        playsound("voice/" + string + '.mp3')
    else:
        print("<Lucy> "+string)

def speakError():
    playsound('error.mp3')

def getUserInput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    
    try:
        return r.recognize_google(audio)
    except:
        lucy.speakError()
        print("Error")
        return "Error"