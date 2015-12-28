from pymongo import MongoClient
import json

# __init__() method is not necessary for use - therefore we ignore that warning here
class ArrestCrime:

    def main_Method(self):
        self.is_Not_Used()                                                  # Removes the 'not static' warning

        client = MongoClient('localhost', 27017)                            # connects the the local database
        db = client['dataDump']                                             # refers to the database 'dataDump', which contains all necessary collections
        data = {}                                                           # data object, which will contain the "Series"-Type for correct parsing later on
        subDataObject = {}
        mainArray = []
        for doc in db.get_collection("arrest").find():                      # Iterate of every document in table 'arrest'
            element = {"name": doc["year"],"y" : doc["arrests"]}
            mainArray.append(element)                                       # Append that dictionary to the list "mainArray"
        subDataObject['data'] = mainArray
        data['series'] = subDataObject
        json_data = json.dumps(data)                                        # Dumps that object to be really in json-format
        return json_data                                                    # Returns a JSON String, containing all arrest cases

    def is_Not_Used(self):                                                  # Necessary to remove 'not static' warning
        pass