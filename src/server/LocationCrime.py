from pymongo import MongoClient
import json

class LocationCrime:

    def main_Method(self,year):
        client = MongoClient('localhost', 27017)
        db = client['dataDump']
        data = {}
        mainArray = []
        collection = db.get_collection("loc" + year)
        for element in collection.find():
            if not element["Longitude"] == "nan":
                coordinate = {"lng":element["Longitude"],"lat":element["Latitude"],"weight":element["Count"]}
                mainArray.append(coordinate)
        data['series'] = mainArray
        json_data = json.dumps(data)
        return json_data