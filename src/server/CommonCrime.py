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
        yearArray = ['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']
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


        data["series"] = crimeList
        print data
        json_data = json.dumps(data)
        return json_data


