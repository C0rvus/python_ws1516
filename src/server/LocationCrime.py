from pymongo import MongoClient
import json

# __init__() method is not necessary for use - therefore we ignore that warning here
class LocationCrime:

    def main_Method(self,year):

        self.is_Not_Used()                                                  # Removes the 'not static' warning

        client = MongoClient('localhost', 27017)                            # Connects the the local database
        db = client['dataDump']                                             # Refers to the database 'dataDump', which contains all necessary collections
        data = {}                                                           # data object, which will contain the "Series"-Type for correct parsing later on
        mainArray = []
        collection = db.get_collection("loc" + str(year))

        for element in collection.find():                                   # For every element in that collection
            if not element["Longitude"] == "nan":                           # Skip the "nan" entry, whenever a coordinate pair with no coordinates is iterated over
                coordinate = {"lng":element["Longitude"],"lat":element["Latitude"],"weight":element["Count"]}
                mainArray.append(coordinate)

        data['series'] = mainArray
        json_data = json.dumps(data)                                        # Dumps that object to be really in json-format
        return json_data                                                    # Returns a JSON String, containing all arrest cases

    def is_Not_Used(self):                                                  # Necessary to remove 'not static' warning
        pass