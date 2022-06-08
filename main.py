import time
import requests
from datetime import datetime

def is_iss_overhead(lat, lgt):
    """
    Check if ISS is close to a given location
    """
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])
    return abs(lat - latitude)<5 and abs(lgt - longitude)<5

def is_dark_outside(lat, lng):
    """
    Check if it is dark outside
    """
    parameters = {
        'lat': lat, 
        'lng': lng,
        'formatted': 0,
        }

    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    time_now = datetime.now()
    return time_now.hour not in range(sunrise, sunset+1)


if __name__ == '__main__':

    # Cartagena(Colombia) coordinates
    MY_LAT = 10.397520
    MY_LONG = -435.463243

    while True:
        if is_dark_outside(MY_LAT, MY_LONG): 
            if is_iss_overhead(MY_LAT, MY_LONG): 
                print(str(datetime.now())+' ISS is close to you! Look up now!!') 
                print(str(datetime.now())+"*****SEND EMAIL*****")
            else:
                print(str(datetime.now())+" It's currently dark outside, but Iss is not in my area")
        else:
            print(str(datetime.now())+" It's currently light")
        time.sleep(1)
     