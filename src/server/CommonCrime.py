from pymongo import MongoClient
import json

class CommonCrime:

    def main_Method(self):
        client = MongoClient('localhost', 27017)
        db = client['dataDump']
        collection = db.get_collection("commonc")
        data = {}
        dictlist = []
        minList = []
        for doc in collection.find():
            for key, value in doc.iteritems():
                if(key == "year"):
                        temp = [key,value]
                        minList.append(temp)
                        dictlist.append(minList)
                        minList = []
                else:
                    if(key != "_id"):
                        temp = [key,value]
                        minList.append(temp)
        crimeList = []
        for year in dictlist:
            for crime in year:
                if(crime[0] != "year"):
                    crimeListElement = {"name":crime[0],"data":[crime[1]]}
                    crimeList.append(crimeListElement)

        crimeMergeList = []
        #crimeMergeList.append(crimeList[0])
        sensorMain = False
        for crimeElement in crimeList:
            sensorMain = False
            for crimeMergeElement in crimeMergeList:
                if crimeMergeElement["name"] == crimeElement["name"]:
                    crimeMergeElement["data"].append(crimeElement["data"][0])
                    sensorMain = True
            if sensorMain is not True:
                crimeMergeList.append(crimeElement)
                
        for year in crimeMergeList:
            year['data'] = [int(x) for x in year['data']]
            year['data'].sort()

        data["series"] = crimeMergeList
        json_data = json.dumps(data)
        return json_data