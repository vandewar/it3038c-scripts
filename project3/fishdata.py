import requests, re
from bs4 import BeautifulSoup

#define scrapedata function to call from routes.py with parameter fishtype
def scrapedata(fishtype):

	#combine the common url start with the imported fishtype to find the url to scrape
	url = "http://aquahuna.com/collections/" + fishtype

	#use requests and beautifulsoup to pull xml data from the url
	r = requests.get(url).content
	soup = BeautifulSoup(r, "lxml")

	#isolate data within the product grid div class
	fish = soup.findAll("div", {"class":re.compile('(product grid)')})

	#declare empty string data variable to prepare for writing
	data = ""

	#find the name and price for each fish on the page, and format each entry for a row in an html table
	for f in fish:
		name = f.findAll("div", {"class":re.compile('(product__title text-center)')})
		price = f.findAll("span", {"class":re.compile('(product__price)')})
		datarow = "<tr><td>" + name[0].text + "</td><td>" + price[0].text + "</td></tr>"

		#append data string with each row of data
		data = data + datarow
	
	#access fishdata.html to write scraped data
	datatable = open("templates/fishdata.html", "w")

	#Write html text for the fishdata page, with variables for the fish type and for the table data
	message= """<html>
		<head>
			<h1>Aquahuna fish available for type {type}</h1>
		</head>
		<body>
			<table>
				<tr>
					<th>Fish</th>
					<th>Price</th>
				</tr>
			{tbl}
			</table>
		</body>
		</html>"""

	message = message.format(type = fishtype, tbl = data)

	#write to fishdata.html 
	datatable.write(message)
	datatable.close()