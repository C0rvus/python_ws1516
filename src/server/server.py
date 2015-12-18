from flask import Flask
from pymongo import MongoClient
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/getData/number-of-tables", methods=['GET'])
def hello():
    return main_Method()

def main_Method():
	client = MongoClient()
	client = MongoClient('localhost', 27017)
	returnString = "{'data':["

	db = client['dataDump']
	yearArray = ['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']

	for year in yearArray:
		returnString = str(returnString) + "[" + str(year) + "," + str(db.get_collection(year).count()) + "],"
	returnString = returnString + "}"

	return returnString

if __name__ == "__main__":
    app.run(host='0.0.0.0')
