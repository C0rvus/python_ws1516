# TODO: folding comments : select Text and press CTRL + ALT + T
# TODO: automatic writing into the database needs to be done then
# TODO: Sort database

from pymongo import MongoClient                         # necessary to interact with MongoDB
import pandas as pd                                     # necessary for fast .csv-processing


csv_Loaded_CSV = ""
csv_Starting_Counter = 2001                                     # The starting number correspondig to our first data set        (Crimes_-_2001.csv)
csv_Ending_Counter = 2015                                       # The ending number corresponding to our last data set          (Crimes_-_2014.csv)
csv_Columns_To_Keep = ['Date','IUCR','Primary Type','Description','Location Description','Arrest','Domestic','District','FBI Code','Year','Latitude','Longitude']                          # Contains all columns which are to be kept within newly generated csv data files - necessary for process_CSV_Data
csv_Actual_Row = ""


client = MongoClient                                            # will be modified by connect_To_MongoDB()
mongo_DB_Chicago = MongoClient                                  # will be modified by get_DB_Instance()
mongo_DataSet_Row = {}                                          # will be modified by generate_DataSet_To_Be_Written_To_DB()


# <editor-fold desc="CSV data operations happen inside here">
# <editor-fold desc="Reads CSV data">
# Source: http://pandas.pydata.org/pandas-docs/stable/api.html
def read_CSV_Data():
	global csv_Loaded_CSV

	csv_Loaded_CSV = pd.read_csv('..\datasets\_sample_2014.csv')

	#for i in range(starting_Counter, ending_Counter):                                       # Iterates over all .CSV file
#        print str(i) + ".er Durchgang"
#        df = pd.read_csv('..\datasets\Crimes_-_' + str(i) +'.csv')
#        df_new = df[columns_To_keep]
#        df_new.to_csv('..\datasets\_MODIFIED_Crimes_-_' + str(i) +'.csv', index=False)        # Index=False ignores creation of a counting column




# </editor-fold>

def process_CSV_Data():
	global csv_Loaded_CSV
	global csv_Columns_To_Keep
	global csv_Actual_Row
	global mongo_DataSet_Row                                       # refers to the global variable


	csv_Processed = csv_Loaded_CSV[csv_Columns_To_Keep]            # Reduce the read csv data to only contain defined columns
	csv_Processed = csv_Processed.T.to_dict('list')                # Converts the newly defined csv-data to a list

	for key in sorted(csv_Processed):
		csv_Actual_Row = csv_Processed[key]                          # Contains the actual iterated row
		create_Dictionary_For_DB_Write()                            # Creates a "dictionary" out of the given file data
		write_Data_To_DB()                                          # Writes that actuallyprocessed / iterated row into the MongoDB



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
        global client                                           # refers to the global variable

        client = MongoClient('localhost', 27017)                # filles global variable with appropriate value

# <editor-fold desc="Retrieve the data base instance">
# The method below retrieves the correct database instace here "Chicago_Crime_Database"
# </editor-fold>
def get_DB_Instance():
        global mongo_DB_Chicago                                 # refers to the global variable

        mongo_DB_Chicago = client.Chicago_Crime_Database        # refers to the crime db and creates it if non existent


# <editor-fold desc="Creates directory information for MongoDB">
# This method processes the actual row, to be iterated at the moment
# And builds a "directory" object out of the single informations of the row
# </editor-fold>
def create_Dictionary_For_DB_Write():
		global mongo_DataSet_Row                                # refers to the global variable
		global csv_Actual_Row                                    # refers to the global variable

		# Builds a "dictionary" out of the information which the actually iterated row contains
		mongo_DataSet_Row = dict({csv_Columns_To_Keep[0]: csv_Actual_Row[0],
		          csv_Columns_To_Keep[1]: csv_Actual_Row[1],
		          csv_Columns_To_Keep[2]: csv_Actual_Row[2],
		          csv_Columns_To_Keep[3]: csv_Actual_Row[3],
		          csv_Columns_To_Keep[4]: csv_Actual_Row[4],
		          csv_Columns_To_Keep[5]: csv_Actual_Row[5],
		          csv_Columns_To_Keep[6]: csv_Actual_Row[6],
		          csv_Columns_To_Keep[7]: csv_Actual_Row[7],
		          csv_Columns_To_Keep[8]: csv_Actual_Row[8],
		          csv_Columns_To_Keep[9]: csv_Actual_Row[9],
		          csv_Columns_To_Keep[10]: csv_Actual_Row[10],
		          csv_Columns_To_Keep[11]: csv_Actual_Row[11]
		          })

# <editor-fold desc="Writes the modified data set into all tables of the database">
# Writes generated data into all tables
# </editor-fold>
def write_Data_To_DB():
		global mongo_DataSet_Row                                # refers to the global variable
		global mongo_DB_Chicago                                 # refers to the global variable

		# TODO: Expand this shit to write necessary data into all tables !
		chicago_2014 = mongo_DB_Chicago.chicago_2014
		chicago_2014.insert_one(mongo_DataSet_Row)

# </editor-fold>











connect_To_MongoDB()
get_DB_Instance()

read_CSV_Data()
process_CSV_Data()
