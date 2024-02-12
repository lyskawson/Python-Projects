#! /usr/bin/env python3

import json, requests, sys

if len(sys.argv) < 2:
    print('Usage: ./quickWeather.py location')

location = ' '.join(sys.argv[1:])
APPID = 'd77399d5b5a81a1da4aa6af43f716ad9'


url = url ='https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (location,
APPID)
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)





w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
