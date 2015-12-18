from flask import Flask
from pymongo import MongoClient
from flask.ext.cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/getData/number-of-tables", methods=['GET'])
def hello():
    return main_Method()

def main_Method():
	client = MongoClient()
	client = MongoClient('localhost', 27017)
	returnString = {}

	db = client['dataDump']
	yearArray = ['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']

    data = {}
    mainArray = []

	for year in yearArray:
        subData = {}
        subData['data'] = [db.get_collection(year).count()]
        subData['name'] = str(year)
        mainArray.append(subData)

    data['series'] = mainArray
    json_data = json.dumps(data)
	return json_data

if __name__ == "__main__":
    app.run(host='0.0.0.0')
