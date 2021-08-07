import threading
import re
from config import *
from speak import *

stopwatchRunning = False

timePassedSeconds = 0

def iterateStopwatch():
    if stopwatchRunning == True:
        global timePassedSeconds
        timePassedSeconds += 1
        threading.Timer(1.0, iterateStopwatch).start()

def parseQuestion(string):
    if 'start' in string:
        stopwatchRunning = True
        iterateStopwatch()
    if 'stop' in string:
        stopwatchRunning = False
    if 'long' in string:
        speakText(secondsToString())
    if 'reset' in string:
        timePassedSeconds = 0
        stopwatchRunning = False

def secondsToString():
    timeRemainingInt = timePassedSeconds
    timeUnits = []
    if timeRemainingInt > 3600:
        hourCount = timeRemainingInt // 3600
        if hourCount == 1:
            timeUnits.append(str(hourCount) + " hour")
        else:
            timeUnits.append(str(hourCount) + " hours")
        timeRemainingInt = timeRemainingInt % 3600
    if timeRemainingInt > 60:
        minuteCount = timeRemainingInt // 60
        if minuteCount == 1:
            timeUnits.append(str(minuteCount) + " minute")
        else:
            timeUnits.append(str(minuteCount) + " minutes")
        secondCount = timeRemainingInt % 60
        if secondCount == 1:
            timeUnits.append(str(secondCount) + " second")
        else:
            timeUnits.append(str(secondCount) + " seconds")
    # timeUnits = (value for value in timeUnits if value != "")
    if "" in timeUnits:
        timeUnits.remove("")
    response = ""
    if len(timeUnits) == 1:
        response = timeUnits[0]
    elif len(timeUnits) == 2:
        response = timeUnits[0] + " and " + timeUnits[1]
    elif len(timeUnits) == 3:
        response = timeUnits[0] + " " + timeUnits[1] + " and " + timeUnits[2]
    return "The stopwatch has been running for " + response