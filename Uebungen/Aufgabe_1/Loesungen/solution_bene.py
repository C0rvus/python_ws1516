# An der Loesung dieser Aufgabe waren folgende Personen beteiligt:
# Markus Guder, Philipp Mai, Benedikt Hierl, Christian Weber



# Solution exercise 1a
def anzahlDerWoerter(dokument):

	# Process the document my executing a method which kicks commas and dots out of it
	processDocument = kickCommaAndDots(dokument)


	# Return the amount of words in the text without comma and dots
	return len(processDocument)



# Solution exercise 1b
def anzahlUnterschiedlicherWoerter(dokument):

	# Converts every object to lower case
	documentLowerCase = dokument.lower()

	# Now commas and dots get kicked out of the text
	processDocument =  kickCommaAndDots(documentLowerCase)

	# Set only holds unique members, therefore we use it here
	amountOfUniqueWords = set(processDocument)


	# Return the amount of unique words
	return len(amountOfUniqueWords)



# Removes comma and whitespaces out of the document
def kickCommaAndDots(dokument):

	# Dots get replaced with nothing here -> therefore they get removed
	documentPrepared = dokument.replace(".", "")

	# Commata get replaced with nothing here -> therefore they get removed
	documentPrepared = documentPrepared.replace(",", "")

	# The remaining parts will be broken up, removing line breaks and splitting the text by whitespaces
	documentPrepared = documentPrepared.split()


	# Return the "heavily" modified document back to it's former call
	return documentPrepared


#######################################################################################

# Opens the necessary document here
dokument = open("ausarb.txt").read()

# Executes the method "anzahlDerWoerter" and brings "dokument" with it
anzahlDerWoerter = anzahlDerWoerter(dokument)

# Executes the method "anzahlUnterschiedlicherWoerter" and brings "dokument" with it
anzahlUnterschiedlicherWoerter = anzahlUnterschiedlicherWoerter(dokument)


# Below here the code input will be checked
print "1a) " + str(anzahlDerWoerter)
if anzahlDerWoerter == 134:
	print "Das sieht soweit gut aus!\n"
else:
	print "Da fehlt noch was!\n"
	
print "1b) " + str(anzahlUnterschiedlicherWoerter)
if anzahlUnterschiedlicherWoerter == 99:
	print "Das sieht soweit gut aus!\n"
else:
	print "Da fehlt noch was!\n"