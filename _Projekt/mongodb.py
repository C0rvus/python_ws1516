from pymongo import MongoClient


# TODO Logon to DB with credentials
# TODO folding comments : select Text and press CTRL + ALT + T
# TODO Create collection for every year

##### Connecting to the database is described below

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


#### Writing data to the database is defined here

# <editor-fold desc="Getting database instance">
# Getting database / creates it if non existent
# </editor-fold>
mongo_DB_Chicago = client.Chicago_Crime_Database

# <editor-fold desc="Creation of sample row">
# Defines a dataset / "row" which will be written into the database later on
# </editor-fold>
mongo_dataSet_Row = {
		"author": "Mike",
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


# <editor-fold desc="Getting collection">
# Getting collection / "table"
# Collection is something like a table as you know it from relational databases
# Concrete: The Subfolder where all our tables lay down
# </editor-fold>
# collection = mongo_db.chicago_2014