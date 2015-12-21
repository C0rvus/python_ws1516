# TODO: folding comments : select Text and press CTRL + ALT + T

from pymongo import MongoClient                         # necessary to interact with MongoDB
import pandas as pd                                     # necessary for fast .csv-processing
import collections                                      # necessary for sorting dictionaries
import unicodedata                                      # necessary for converting unicode datatypes to string

client = MongoClient                                    # will be modified by connect_To_MongoDB()
mongo_DB_Chicago = MongoClient                          # will be modified by get_DB_Instance()
mongo_DB_Collections = ""                               # will be modified by get_DB_Collections()
mongo_DataSet_Row = {}                                  # will be modified by generate_DataSet_To_Be_Written_To_DB()


csv_Loaded_CSV = ""
data_Counter_Starting = 0                               # will be modified by reset_Data_Counter
data_Counter_In_Between = 0                             # will be modified by reset_Data_Counter
data_Counter_Ending = 0                                 # will be modified by reset_Data_Counter

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
	global data_Counter_In_Between                      # references the global variable to make use of it locally

	reset_Data_Counter()                                 # (re)sets initial values vor correct counting of data files

	for i in range(data_Counter_Starting, data_Counter_Ending):                                       # Iterates over all .CSV files
		data_Counter_In_Between+= 1                                                                  # This counter is necessary for writing data into the correct tables . Tables is named accorded to this var

		csv_Loaded_CSV = pd.read_csv('..\datasets\Crimes_-_' + str(i) +'.csv')
		if not any(str(data_Counter_In_Between) in s for s in mongo_DB_Collections):                 # Whenever the table already exists, skip that csv file!
			print "Crime data for year " + str(i) + "does not exist yet - generating tables now."
			process_CSV_Data()
		else:
			print "Table " + "'" + str(i) + "'" + " already exists.. Skipping the creation of that table"

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
		create_Dictionary_For_CSV_To_DB_Write()                           # Creates a "dictionary" out of the given file data
		write_CSV_Data_To_DB()                                         # Writes that actually processed / iterated row into the MongoDB



# </editor-fold>

# <editor-fold desc="MongoDB operations happen inside here">

# <editor-fold desc="Connecting to MongoDB-Server">
# Connects to the specified MongoDB-Server
# We can replace localhost with an IP-Adress, whenever the database runs somewhere else
# Alternative connect method: client = MongoClient('mongodb://localhost:27017/')
# Source: http://api.mongodb.org/python/current/tutorial.html                   @ 28.11.2015 ~ 20:15
#
# </editor-fold>
def connect_To_MongoDB():
		global client                                   # references the global variable to make use of it locally

		client = MongoClient('localhost', 27017)        # filles the global variable with corrrect values, according to the mongoDB we want to connect to

# <editor-fold desc="Retrieve the data base instance">
# The method below retrieves the correct database instace here "dataDump"
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
def create_Dictionary_For_CSV_To_DB_Write():
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
def write_CSV_Data_To_DB():
		global mongo_DataSet_Row                        # references the global variable to make use of it locally
		global mongo_DB_Chicago                         # references the global variable to make use of it locally

		table_To_Be_Written = mongo_DB_Chicago[str(data_Counter_In_Between)]            # Selects the table / collection the new line will be written into
		table_To_Be_Written.insert_one(mongo_DataSet_Row)                               # Wroites the actually processed line into that collection

# </editor-fold>

def create_Arrest_Table():
	global mongo_DB_Chicago                         # references the global variable to make use of it locally
	reset_Data_Counter()                            # Resets the CSV-Values to its initial state.. necessary for correct table writing

	# Checks whether the table / collection "arrest" already exists.. If not then create that table / collection
	if not any(str("arrest") in s for s in mongo_DB_Collections):                 # Whenever the table already exists -> do nothing

		# Iterate over every table / collection and get the amount of arrested crimes
		for i in range (data_Counter_Starting, data_Counter_Ending):

			print "Creating arrest entries for the year " + str(i)

			collection = mongo_DB_Chicago[str(i)]                                 # Gets the collection depending on the defined variable name (i.e. 2001)
			selector = collection.find({"Arrest": True})                          # Give me all entries in that table with the attribute "Arrest" = True

			# The comment down below lets pycharm ignore some "warnings" about the correct writing style of a dictionary
			# noinspection PyTypeChecker
			mongo_DataSet_Row_Arrests = dict({
				str(i): str(selector.count())                                     # cursor.count() returns the amount of entries in that cursor / selector
			})
			table_To_Be_Written = mongo_DB_Chicago["arrest"]                      # references the table into which that data will be written
			table_To_Be_Written.insert_one(mongo_DataSet_Row_Arrests)             # write it now
	else:

		print "Table 'arrest' already exists.. Skipping the creating of that table"

