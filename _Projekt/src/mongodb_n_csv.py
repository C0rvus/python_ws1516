# TODO: folding comments : select Text and press CTRL + ALT + T

from pymongo import MongoClient                         # necessary to interact with MongoDB
import pandas as pd                                     # necessary for fast .csv-processing
import collections                                      # necessary for sorting dictionaries

client = MongoClient                                    # will be modified by connect_To_MongoDB()
mongo_DB_Chicago = MongoClient                          # will be modified by get_DB_Instance()
mongo_DB_Collections = ""                               # will be modified by get_DB_Collections()
mongo_DataSet_Row = {}                                  # will be modified by generate_DataSet_To_Be_Written_To_DB()


csv_Loaded_CSV = ""
csv_Counter_Starting = 2001                             # The starting number correspondig to our first data set        (Crimes_-_2001.csv)
csv_Counter_In_Between = 2000                           # An in between counter which is used by dynamically generating / checking tables according to processed csv data
csv_Counter_Ending = 2015                               # The ending number corresponding to our last data set          (Crimes_-_2014.csv)

# Contains all columns which are to be kept within newly generated csv data files - necessary for process_CSV_Data
csv_Columns_To_Keep = ['Date','IUCR','Primary Type','Description','Location Description','Arrest','Domestic','FBI Code','Latitude','Longitude']

csv_Actual_Row = ""                                     # Contains the actual, processed / iterated row of an csv file


# <editor-fold desc="CSV data operations happen inside here">

# <editor-fold desc="Reads CSV data">
# Source: http://pandas.pydata.org/pandas-docs/stable/api.html
# </editor-fold>
def read_CSV_Data():
	global csv_Loaded_CSV                               # references the global variable to make use of it locally
	global mongo_DB_Collections                         # references the global variable to make use of it locally
	global csv_Counter_In_Between                       # references the global variable to make use of it locally

	for i in range(csv_Counter_Starting, csv_Counter_Ending):                                       # Iterates over all .CSV files
		csv_Counter_In_Between+= 1                                                                  # This counter is necessary for writing data into the correct tables . Tables is named accorded to this var

		print "Processing crime csv data for year: " + str(i)

		csv_Loaded_CSV = pd.read_csv('..\datasets\Crimes_-_' + str(i) +'.csv')
		if not any(str(csv_Counter_In_Between) in s for s in mongo_DB_Collections):                 # Whenever the table already exists, skip that csv file!
			print "Crime data for year " + str(i) + "does not exist yet - generating tables now."
			process_CSV_Data()

# <editor-fold desc="Writes every row of the csv into mongoDB">
# Processes the csv data the following way:
# 1. It strips needed columns out of the origin csv file
# 2. It converts that stripped csv-file to a dictionarty in list format
# 3. It iterates over every row within that dictionary
#   3.1. It builds a ordered dictionary element for each row
#   3.2. This created dictionary element immediately gets written into the mongoDB
# </editor-fold>
def process_CSV_Data():
	global csv_Loaded_CSV                               # references the global variable to make use of it locally
	global csv_Columns_To_Keep                          # references the global variable to make use of it locally
	global csv_Actual_Row                               # references the global variable to make use of it locally
	global mongo_DataSet_Row                            # references the global variable to make use of it locally


	csv_Processed = csv_Loaded_CSV[csv_Columns_To_Keep]            # Reduce the read csv data to only contain the previously defined columns
	csv_Processed = csv_Processed.T.to_dict('list')                # Converts the newly defined csv-data to a list (necessary for easier post-processing)

	for key in sorted(csv_Processed):
		csv_Actual_Row = csv_Processed[key]                        # Contains the actual iterated row
		create_Dictionary_For_DB_Write()                           # Creates a "dictionary" out of the given file data
		write_Data_To_DB()                                         # Writes that actually processed / iterated row into the MongoDB


# </editor-fold>

# <editor-fold desc="MongoDB operations happen inside here">

