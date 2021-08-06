import requests
import speech_recognition as sr
import pyttsx3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SP_CI, SP_CS, SP_URL, SCOPE, AUTH_URL, your_name


# speech engine
r = sr.Recognizer()
tts = pyttsx3.speak
engine = pyttsx3.init()

# voice
voices = engine.getProperty('voices')
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')

# spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SP_CI, client_secret=SP_CS, redirect_uri=SP_URL, scope=SCOPE))
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': SP_CI,
    'client_secret': SP_CS,
})
auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

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
        elif userIn == 'pause':
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
            song = userIn.replace('play ', '')
            tts("I'm on it")
            print('On it!')

            response = sp.search(q=song, type="track")

            artist = response["tracks"]["items"][0]["artists"][0]["uri"]
            album = response["tracks"]["items"][0]["album"]["uri"]
            track = response["tracks"]["items"][0]["uri"]
            name = response["tracks"]["items"][0]["name"]

            tts("Playing " + name)
            print('<Lucy> Playing "' + name + '"')

            sp.start_playback(context_uri=album , offset={"uri": track})

except:
    tts("Sorry, I didn't quite catch that")
    print("<Lucy> Sorry, I didn't quite catch that")
    pass
