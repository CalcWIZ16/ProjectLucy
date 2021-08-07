import threading
from time import time
from config import *
from speak import *

stopwatchRunning = False
timePassedSeconds = 0

def iterateStopwatch():
    global t, timePassedSeconds
    timePassedSeconds += 1
    print(timePassedSeconds)
    t = threading.Timer(1.0, lambda: iterateStopwatch())
    t.start()

def parseQuestion(string):
    global t, timePassedSeconds
    if 'start' in string:
        t = threading.Timer(1.0, lambda: iterateStopwatch())
        t.start()
    elif string.count("stop") > 1:
        t.cancel()
    elif 'long' in string:
        speakText(secondsToString())
    elif 'reset' in string:
        timePassedSeconds = 0
        t.cancel()

def secondsToString():
    global stopwatchRunning, timePassedSeconds
    print(timePassedSeconds)
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