from pymongo import MongoClient
import json

# __init__() method is not necessary for use - therefore we ignore that warning here
class CommonCrime:

    def main_Method(self):

        self.is_Not_Used()                                                  # Removes the 'not static' warning

        client = MongoClient('localhost', 27017)                            # Connects the the local database
        db = client['dataDump']                                             # Refers to the database 'dataDump', which contains all necessary collections
        collection = db.get_collection("commonc")                           # Get that collection with the name "commonc" which contains all crime types
        data = {}
        dictlist = []

        for doc in collection.find():                                       # Iterate over every document
            minList = []
            for key, value in doc.iteritems():                              # For every key, value in each document
                if(key != "year") and (key != "_id"):
                    dictlist.append([key,value])

        crimeTypeList = []
        for crime in dictlist:
            aktCrimeElement = crime[0]
            if not any(aktCrimeElement in s for s in crimeTypeList):
                crimeTypeList.append(aktCrimeElement)


        mainArray = []
        for year in dictlist:
            yearArray = []
            for crimeType in crimeTypeList:
                yearArray.append(crimeType)
            mainArray.append(year)

        crimeMergeList = []
        for crime in crimeTypeList:
            crimeMergeList.append({"data":[],"name":crime})

        for crimeMergeElement in crimeMergeList:
            aktCrime = crimeMergeElement["name"]
            flag = False
            for crime in mainArray:
                test = crime[0]
                if(crime[0] == aktCrime):
                    flag = True
                    crimeMergeElement["data"].append(crime[1])
            if (flag == False):
                crimeMergeElement["data"].append(0)

        data["series"] = crimeMergeList
        json_data = json.dumps(data)                                        # Dumps that object to be really in json-format
        return json_data                                                    # Returns a JSON String, containing all arrest cases

    def is_Not_Used(self):                                                  # Necessary to remove 'not static' warning
        pass