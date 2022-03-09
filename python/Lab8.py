import requests, re
from bs4 import BeautifulSoup

r = requests.get("http://aquahuna.com/collections/african-cichlids").content

soup = BeautifulSoup(r, "lxml")

#fish = soup.findAll("div", {"class":re.compile('(product__title text-center)')})
#price = soup.findAll("div", {"class":re.compile('(product__prices text-center)')})
#for f in fish:
#	n = f.findAll("a")
#	print(n[0].text)
#for p in price:
#	d = p.findAll("span", {"class":re.compile('(product__price)')})
#	print(d[0].text)



fish = soup.findAll("div", {"class":re.compile('(product grid)')})
for f in fish:
	name = f.findAll("div", {"class":re.compile('(product__title text-center)')})
	price = f.findAll("span", {"class":re.compile('(product__price)')})
	print(name[0].text + price[0].text)