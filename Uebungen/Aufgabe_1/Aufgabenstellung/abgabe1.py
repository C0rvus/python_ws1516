# An der Loesung dieser Aufgabe waren folgende Personen beteiligt:
# <bitte ergaenzen>

def anzahlDerWoerter(dokument):
	# Hier bitte Aufgabe 1a eintragen
	return 0

def anzahlUnterschiedlicherWoerter(dokument):
	# Hier bitte Aufgabe 1b eintragen
	return 0

	

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
	
