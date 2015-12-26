import unicodedata                                      # necessary for converting unicode datatypes to string
import collections                                      # necessary for sorting dictionaries

# <editor-fold desc="Pre calculated table / collection 'time' will be created here">
# This collection contains the amount of crimes per day time on a 24 hour basis
# This method works the following way:
# 1. Global DB_Instance "mongo_DB_Chicago" will be referenced first
# 2. Now the data counter will be reset, so data can be retrieved from the correct tables later on
# 3. Checks whether that collection already exists.
#   3.1. If it already exists skip the creation of that table
#   3.2. If it does not already exist: Create the table as described in step 4
# 4. Now an empty dictionary will be created with 24 entry possibilities. It will be filled later on
# 5. Now the current collection with all its entires will be retrieved, filtered by "Date" and converted from unicode to string
# 6. Afterwards the retrieved time will be split into various arrays and the timestamp will be correctly calculated depending on the 12h format (AM / PM)
# 7. After each document has been iterated a counter depending on the hours time will be raised and that entry will be written into the database
# </editor-fold>
class create_Time_Table:

	def __init__(self):
		print "...Initializing create_Time_Table..."

	def main_Method(self, mongo_DB_Chicago, mongo_DB_Collections, data_Counter_Starting, data_Counter_Ending):
		self.is_Not_Used()                              # Removes the 'not static' warning

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
					date_Var = document.get("Date")                                               # only get me the table with the column "Date"
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

	def is_Not_Used(self):                                                          # Necessary to remove 'not static' warning
		pass