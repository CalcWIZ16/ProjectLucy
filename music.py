from config import *
from speak import *
from pynput.keyboard import Key, Controller

keyboard = Controller()

def parseQuestion(string):
    keyboard.press(Key.media_play_pause)
    keyboard.release(Key.media_play_pause)