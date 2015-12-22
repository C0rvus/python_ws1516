from pymongo import MongoClient
import json
from bson.json_util import dumps

class TimeCrime:
    def main_Method(self, year):
        client = MongoClient('localhost', 27017)
        return dumps(client['dataDump'].get_collection('time').find({'year':str(year)})[0])