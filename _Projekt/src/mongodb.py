# TODO: folding comments : select Text and press CTRL + ALT + T
# TODO: implement if exist method to not always generate new .csv-files
# TODO: automatic writing into the database needs to be done then

from pymongo import MongoClient                         # necessary to interact with MongoDB
import pandas as pd                                     # necessary for fast .csv-processing






##### !! Connecting to the database is described below

# <editor-fold desc="Connecting to MongoDB-Server without credentials">
# Connects to the specified MongoDB-Server
# We can replace localhost with an IP-Adress, whenever the database runs somewhere else
# Alternative connect method: client = MongoClient('mongodb://localhost:27017/')
# Source: http://api.mongodb.org/python/current/tutorial.html                   @ 28.11.2015 ~ 20:15
# </editor-fold>
client = MongoClient('localhost', 27017)

# <editor-fold desc="Connecting to MongoDB-Server with (!) credentials">
# Here we have to code whenever we need to connect to a server with credetials.
# Source: http://api.mongodb.org/python/current/examples/authentication.html    @ 28.11.2015 ~ 21:22
#import urllib
#password = urllib.quote_plus('pass/word')                       # password needs to be entered here
#password
#MongoClient('mongodb://user:' + password + '@127.0.0.1')        # username and serveradress would be needed to be chnaged
# </editor-fold>





#### !! Writing data to the database is described below

# <editor-fold desc="Getting database instance">
# Getting database / creates it if non existent
# </editor-fold>
mongo_DB_Chicago = client.Chicago_Crime_Database

# <editor-fold desc="Creation of sample row">
# Defines a dataset / "row" which will be written into the database later on
# </editor-fold>
mongo_dataSet_Row = {
		"author": "Mike_123",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],   # Defines an array within a column
        "date": "Bin eine 111 Rasdswwadsaow",
		}

# <editor-fold desc="Writing sample row to the database - to table chicago_2014">
# Referencing the chicago_2014 database here
# Inserting the example dataset into the database into the table chicago_2014
# </editor-fold>
chicago_2014 = mongo_DB_Chicago.chicago_2014
chicago_2014.insert_one(mongo_dataSet_Row).inserted_id





#### !! Reading and converting .CSV files is described below

# <editor-fold desc="Reading and processing .CSV files">
# Reading und processing of csv-file is done here
# Every .csv-file will be read and, corresponding to the columns we want to keep, a new .csv-file will be generated
# Source: http://pandas.pydata.org/pandas-docs/stable/api.html
# </editor-fold>

starting_Counter = 2001                                                                 # The starting number correspondig to our first data set        (Crimes_-_2001.csv)
ending_Counter = 2014                                                                   # The ending number corresponding to our last data set          (Crimes_-_2014.csv)
columns_To_keep = ['Date','Block']


for i in range(starting_Counter, ending_Counter):                                       # Iterates over all .CSV file
        print str(i) + ".er Durchgang"
        df = pd.read_csv('.\datasets\Crimes_-_' + str(i) +'.csv')
        df_new = df[columns_To_keep]
        df_new.to_csv('.\datasets\_MODIFIED_Crimes_-_' + str(i) +'.csv', index=False)        # Index=False ignores creation of a counting column




# <editor-fold desc="Getting collection">
# Getting collection / "table"
# Collection is something like a table as you know it from relational databases
# Concrete: The Subfolder where all our tables lay down
# </editor-fold>
# collection = mongo_db.chicago_2014