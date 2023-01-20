#!/usr/bin/env python3

import sys
import asyncio
import pandas as pd

from openmeteo_py import Hourly,Daily,Options,OWmanager
from geopy.geocoders import Nominatim

""" Find the compound percent by using a simple algorithm"""

USAGE = '''
Weather

USAGE:
    {script_name} name_city

example: $chmod +x weather.py
./weather.py Kyiv

end
'''

USAGE = USAGE.strip()


#create the function which find information about location using the name of city  
def get_city_info(city):
    geolocator = Nominatim(user_agent='DecideWeatherApp')
    loca = geolocator.geocode(city.capitalize())
    position = dict()
    position['latitude'] = loca.latitude
    position['longitude'] = loca.longitude
    return position

async def weather(args):
    #no arguments provided -- print USAGE and exit with error 
    if len(args) <=1 or len(args) >=3 :
        print(USAGE)
        exit(-1)

    #print arguments and len of them to know
    print(f'Received args: {args}, {len(args)}')

    # Separate script name from other args
    script_name = args[0]
    city = args[1]

    #get the city information
    city_info = get_city_info(city)
    
    hourly = Hourly()
    daily = Daily()
    # Latitude, Longitude for city info
    latitude = city_info['latitude']
    longitude = city_info['longitude']

    #using openmeteo_py library to get information about weather
    options = Options(latitude,longitude)

    mgr = OWmanager(options,
        hourly.all(),
        daily.all())

    # Download data
    meteo = mgr.get_data()

    #Export in excel and print downloaded data
    weather_daily = dict()
    weather_daily = meteo['daily']
    ds = pd.DataFrame(data=weather_daily)
    ds = (ds.T)
    print(ds)
    print('\n')
    ds.to_excel('weather_daily.xlsx')
    weather_hourly = dict()
    weather_hourly = meteo['hourly']
    df = pd.DataFrame(data=weather_hourly)
    df = (df.T)
    print(df)
    df.to_excel('weather_hourly.xlsx')

    
if __name__ == '__main__':
    asyncio.run(weather(sys.argv))

    


