# TODO: folding comments : select Text and press CTRL + ALT + T
# TODO: implement if exist method to not always generate new .csv-files
# TODO: automatic writing into the database needs to be done then

from pymongo import MongoClient                         # necessary to interact with MongoDB
import pandas as pd                                     # necessary for fast .csv-processing

csv_Starting_Counter = 2001                                     # The starting number correspondig to our first data set        (Crimes_-_2001.csv)
csv_Ending_Counter = 2015                                       # The ending number corresponding to our last data set          (Crimes_-_2014.csv)
csv_Columns_To_Keep = ['Date','Block']                          # Contains all columns which are to be kept within newly generated csv data files

client = MongoClient                                            # will be modified by connect_To_MongoDB()
mongo_DB_Chicago = MongoClient                                  # will be modified by get_DB_Instance()
mongo_dataSet_Row = {}                                          # will be modified by generate_DataSet_To_Be_Written_To_DB()


# <editor-fold desc="CSV data operations happen inside here">
print "Sackl picka!"
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

# <editor-fold desc="Generates data rows which will be written in to the referenced data base (Chicago_Crime_Database">
# Generates a Dataset which will be Written into the, previously referenced, data base instace
# Which is here Chicago_Crime_Data_Base
# TODO: Depending on tables the tablename (i.E. chicago_2014) needs to change!
# </editor-fold>
def generate_DataSet_To_Be_Written_To_DB():
        global mongo_dataSet_Row                                # refers to the global variable

        mongo_dataSet_Row = {
		"author": "Test_DB",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],   # Defines an array within a column
        "date": "Bin eine 111 Rasdswwadsaow",
		}

# <editor-fold desc="Writes the modified data set into all tables of the database">
# Writes generated data into all tables
# </editor-fold>
def write_Data_To_DB():
        global mongo_dataSet_Row                                # refers to the global variable
        global mongo_DB_Chicago                                 # refers to the global variable

        # TODO: Expand this shit to write necessary data into all tables !
        chicago_2014 = mongo_DB_Chicago.chicago_2014
        chicago_2014.insert_one(mongo_dataSet_Row)

# </editor-fold>




#### !! Reading and converting .CSV files is described below

# <editor-fold desc="Reading and processing .CSV files">
# Reading und processing of csv-file is done here
# Every .csv-file will be read and, corresponding to the columns we want to keep, a new .csv-file will be generated
# Source: http://pandas.pydata.org/pandas-docs/stable/api.html
# </editor-fold>




#for i in range(starting_Counter, ending_Counter):                                       # Iterates over all .CSV file
#        print str(i) + ".er Durchgang"
#        df = pd.read_csv('..\datasets\Crimes_-_' + str(i) +'.csv')
#        df_new = df[columns_To_keep]
#        df_new.to_csv('..\datasets\_MODIFIED_Crimes_-_' + str(i) +'.csv', index=False)        # Index=False ignores creation of a counting column



connect_To_MongoDB()
get_DB_Instance()
generate_DataSet_To_Be_Written_To_DB()
write_Data_To_DB()