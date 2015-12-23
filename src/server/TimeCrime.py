from pymongo import MongoClient
import unicodedata                                      # necessary for converting unicode datatypes to string
import collections                                      # necessary for sorting dictionaries
import json

class TimeCrime:
	def main_Method(self):
		client = MongoClient('localhost', 27017)
		db = client['dataDump']
		collection = db['time']
		selector = collection.find()
		data = {}
		returned_JSON_Data = []    # Creates the JSON-Array which is to be returned

		returned_JSON_Data_Format = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24] # Creates an list with fixed length

		for document in selector:
			#print type(document)
			document = collections.OrderedDict(sorted(document.items()))          # Contains that previously defined dictionary, with columns sorted in alphabetically order

			print type(document)

			for key, value in document.iteritems():
				# print key, value

				if not key == 'year' and not key == '_id':
					converted_Key = unicodedata.normalize('NFKD', key).encode('ascii', 'ignore')
					converted_Key = int(converted_Key)
					returned_JSON_Data_Format[converted_Key] = value
				else:
					if key == 'year':
						returned_JSON_Data_Format[24] = value
			# noinspection PyTypeChecker
			returned_JSON_Data.append({'name': returned_JSON_Data_Format[24], 'data' : returned_JSON_Data_Format[0:24]})

		data["series"] = returned_JSON_Data
		json_data = json.dumps(data)
		return json_data