from pymongo import MongoClient
import json
import time

client = MongoClient()
client = MongoClient('localhost', 27017)
returnString = {}

firstTimeStamp = time.time()
data = {}
mainArray = []
counter = 0
db = client['dataDump']
collection = db.get_collection('2001')
for doc in collection.find():
    subArray = [doc["Latitude"],doc["Longitude"]]
    mainArray.append(subArray)
    counter = counter +1
data['data'] = mainArray
json_data = json.dumps(data)
lastTimeStamp = time.time()
diff = lastTimeStamp - firstTimeStamp
print "Success:  " + str(diff) + " Counter:  " + str(counter)
print json_data