from pymongo import MongoClient
import json

class ArrestCrime:

    def main_Method(self):
        client = MongoClient('localhost', 27017)
        db = client['dataDump']
        data = {}
        subDataObject = {}
        mainArray = []
        for doc in db.get_collection("arrest").find():
            element = {"name": doc["year"],"y" : doc["arrests"]}
            mainArray.append(element)
        subDataObject['data'] = mainArray
        subDataObject['name'] = 'Brands'
        subDataObject['colorByPoint'] = True
        data['series'] = subDataObject
        json_data = json.dumps(data)
        return json_data