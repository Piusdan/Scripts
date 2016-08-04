#! python3
# quickWeather.py - Gets weather forecast for 3
# days from openweathermap.org
import requests
import sys
import json
import pprint

# read requested location from cmd
while True:
    if len(sys.argv) < 2:
        print('usage: quickWeather.py location')
        sys.exit(0)
    else:
        location = ''.join(sys.argv[1:])
        break
# Download JSON data from OpenWeatherMap.org
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=ae474eecd850ac938674c302f29a8c6d' % (
    location)
res = requests.get(url)
res.raise_for_status()
# convert the JSON string data into a python data structure
weatherData = json.loads(res.text)
# Prints weather for today and the next day
w = weatherData['list']
print('Current weather in %s %s: ' % (location, weatherData['city']['country']))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print('Tomorrow: ')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print('Day after tomorrow')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
# pprint.pprint(weatherData)
