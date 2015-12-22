from pymongo import MongoClient
import json
from bson.json_util import dumps

class TimeCrime:

    def main_Method(self, year, time):
        client = MongoClient('localhost', 27017)
        db = client['dataDump']
        print time
        print year
        collection = db.get_collection('time')
        collMain = collection.find({'year':str(year)})[0]
        return dumps(collMain)