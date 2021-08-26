from config import *
from speak import *

from datetime import datetime

def parseQuestion(string):
    # time = datetime.time()
    time = datetime.now()
    hour = time.strftime('%I')
    minute = time.strftime('%M')
    ampm = time.strftime('%p')
    date = datetime.now()
    month = date.strftime('%B')
    dateNumber = date.strftime('%d')
    year = date.strftime('%Y')
    day = date.strftime('%A')

    ending = 'th'
    if int(dateNumber)==1:
        ending = 'st'
    if int(dateNumber)==2:
        ending = 'nd'
    if int(dateNumber)==3:
        ending = 'rd'

    if 'time' in string:
        if int(minute) == 0:
            print("It is "+hour+" o'clock "+ampm)
        if int(minute) < 10:
            print("It is "+hour+':'+minute+' '+ampm)
        else:
            print("It is "+hour+':'+minute+' '+ampm)

    if 'day' in string:
        print("Today is "+day+', '+month+' '+dateNumber+ending+' '+year)

    if 'date' in string:
        print("Today is "+month+' '+dateNumber+'th '+year)
    
