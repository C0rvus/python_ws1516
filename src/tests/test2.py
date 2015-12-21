from pymongo import MongoClient
import json
import time

client = MongoClient()
client = MongoClient('localhost', 27017)
returnString = {}

data = {}
mainArray = []
db = client['dataDump']
collection = db.get_collection('2001')
for doc in collection.find():
	lat = str(doc["Latitude"])
	long = str(doc["Longitude"])
	if not (lat is "NaN"):
		if not (long is "NaN"):
			subArray = [doc["Latitude"],doc["Longitude"]]
			mainArray.append(subArray)

data['data'] = mainArray
json_data = json.dumps(data)
print json_data