import requests
from pprint import pprint
import os


city = input('Enter the city: ')
state = input('Is there a state or provence? If so what is the state or provence code otherwise press enter: ')
state = ",{state}" if state else ""
country = input('Enter the 2 letter country code: ')
location = f'{city}{state},{country}'

api_key=os.environ.get('WEATHER_KEY')
url = f'https://api.openweathermap.org/data/2.5/weather'
query = {'appid':api_key, 'q':location,"units":'imperial'}

data = requests.get(url,params=query).json()
temp = data['main']['temp']

print(f'The current temperature is {temp}F')
