import collections                                      # necessary for sorting dictionaries

# <editor-fold desc="Pre calculated table / collection 'locXY' will be created here">
# Creates initial tables for usage of heatmap on our website.
# To radically increase its speed the coordinates will be pre calculated in that to table and rounded to three digits after the comma
# The method works the following way:
# 1. Global DB_Instance "mongo_DB_Chicago" will be referenced first
# 2. Now the data counter will be reset, so data can be retrieved from the correct tables later on
# 3. Checks whether that collection already exists.
#   3.1. If it already exists skip the creation of that table
#   3.2. If it does not already exist: Create the table as described in step 4
# 4. Get that collection for the current year
# 5. Now iterate over every document and get the values from "Latitude", "Longitude" and round them to 3 units after the comma
# 6. Now put them together as pair and check whether that poair already exists in "loc_Array".
#   6.1. If no, add that pair into the array and create number "1" for the first apperance of it in "loc_Array_Count".
#   6.2. If yes, simply raise that counter in "loc_Array_Count" by one
# 7. After the iteration of all documents is done simply write every pair of coordinates with its number of appearance into the database, document by document.
# </editor-fold>
class create_Location_Table:

	def __init__(self):
		print "...Initializing create_Location_Table..."

	def main_Method(self, mongo_DB_Chicago, mongo_DB_Collections, data_Counter_Starting, data_Counter_Ending):
		self.is_Not_Used()                              # Removes the 'not static' warning

		loc_Array = []                                  # Contains pairs of "Longitude" and "Latitude"
		loc_Array_Count = []                            # Contains a corresponding number, which describes the amount


		# Iterate over every table / collection and get the amount of arrested crimes
		for i in range (data_Counter_Starting, data_Counter_Ending):

			# Checks whether the table / collection "locX" already exists.. If not then create that table / collection
			if not any(str("loc" + str(i)) in s for s in mongo_DB_Collections):       # Whenever the table already exists -> do nothing

				print "Creating location entries for the year " + str(i)

				collection = mongo_DB_Chicago[str(i)]                                 # Gets the collection depending on the defined variable name (i.e. 2001)
				selector = collection.find()                                          # Give me all entries in that table with the attribute "Arrest" = True

				# Iterates over every document in this collection
				for document in selector:
					loc_Lat_Var = document.get("Latitude")                                                # only get me the the column "Latitude"
					loc_Lon_Var = document.get("Longitude")                                               # only get me the the column "Longitude"

					rounded_Loc_Lat_Var = "%.3f" % loc_Lat_Var                                            # Round to 3 units after the comma
					rounded_Loc_Lon_Var = "%.3f" % loc_Lon_Var                                            # Round to 3 units after the comma
					type_Var = [rounded_Loc_Lat_Var, rounded_Loc_Lon_Var]


					# This is a faster index checker than usual..
					# Source: https://stackoverflow.com/questions/7571635/fastest-way-to-check-if-a-value-exist-in-a-list

					try:
						b=loc_Array.index(type_Var)

					# Whenever the pair of Latitutide and Longitude does not exist yet
					except ValueError:
						loc_Array.extend([type_Var])          # adds that type into the list
						loc_Array_Count.extend([1])           # adds a counter into the count list
					# If crime type does already exist
					else:
						# raise counter by one, depending on index
						loc_Array_Count[loc_Array.index(type_Var)] +=1

				for j in range (0, len(loc_Array)):
					temp_Var = {"Latitude": loc_Array[j][0],
					            "Longitude": loc_Array[j][1],
					            "Count": loc_Array_Count[j]}

					temp_Var = collections.OrderedDict(sorted(temp_Var.items()))          # Contains that previously defined dictionary, with columns sorted in alphabetically order
					table_To_Be_Written = mongo_DB_Chicago["loc" + str(i)]                # references the table into which that data will be written
					table_To_Be_Written.insert_one(temp_Var)                              # write it now
			else:
				print "Table 'loc" + str(i) + "' already exists.. Skipping the creation of that table"

	def is_Not_Used(self):                                                                # Necessary to remove 'not static' warning
		pass