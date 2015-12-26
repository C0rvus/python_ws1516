# <editor-fold desc="Pre calculated table / collection 'arrest' will be created here">
# This collection contains the amount of crimes which lead to arrest
# The method works the following way:
# 1. Global DB_Instance "mongo_DB_Chicago" will be referenced first
# 2. Now the data counter will be reset, so data can be retrieved from the correct tables later on
# 3. Checks whether that collection already exists.
#   3.1. If it already exists skip the creation of that table
#   3.2. If it does not already exist: Create the table as described in step 4
# 4. Reference the correct collection, sum up the entries of all "Arrest" entries and write it into the db, with its apropriate year
# </editor-fold>

class create_Arrest_Table:

	def __init__(self):
		print "...Initializing create_Arrest_Table..."

	def main_Method(self, mongo_DB_Chicago, mongo_DB_Collections, data_Counter_Starting, data_Counter_Ending):
		self.is_Not_Used()                              # Removes the 'not static' warning

		# Checks whether the table / collection "arrest" already exists.. If not then create that table / collection
		# This check is not an exact match, like in the "readCSV()" but it is not necessary for us, because there will be only one collection with the name 'arrest'
		if not any(str("arrest") in s for s in mongo_DB_Collections):                 # Whenever the table already exists -> do nothing

			# Iterate over every table / collection and get the amount of arrested crimes
			for i in range (data_Counter_Starting, data_Counter_Ending):

				print "Creating arrest entries for the year " + str(i)

				collection = mongo_DB_Chicago[str(i)]                                 # Gets the collection depending on the defined variable name (i.e. 2001)
				selector = collection.find({"Arrest": True})                          # Give me all entries in that table with the attribute "Arrest" = True

				# The comment down below lets pycharm ignore some "warnings" about the correct writing style of a dictionary
				# noinspection PyTypeChecker
				mongo_DataSet_Row_Arrests = dict({
					"arrests": str(selector.count()),                                 # cursor.count() returns the amount of entries in that cursor / selector
					"year": str(i)                                                    # the actual iterated year as string
				})
				table_To_Be_Written = mongo_DB_Chicago["arrest"]                      # references the table into which that data will be written
				table_To_Be_Written.insert_one(mongo_DataSet_Row_Arrests)             # write it now
		else:

			print "Table 'arrest' already exists.. Skipping the creating of that table"

	def is_Not_Used(self):                                                  # Necessary to remove 'not static' warning
		pass