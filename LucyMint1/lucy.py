import requests
import speech_recognition as sr
# import pyttsx3
import spotipy
 
from speak import *

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SP_CI, client_secret=SP_CS, redirect_uri=SP_URL, scope=SCOPE))

def tts(string):
    i = 0
    speakText(string)

activated = True

while activated:
    try:
        with sr.Microphone() as source:
            # print("<Lucy> I'm Listening...")
            # audio = r.listen(source)
            # userIn = r.recognize_google(audio)
            userIn = input("I'm listening: ")
            print("<"+your_name+"> "+userIn)

            if 'hello Lucy' in userIn:
                tts("Hello "+your_name)

            # SPOTIFY CONTROL
            # Pause
            elif userIn == 'exit':
                activated = False
            elif userIn == 'pause' or userIn == 'stop':
                sp.pause_playback()
            # Resume
            elif userIn == 'resume':
                sp.start_playback()
            # Next Song
            elif userIn == 'skip':
                sp.next_track()
                tts('skipping')
            # Previous Song
            elif userIn == 'previous':
                sp.previous_track()
                tts('previous')
            # Play Song
            elif 'play' in userIn:
                userArray = userIn.split(" ")
                if len(userArray) > 1:
                    song = userIn.replace('play ', '')
                    # tts("I'm on it")
                    # print('On it!')

                    response = sp.search(q=song, type="track")

                    artist = response["tracks"]["items"][0]["artists"][0]["uri"]
                    album = response["tracks"]["items"][0]["album"]["uri"]
                    track = response["tracks"]["items"][0]["uri"]
                    name = response["tracks"]["items"][0]["name"]

                    tts("Playing " + name)
                    print('<Lucy> Playing "' + name + '"')

                    sp.start_playback(context_uri=album , offset={"uri": track})
                else:
                    sp.start_playback()

    except:
        speakError()
        print("<Lucy> Sorry, I ran into a problem")
        pass