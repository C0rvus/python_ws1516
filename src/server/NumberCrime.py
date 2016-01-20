from pymongo import MongoClient                         # necessary to interact with MongoDB
import unicodedata                                      # necessary for converting unicode datatypes to string
import collections                                      # necessary for sorting dictionaries
import json                                             # necessary for creating json objects

# __init__() method is not necessary for use - therefore we ignore that warning here
class NumberCrime:

	def main_Method(self):
		self.is_Not_Used()

		client = MongoClient('localhost', 27017)
		counter = 0
		yearArray = ['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']
		db = client['dataDump']
		for year in yearArray:
			collectionCount = db.get_collection(year).count()
			counter = counter + int(collectionCount)
		return str(counter)

	def is_Not_Used(self):                                                  # Necessary to remove 'not static' warning
			pass