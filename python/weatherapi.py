import json
import requests

print('Please input your zip code')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=2666f476ad9e89ae60508bf798273d9c' % zip)

data = r.json()

print(data['weather'][0]['description'])