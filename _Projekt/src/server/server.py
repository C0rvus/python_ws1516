import numpy as np
from pymongo import MongoClient
from flask import Flask
app = Flask(__name__)

@app.route('/getData/number-of-tables')
def hello_world():
    return mainMethod()

if __name__ == '__main__':
    app.run(host='0.0.0.0')

def mainMethod():
	client = MongoClient()
	client = MongoClient('localhost', 27017)
	returnString = "{data:["

	db = client['dataDump']
	yearArray = ['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']

	for year in yearArray:
    	returnString = str(returnString) + "[" + str(year) + "," + str(db.get_collection(year).count()) + "]"
	returnString = returnString + "]}"

	return returnString