def create_Time_Table():
	global mongo_DB_Chicago                         # references the global variable to make use of it locally
	reset_Data_Counter()                            # Resets the CSV-Values to its initial state.. necessary for correct table writing

	# Checks whether the table / collection "time" already exists.. If not then create that table / collection
	if not any(str("time") in s for s in mongo_DB_Collections):                   # Whenever the table already exists -> do nothing

		# Iterate over every table / collection and get the amount of arrested crimes
		for i in range (data_Counter_Starting, data_Counter_Ending):
			print "Creating time entries for the year " + str(i)

			collection = mongo_DB_Chicago[str(i)]                                 # Gets the collection depending on the defined variable name (i.e. 2001)

			# noinspection PyTypeChecker
			time_Dictionary = dict({
			0: 0,	1: 0,	2: 0,	3: 0,	4: 0,	5: 0,	6: 0,	7: 0,	8: 0,	9: 0,	10: 0,	11: 0,	12: 0,	13: 0,	14: 0,	15: 0,	16: 0,	17: 0,	18: 0,	19: 0,	20: 0,	21: 0,	22: 0,	23: 0
			})
			cursor = collection.find()

			# Gibt mir alle Eintraege zurueck, die Arrest: True sind
			for document in cursor:
				date_Var = document.get("Date")                                                # only get me the table with the column "Date"
				date_Var = unicodedata.normalize('NFKD', date_Var).encode('ascii', 'ignore')  # because it is in unicode-style, we have to convert it first. [-> (i.e.) 02/26/2001 12:00:00 PM]
				# Source: https://stackoverflow.com/questions/1207457/convert-a-unicode-string-to-a-string-in-python-containing-extra-symbols

				# Splits that string into an array
				date_Var = date_Var.split()                                                   # converts it as follows: '02/26/2001 07:15:00 PM' -> ['02/26/2001', '07:15:00', 'PM']

				date_Var_Raw_Time_Hour_Array = date_Var[1].split()                            # Gets the time of that array and splits it again into an another array (i.e.) '07:15:00' -> '[07:15:00]'
				date_Var_Single_Hours = date_Var_Raw_Time_Hour_Array[0].split(":")            # Split that array anew so that (i.e.): ['07:15:10'] -> ['07' , '15' , '10']
				date_Var_12_Format = date_Var[2]                                              # Gets the AM /PM of that array

				# Whenever a crime happened between 00:00 and 00:59
				if date_Var_Single_Hours[0] == "12" and date_Var_12_Format == "AM":
					time_Dictionary[0] +=1

				# Whenever a crime happened between 01:00 and 01:59
				elif date_Var_Single_Hours[0] == "01" and date_Var_12_Format == "AM":
					time_Dictionary[1] +=1

				# Whenever a crime happened between 02:00 and 02:59
				elif date_Var_Single_Hours[0] == "02" and date_Var_12_Format == "AM":
					time_Dictionary[2] +=1

				# Whenever a crime happened between 03:00 and 03:59
				elif date_Var_Single_Hours[0] == "03" and date_Var_12_Format == "AM":
					time_Dictionary[3] +=1

				# Whenever a crime happened between 04:00 and 04:59
				elif date_Var_Single_Hours[0] == "04" and date_Var_12_Format == "AM":
					time_Dictionary[4] +=1

				# Whenever a crime happened between 05:00 and 05:59
				elif date_Var_Single_Hours[0] == "05" and date_Var_12_Format == "AM":
					time_Dictionary[5] +=1

				# Whenever a crime happened between 06:00 and 06:59
				elif date_Var_Single_Hours[0] == "06" and date_Var_12_Format == "AM":
					time_Dictionary[6] +=1

				# Whenever a crime happened between 07:00 and 07:59
				elif date_Var_Single_Hours[0] == "07" and date_Var_12_Format == "AM":
					time_Dictionary[7] +=1

				# Whenever a crime happened between 08:00 and 08:59
				elif date_Var_Single_Hours[0] == "08" and date_Var_12_Format == "AM":
					time_Dictionary[8] +=1

				# Whenever a crime happened between 09:00 and 09:59
				elif date_Var_Single_Hours[0] == "09" and date_Var_12_Format == "AM":
					time_Dictionary[9] +=1

				# Whenever a crime happened between 10:00 and 10:59
				elif date_Var_Single_Hours[0] == "10" and date_Var_12_Format == "AM":
					time_Dictionary[10] +=1

				# Whenever a crime happened between 11:00 and 11:59
				elif date_Var_Single_Hours[0] == "11" and date_Var_12_Format == "AM":
					time_Dictionary[11] +=1

				# Whenever a crime happened between 12:00 and 12:59
				elif date_Var_Single_Hours[0] == "12" and date_Var_12_Format == "PM":
					time_Dictionary[12] +=1

				# Whenever a crime happened between 13:00 and 13:59
				elif date_Var_Single_Hours[0] == "01" and date_Var_12_Format == "PM":
					time_Dictionary[13] +=1

				# Whenever a crime happened between 14:00 and 14:59
				elif date_Var_Single_Hours[0] == "02" and date_Var_12_Format == "PM":
					time_Dictionary[14] +=1

				# Whenever a crime happened between 15:00 and 15:59
				elif date_Var_Single_Hours[0] == "03" and date_Var_12_Format == "PM":
					time_Dictionary[15] +=1

				# Whenever a crime happened between 16:00 and 16:59
				elif date_Var_Single_Hours[0] == "04" and date_Var_12_Format == "PM":
					time_Dictionary[16] +=1

				# Whenever a crime happened between 17:00 and 17:59
				elif date_Var_Single_Hours[0] == "05" and date_Var_12_Format == "PM":
					time_Dictionary[17] +=1

				# Whenever a crime happened between 18:00 and 18:59
				elif date_Var_Single_Hours[0] == "06" and date_Var_12_Format == "PM":
					time_Dictionary[18] +=1

				# Whenever a crime happened between 19:00 and 19:59
				elif date_Var_Single_Hours[0] == "07" and date_Var_12_Format == "PM":
					time_Dictionary[19] +=1

				# Whenever a crime happened between 20:00 and 20:59
				elif date_Var_Single_Hours[0] == "08" and date_Var_12_Format == "PM":
					time_Dictionary[20] +=1

				# Whenever a crime happened between 21:00 and 21:59
				elif date_Var_Single_Hours[0] == "09" and date_Var_12_Format == "PM":
					time_Dictionary[21] +=1

				# Whenever a crime happened between 22:00 and 22:59
				elif date_Var_Single_Hours[0] == "10" and date_Var_12_Format == "PM":
					time_Dictionary[22] +=1

				# Whenever a crime happened between 23:00 and 23:59
				elif date_Var_Single_Hours[0] == "11" and date_Var_12_Format == "PM":
					time_Dictionary[23] +=1

			# Hier arbeiten!

			# The comment down below lets pycharm ignore some "warnings" about the correct writing style of a dictionary
			# noinspection PyTypeChecker
			mongo_DataSet_Row_Time = dict({
				"year": i,
				str(0): time_Dictionary[0],
				str(1): time_Dictionary[1],
				str(2): time_Dictionary[2],
				str(3): time_Dictionary[3],
				str(4): time_Dictionary[4],
				str(5): time_Dictionary[5],
				str(6): time_Dictionary[6],
				str(7): time_Dictionary[7],
				str(8): time_Dictionary[8],
				str(9): time_Dictionary[9],
				str(10): time_Dictionary[10],
				str(11): time_Dictionary[11],
				str(12): time_Dictionary[12],
				str(13): time_Dictionary[13],
				str(14): time_Dictionary[14],
				str(15): time_Dictionary[15],
				str(16): time_Dictionary[16],
				str(17): time_Dictionary[17],
				str(18): time_Dictionary[18],
				str(19): time_Dictionary[19],
				str(20): time_Dictionary[20],
				str(21): time_Dictionary[21],
				str(22): time_Dictionary[22],
				str(23): time_Dictionary[23]
			})

			mongo_DataSet_Row_Time = collections.OrderedDict(sorted(mongo_DataSet_Row_Time.items()))              # Sorts that dictionary alphabetically ordered

			table_To_Be_Written = mongo_DB_Chicago["time"]                     # references the table into which that data will be written
			table_To_Be_Written.insert_one(mongo_DataSet_Row_Time)             # write it now
	else:
		print "Table 'time' already exists.. Skipping the creating of that table"





def reset_Data_Counter():
	global data_Counter_Starting                             # references the global variable to make use of it locally
	global data_Counter_In_Between                           # references the global variable to make use of it locally
	global data_Counter_Ending                               # references the global variable to make use of it locally

	data_Counter_Starting = 2001                             # The starting number correspondig to our first data set        (Crimes_-_2001.csv)
	data_Counter_In_Between = 2000                           # An in between counter which is used by dynamically generating / checking tables according to processed csv data
	data_Counter_Ending = 2015                               # The ending number corresponding to our last data set          (Crimes_-_2014.csv)



connect_To_MongoDB()                                    # Connects to the mongoDB
get_DB_Instance()                                       # Gets and declares the mongoDB-Instance
get_DB_Collections()                                    # Gets all existent collections (necessary to skip unnecessary / redundant writes into mongoDB)

read_CSV_Data()                                         # Reads in those csv-Data and processes them afterwards.. This is only necessary once for the initial mongoDB build up
create_Arrest_Table()                                   # Creates an extra table, which contains the amount of all crimes which lead to an arrest.
create_Time_Table()                                     # Creates an extra Time which contains the amount of crimes during day hours