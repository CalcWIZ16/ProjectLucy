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
        timersToRemove = []
        for timer in timers:
            if timer.getTotalDuration() == timerDuration:
                timersToRemove.append(timer)
        if len(timersToRemove) > 1:
            speakText("There are " + str(len(timersToRemove)) + " timers with that duration")
            i = 0
            for timer in timersToRemove:
                timeRemaining = ""
                timeRemainingInt = timer.getCurrentTime()

                timeUnits = []
                if timeRemainingInt > 3600:
                    hourCount = timeRemainingInt // 3600
                    if hourCount == 1:
                        timeUnits.append(str(hourCount) + " hour")
                    else:
                        timeUnits.append(tr(hourCount) + " hours")
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
                if i == len(timersToRemove) - 1:
                    speakText("and a timer with " + response + " remaining")
                else:
                    speakText("There is a timer with " + response + " remaining")
                i += 1
            speakText("What is the index of the timer you want to remove?")
            waiting = True
            while waiting:
                timerToRemove = getUserInput()
                try:
                    timers.remove(timersToRemove[int(timerToRemove)])
                    speakText("Removed the timer")
                    waiting = False
                except:
                    speakText("There was an error, please try again")
        else:
            timers.remove(timersToRemove[0])
            speakText("Removed a " + amountOfTime + " " + unitOfTime + " timer")

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