# <editor-fold desc="Connecting to MongoDB-Server">
# Connects to the specified MongoDB-Server
# We can replace localhost with an IP-Adress, whenever the database runs somewhere else
# Alternative connect method: client = MongoClient('mongodb://localhost:27017/')
# Source: http://api.mongodb.org/python/current/tutorial.html                   @ 28.11.2015 ~ 20:15
#
#
# For connection with credentials look below:
#
# import urllib
# password = urllib.quote_plus('pass/word')                       # password needs to be entered here
# password
# MongoClient('mongodb://user:' + password + '@127.0.0.1')        # username and serveradress would be needed to be chnaged
# Source: http://api.mongodb.org/python/current/examples/authentication.html    @ 28.11.2015 ~ 21:22
#
# </editor-fold>
def connect_To_MongoDB():
        global client                                   # references the global variable to make use of it locally

        client = MongoClient('localhost', 27017)        # filles the global variable with corrrect values, according to the mongoDB we want to connect to

# <editor-fold desc="Retrieve the data base instance">
# The method below retrieves the correct database instace here "Chicago_Crime_Database"
# </editor-fold>
def get_DB_Instance():
        global mongo_DB_Chicago                         # references the global variable to make use of it locally

        mongo_DB_Chicago = client.dataDump              # refers to the crime database and creates it if non existent

# <editor-fold desc="Retrieves all collections / tables">
# Stores all mongoDB collections (tables) into mongo_DB_Collections
# </editor-fold>
def get_DB_Collections():
	global mongo_DB_Chicago                             # references the global variable to make use of it locally
	global mongo_DB_Collections                         # references the global variable to make use of it locally

	mongo_DB_Collections = mongo_DB_Chicago.collection_names()          # stores all collections / tables into that array. Necessary for csv -> mongoDB writing checking

# <editor-fold desc="Creates directory information for MongoDB">
# This method processes the actual row, to be iterated at the moment
# And builds a "directory" object out of the single informations of the row
# </editor-fold>
def create_Dictionary_For_DB_Write():
		global mongo_DataSet_Row                        # references the global variable to make use of it locally
		global csv_Actual_Row                           # references the global variable to make use of it locally


		# Builds a "dictionary" out of the information which the actually iterated row contains
		# Problem with dictionaries are, that they are unsorted.. After building that dictionary they are not in the order like below
		# So you have to adjust your database view
		# I have added the comment below so PyCharm don't "spackt around"
		# noinspection PyTypeChecker
		mongo_DataSet_Row = dict({
				csv_Columns_To_Keep[0]: csv_Actual_Row[0],
		        csv_Columns_To_Keep[1]: csv_Actual_Row[1],
		        csv_Columns_To_Keep[2]: csv_Actual_Row[2],
		        csv_Columns_To_Keep[3]: csv_Actual_Row[3],
		        csv_Columns_To_Keep[4]: csv_Actual_Row[4],
		        csv_Columns_To_Keep[5]: csv_Actual_Row[5],
		        csv_Columns_To_Keep[6]: csv_Actual_Row[6],
		        csv_Columns_To_Keep[7]: csv_Actual_Row[7],
		        csv_Columns_To_Keep[8]: csv_Actual_Row[8],
		        csv_Columns_To_Keep[9]: csv_Actual_Row[9]
		})

		# Sorts the dictionary according to the columns name (alphabetically) .. This is necessary to reduce workload on the database
		# because mongoDB does not have to hassle around by adding single values to appropriate columns then..
		# Hopefully this is MongoDB compatible everywhere, because mongoDB normally only supports dictionaries..
		mongo_DataSet_Row = collections.OrderedDict(sorted(mongo_DataSet_Row.items()))              # Contains that previously defined dictionary, with columns sorted in alphabetically order

# <editor-fold desc="Writes the modified data set into all tables of the database">
# Writes generated data into all tables
# </editor-fold>
def write_Data_To_DB():
		global mongo_DataSet_Row                        # references the global variable to make use of it locally
		global mongo_DB_Chicago                         # references the global variable to make use of it locally

		table_To_Be_Written = mongo_DB_Chicago[str(csv_Counter_In_Between)]             # Selects the table / collection the new line will be written into
		table_To_Be_Written.insert_one(mongo_DataSet_Row)                               # Wroites the actually processed line into that collection

# </editor-fold>




connect_To_MongoDB()                                    # Connects to the mongoDB
get_DB_Instance()                                       # Gets and declares the mongoDB-Instance
get_DB_Collections()                                    # Gets all existent collections (necessary to skip unnecessary / redundant writes into mongoDB)

read_CSV_Data()                                         # Reads in those csv-Data and processes them afterwards.. This is only necessary once for the initial mongoDB build up