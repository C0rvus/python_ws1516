import unicodedata                                      # necessary for converting unicode datatypes to string
import collections                                      # necessary for sorting dictionaries

# <editor-fold desc="Pre calculated table / collection 'commonc' will be created here">
# Creates the pre calculated table which contains all crime types with its number of appearance for every year
# The method works the following way:
# 1. Global DB_Instance "mongo_DB_Chicago" will be referenced first
# 2. Now the data counter will be reset, so data can be retrieved from the correct tables later on
# 3. Checks whether that collection already exists.
#   3.1. If it already exists skip the creation of that table
#   3.2. If it does not already exist: Create the table as described in step 4
# 4. Get that collection for the current year and filter it by only selecting the "primary type" column and convert it from unicode into string
# 5. Now check whether that "crime type" already exists in "types_array".
#   5.1. If not, then create that entry in "types_Array" on that specific index and raise the amount and create the number 1 in "types_Array_Count"
#   5.2. If yes, simply increase the counter in "types_Array_Count"
# </editor-fold>
class create_Common_Crime_Table:

	def __init__(self):
		print "...Initializing create_Common_Crime_Table..."

	def main_Method(self, mongo_DB_Chicago, mongo_DB_Collections, data_Counter_Starting, data_Counter_Ending):
		self.is_Not_Used()                              # Removes the 'not static' warning

		# Checks whether the table / collection "commonc" already exists.. If not then create that table / collection
		if not any(str("commonc") in s for s in mongo_DB_Collections):                   # Whenever the table already exists -> do nothing

			# Iterate over every table / collection and get the amount of arrested crimes
			for i in range (data_Counter_Starting, data_Counter_Ending):

				print "Creating comonc entries for the year " + str(i)
				collection = mongo_DB_Chicago[str(i)]                                             # Gets the collection depending on the defined variable name (i.e. 2001)
				selector = collection.find()                                                      # Give me all entries in that table

				types_Array = []                                                                  # The various crime types are defined here
				types_Array_Count = []                                                            # The amount of crimes is defined here
				types_Dict_Style = dict({})                                                       # The final dictionary which will be written into the database later on
				for document in selector:
					type_Var = document.get("Primary Type")                                       # only get me the table with the column "Primary Type"
					type_Var = unicodedata.normalize('NFKD', type_Var).encode('ascii', 'ignore')  # because it is in unicode-style, we have to convert it first.

					# Source: https://stackoverflow.com/questions/7571635/fastest-way-to-check-if-a-value-exist-in-a-list

					# This is a faster index checker than usual..
					try:
						b=types_Array.index(type_Var)

					# If the crime type does not yet exist in the list
					except ValueError:
						types_Array.extend([type_Var])          # adds that type into the list
						types_Array_Count.extend([1])           # adds a counter into the count list

					# If crime type does already exist
					else:
						# raise counter by one, depending on index
						types_Array_Count[types_Array.index(type_Var)] +=1

				# Builds the dictionary here, which will be added into the database table later on
				for j in range (0, len(types_Array)):
					temp_Var = {types_Array[j]: types_Array_Count[j]}
					types_Dict_Style.update(temp_Var)
				# Add that year into the dictionary, after iterating
				temp_Year = {"year": i}
				types_Dict_Style.update(temp_Year)

				types_Dict_Style = collections.OrderedDict(sorted(types_Dict_Style.items()))              # Contains that previously defined dictionary, with columns sorted in alphabetically order

				table_To_Be_Written = mongo_DB_Chicago["commonc"]                                         # references the table into which that data will be written
				table_To_Be_Written.insert_one(types_Dict_Style)                                          # Write that dictionary into the database now

		else:
			print "Table 'commonc' already exists.. Skipping the creation of that table"

	def is_Not_Used(self):                                                          # Necessary to remove 'not static' warning
		pass