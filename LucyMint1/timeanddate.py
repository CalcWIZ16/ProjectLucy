from config import *
from speak import *

from geopy.geocoders import Nominatim
from geopy.geocoders import get_geocoder_for_service
get_geocoder_for_service("nominatim")

def get_timezone(location):

    # g=Nominatim()
    # place, (lat, lng) = g.geocode('New York')
    # print(place)

    # print('working')
    # print(location)

    # gc = self.gmclient().geocode(address)
    # loc = gc[0]['geometry']['location']
    # result = self.gmclient().timezone(location=loc)
    # return result 

def parseQuestion(string):

    # input='new york'
    # get_timezone(input)

    # timezone = pytz.timezone('Asia/Kolkata')

    # timeAndDate = datetime.now(timezone)

    # timeandDate.strftime('%Y:%m:%d %H:%M:%S %Z %z')

    # ending = 'th'
    # if int(dateNumber)==1:
    #     ending = 'st'
    # if int(dateNumber)==2:
    #     ending = 'nd'
    # if int(dateNumber)==3:
    #     ending = 'rd'

    # if 'time' in string:
    #     if int(minute) == 0:
    #         speakText("It is "+hour+" o'clock "+ampm)
    #     if int(minute) < 10:
    #         speakText("It is "+hour+':'+minute+' '+ampm)
    #     else:
    #         speakText("It is "+hour+':'+minute+' '+ampm)

    # if 'day' in string:
    #     speakText("Today is "+day+', '+month+' '+dateNumber+ending+' '+year)

    # if 'date' in string:
    #     speakText("Today is "+month+' '+dateNumber+'th '+year)
    
