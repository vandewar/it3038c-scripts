from flask import Flask, render_template, request

#import scrapedata function from fishdata.py
from fishdata import scrapedata

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/fishdata', methods=['POST'])
def fishes():
	#call scrapedata function with the fishtype parameter from index.html
	scrapedata(request.form['fishtype'])
	return render_template("fishdata.html")