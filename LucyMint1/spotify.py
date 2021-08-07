# play ... on spotify (as input)
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import *
from speak import *

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SP_CI, client_secret=SP_CS, redirect_uri=SP_URL, scope=SCOPE))

def parseQuestion(string):
    userIn = string.removesuffix(' on spotify')
    try:
        # SPOTIFY CONTROL
        # Pause
        if userIn == 'pause' or userIn == 'stop':
            sp.pause_playback()
        # Resume
        elif userIn == 'resume':
            sp.start_playback()
        # Next Song
        elif userIn == 'skip':
            sp.next_track()
            speakText('skipping')
        # Previous Song
        elif userIn == 'previous':
            sp.previous_track()
            speakText('previous')
        # Play Song
        elif 'play' in userIn:
            userArray = userIn.split(" ", 1)
            if len(userArray) > 1:
                print(userArray[1])
                song = userArray[1]

                response = sp.search(q=song, type="track")

                artist = response["tracks"]["items"][0]["artists"][0]["uri"]
                album = response["tracks"]["items"][0]["album"]["uri"]
                track = response["tracks"]["items"][0]["uri"]
                name = response["tracks"]["items"][0]["name"]

                speakText("Playing " + name)
                print('<Lucy> Playing "' + name + '"')

                sp.start_playback(context_uri=album , offset={"uri": track})
            else:
                sp.start_playback()

    except:
        speakError()
        print("<Lucy> Sorry, I ran into a problem")