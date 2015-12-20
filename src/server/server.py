from flask import Flaskfrom pymongo import MongoClientfrom flask.ext.cors import CORSimport jsonapp = Flask(__name__)CORS(app)@app.route("/getData/number-of-tables", methods=['GET'])def numberOverview():    return main_Method()@app.route("/getData/year/2001", methods=['GET'])def getDataYear():    return yearData()def yearData():	client = MongoClient()	client = MongoClient('localhost', 27017)	returnString = {}	firstTimeStamp = time.time()	data = {}	mainArray = []	counter = 0	db = client['dataDump']	collection = db.get_collection('2001')	for doc in collection.find():		subArray = [doc["Latitude"],doc["Longitude"]]		mainArray.append(subArray)		counter = counter +1	data['data'] = mainArray	json_data = json.dumps(data)	lastTimeStamp = time.time()	diff = lastTimeStamp - firstTimeStamp	return json_datadef main_Method():	client = MongoClient()	client = MongoClient('localhost', 27017)	returnString = {}	db = client['dataDump']	yearArray = ['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']	data = {}	mainArray = []	for year in yearArray:		subData = {}		subData['data'] = [db.get_collection(year).count()]		subData['name'] = str(year)		mainArray.append(subData)	data['series'] = mainArray	json_data = json.dumps(data)	return json_dataif __name__ == "__main__":    app.run(host="0.0.0.0")