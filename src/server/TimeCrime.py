from pymongo import MongoClient                         # necessary to interact with MongoDB
import unicodedata                                      # necessary for converting unicode datatypes to string
import collections                                      # necessary for sorting dictionaries
import json                                             # necessary for creating json objects

class TimeCrime:
	def main_Method(self):
		client = MongoClient('localhost', 27017)        # connects to the locally connected
		db = client['dataDump']                         # gets the dataDump-Database instance
		collection = db['time']                         # gets the "time" collection
		selector = collection.find()                    # gets the content of the "time" collection
		data = {}                                       # data object, which will contain the "Series"-Type for correct parsing later on

		returned_JSON_Data = []                         # Creates the JSON-Array which is to be returned
		returned_JSON_Data_Format = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24] # Creates an list with fixed length

		# Iterates over every document in the colletion "time"
		for document in selector:
			document = collections.OrderedDict(sorted(document.items()))          # Contains that previously defined dictionary, with columns sorted in alphabetically order

			# Iterates over every subdocument and assigns its values to returned_JSON_Data_Format
			for key, value in document.iteritems():

				# To prevent assignment errors key "_id" will be skipped, and key "year" gets a special treatment
				if not key == 'year' and not key == '_id':
					converted_Key = unicodedata.normalize('NFKD', key).encode('ascii', 'ignore')        # Converts the object from unicode to string
					converted_Key = int(converted_Key)                            # Converts the string into integer, for correct key assignment
					returned_JSON_Data_Format[converted_Key] = value              # Assigns the value to the list container
				else:
					if key == 'year':
						returned_JSON_Data_Format[24] = value

			# noinspection PyTypeChecker
			returned_JSON_Data.append({'name': returned_JSON_Data_Format[24], 'data' : returned_JSON_Data_Format[0:24]})    # Append that object as JSON-Style to its array

		data["series"] = returned_JSON_Data                                       # Adds "series" type on top of JSON object for better recognition
		json_data = json.dumps(data)                                              # Dump that JSON object into an JSON object, so REST eats it.
		return json_data