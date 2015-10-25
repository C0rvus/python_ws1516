# An der Loesung dieser Aufgabe waren folgende Personen beteiligt:
# Christian Weber, Markus Guder, Benedikt Hierl, Philipp Mai

def anzahlDerWoerter(dokument):
	# Calls function for replacing commas and dots with ""
	noCommasAndDots = replaceCommasAndDots(dokument)
	# Splits whitespace
	words = noCommasAndDots.split()
	#Returns length of words in the list
	return len(words)

def anzahlUnterschiedlicherWoerter(dokument):
	# Calls function for replacing commas and dots with ""
	noCommasAndDots = replaceCommasAndDots(dokument)
	# Transforms document to lowercase
	lowerCase = noCommasAndDots.lower()
	# Splits whitespace
	words = lowerCase.split()
	# Get rid of the same words
	noSameWords = set(words)
	print noSameWords
	return len(noSameWords)

# Function for replacing commas and dots in document with ""
def replaceCommasAndDots(dokument):
	# Replaces commas
	noComma = dokument.replace(",", "")
	# Replaces dots
	noDot = noComma.replace(".", "")
	return noDot

dokument = open("ausarb.txt").read()
anzahlDerWoerter = anzahlDerWoerter(dokument)
anzahlUnterschiedlicherWoerter = anzahlUnterschiedlicherWoerter(dokument)

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
	
