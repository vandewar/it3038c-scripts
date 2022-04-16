import json
import requests

r = requests.get('http://localhost:3000')

data = r.json()
i = 0

for x in data:
	name = data[i]['name']
	color = data[i]['color']
	print('Widget ' + name + ' is color ' + color)
	i = i + 1