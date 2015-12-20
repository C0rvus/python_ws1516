from pymongo import MongoClient
import time

client = MongoClient()
client = MongoClient('localhost', 27017)

counter = 0
yearArray = ['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']
db = client['dataDump']

firstTimeStamp = time.time()

for year in yearArray:
    collection = db.get_collection(year)
    for doc in collection.find():
        counter = counter + 1

lastTimeStamp = time.time()
delay = lastTimeStamp - firstTimeStamp
print "Counter:  "  + counter + "; TimeDelay:  " + delay