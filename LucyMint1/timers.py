import threading
import re
from config import *
from speak import *

import sched, time

s = sched.scheduler(time.time, time.sleep)

timers = []

unitsOfTime = ["seconds", "second", "minutes", "minute", "hours", "hour"]

class Timer():
    totalTime = None
    currentTime = None
    timeUnit = None
    timeAmount = None

    def __init__(self, totalTimeInSeconds, timeUnit, timeAmount):
        self.totalTime = totalTimeInSeconds
        self.currentTime = totalTimeInSeconds
        self.timeUnit = timeUnit
        self.timeAmount = timeAmount
    
    def removeSecond(self):
        self.currentTime -= 1
    
    def getCurrentTime(self):
        return self.currentTime

    def getTotalDuration(self):
        return self.totalTime

    def getTotalDurationString(self):
        return self.timeAmount + " " + self.timeUnit

def parseQuestion(string):
    if 'create' in string:
        sentanceArray = re.split(" |-", string)
        unitOfTime = ""
        amountOfTime = ""
        i = 0
        for string in sentanceArray:
            if string in unitsOfTime:
                unitOfTime = string
                amountOfTime = sentanceArray[i - 1]
            i += 1
        multiplier = 0
        if 'second' in unitOfTime:
            multiplier = 1
        elif 'minute' in unitOfTime:
            multiplier = 60
        elif 'hour' in unitOfTime:
            multiplier = 3600
        print(unitOfTime + " | " + amountOfTime)
        timer = Timer(int(amountOfTime) * multiplier, unitOfTime, amountOfTime)
        timers.append(timer)
        speakText("Added a " + amountOfTime + " " + unitOfTime + " timer")
        if len(timers) == 1:
            threading.Timer(1.0, iterateTimers).start()

    if 'remove' in string or 'stop' in string:
        sentanceArray = re.split(" |-", string)
        unitOfTime = ""
        amountOfTime = ""
        i = 0
        for string in sentanceArray:
            if string in unitsOfTime:
                unitOfTime = string
                amountOfTime = sentanceArray[i - 1]
            i += 1
        multiplier = 0
        if 'second' in unitOfTime:
            multiplier = 1
        elif 'minute' in unitOfTime:
            multiplier = 60
        elif 'hour' in unitOfTime:
            multiplier = 3600
        timerDuration = int(amountOfTime) * multiplier
        for timer in timers:
            if timer.getTotalDuration() == timerDuration:
                timers.remove(timer)
        speakText("Removed a " + amountOfTime + " " + unitOfTime + " timers")

def iterateTimers():
    timersToRemove = []
    for timer in timers:
        timer.removeSecond()
        if timer.getCurrentTime() < 0:
            print("removed timer")
            speakText("ring. The " + timer.getTotalDurationString() + " timer is")
            timersToRemove.append(timer)
    for timer in timersToRemove:
        timers.remove(timer)

    if len(timers) > 0:
        threading.Timer(1.0, iterateTimers).start()
    

iterateTimers()