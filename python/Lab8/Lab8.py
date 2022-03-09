import requests, re
from bs4 import BeautifulSoup

r = requests.get("http://aquahuna.com/collections/african-cichlids").content

soup = BeautifulSoup(r, "lxml")

fish = soup.findAll("div", {"class":re.compile('(product grid)')})
for f in fish:
	name = f.findAll("div", {"class":re.compile('(product__title text-center)')})
	price = f.findAll("span", {"class":re.compile('(product__price)')})
	print(name[0].text + price[0].text)