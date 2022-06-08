import time
import requests
from datetime import datetime

response = requests.get('http://api.open-notify.org/iss-now.json')

response.raise_for_status()

data = response.json()

longitude = float(data['iss_position']['longitude'])
latitude = float(data['iss_position']['latitude'])

iss_position = (longitude, latitude)
#print(iss_position)

MY_LAT = -9.0125
MY_LONG = 14.7335

parameters = {
    'lat': MY_LAT, 
    'lng': MY_LONG,
    'formatted': 0,
    }

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])



time_now = datetime.now()

while True:
    if time_now.hour not in range(sunrise, sunset+1): # if it's not light outside
        if abs(MY_LAT - iss_position[1])<5:  # if ISS is within 5 degrees of my latitude
            print("Look up now!!")
            
        else:
            print("It's currently dark outside, but Iss is not in my area")
            #break
    else:
        print("It's currently light")
        #break
    time.sleep(1)
     