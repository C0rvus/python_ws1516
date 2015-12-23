from pymongo import MongoClient
import json

class ArrestCrime:

    def main_Method(self):
        client = MongoClient('localhost', 27017)
        db = client['dataDump']
        data = {}
        mainArray = []
        for doc in db.get_collection("arrest").find():
            if mainArray == []:
                element = {"name": doc["year"],"y" : doc["arrests"], "sliced": "true", "selected": "true"}
            else: element = {"name": doc["year"],"y" : doc["arrests"]}
            mainArray.append(element)
        data['series'] = mainArray
        json_data = json.dumps(data)
        return json_data