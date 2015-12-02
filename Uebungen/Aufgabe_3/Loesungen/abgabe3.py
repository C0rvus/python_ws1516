# An der Loesung dieser Aufgabe waren folgende Personen beteiligt:
# Markus Guder, Philipp Mai, Benedikt Hierl, Christian Weber
# No animals were harmed during the creation of this program

import glob
import csv
import numpy as np

class DatenAnalyse(object):

	def __init__(self, dateien):
		global dataArray
		dataArray = dateien
		pass

	@property
	def anzahlWeiblichUndMaennlichInKarteUndGraph(self):
		graphM = 0
		graphW = 0
		karteM = 0
		karteW = 0
		for file in dataArray:
			with open(file) as csvfile:
				reader = csv.reader(csvfile)
				for row in reader:
					if(row[3] == 'Graph'):
						if(row[2] == 'm'):
							graphM = graphM + 1
						if(row[2] == 'w'):
							graphW = graphW + 1
					if(row[3] == 'Karte'):
						if(row[2] == 'm'):
							karteM = karteM + 1
						if(row[2] == 'w'):
							karteW = karteW + 1
		ausgabe = {'Graph': {'m': graphM, 'w': graphW}, 'Karte': {'m': karteM, 'w': karteW}}
		return ausgabe

	def arithmetischesMittel(self):
		ausgabe = {}
		return ausgabe

	@staticmethod   # << PyCharm told me to make this method static.
	def unterschiedSchlechtOrientierteGutOrientierte():
		bigArray = []
		for file in dataArray:
			with open(file) as csvfile:
					reader = csv.reader(csvfile)
					for row in reader:
						if(row[0] != 'PID'):
							bigArray.append(row)

		badGoodArray = [[],[]]
		globalArithemtic = []
		for person in bigArray:

			numbers = np.array(person)

			x = numbers[6: 25:] # contains the OS values from OS1 to OS19

			x.sort()            # sorting array for correct mean calculation

			y = x.astype(np.float)

			personArithmetics = np.mean(y)
			person.append(personArithmetics)
			globalArithemtic.append(personArithmetics)


		median = np.median(globalArithemtic)

		for person in bigArray:
			if(person[len(person)-1] < median):         #the last index contains the calculated median for the appropriate person (i.e. 3.6190476190476191)
				badGoodArray[0].append(person)          #[0] means bad orientation
			else:
				badGoodArray[1].append(person)          #[1] means good orientation


		badGoodMaster = []
		for os in badGoodArray:
			badGoodSubMaster = []
			for person in os:
				numbers = np.array(person)
				x = numbers[26: 33:]
				y = x.astype(np.float)
				badGoodSubMaster.append(y)
			badGoodMaster.append(badGoodSubMaster)
		i = 0
		results = []

		while i<7:
			for element in badGoodMaster:
				person = np.array(element)
				median = np.mean(person[:,i])
				results.append("%.2f" % median)
			i=i+1

		# because "result" stores entries as "Strings" the single results will be converted to float, so the winning condition is fulfilled
		ausgabe = {'d6': {'badOS': float(results[10]), 'goodOS': float(results[11])}, 'd7': {'badOS': float(results[12]), 'goodOS': float(results[13])}, 'd4': {'badOS': float(results[6]), 'goodOS': float(results[7])}, 'd5': {'badOS': float(results[8]), 'goodOS': float(results[9])}, 'd2': {'badOS': float(results[2]), 'goodOS': float(results[3])}, 'd3': {'badOS': float(results[4]), 'goodOS': float(results[5])}, 'd1': {'badOS': float(results[0]), 'goodOS': float(results[1])}}

		return ausgabe

		
# ##############################################################################
#
# Abgaben-Ueberpruefung
#
# ##############################################################################

if __name__ == "__main__":
	datenAnalyseInstanz = DatenAnalyse(glob.glob("probanden*.csv"))
	
	if datenAnalyseInstanz.anzahlWeiblichUndMaennlichInKarteUndGraph == {'Graph': {'m': 20, 'w': 16}, 'Karte': {'m': 19, 'w': 19}}:
		print "Aufgabe 3a) sieht soweit gut aus"
	else:
		print "Aufgabe 3a) ist noch nicht fertig"

	if datenAnalyseInstanz.arithmetischesMittel() == {'Graph': {'OS15': 4.69, 'OS14': 4.42, 'OS17': 2.94, 'OS16': 4.56, 'OS11': 3.14, 'OS10': 4.08, 'OS13': 4.39, 'OS12': 4.44, 'OS19': 3.86, 'OS18': 3.67, 'OS9': 4.83, 'OS8': 4.17, 'PedNav': 3.14, 'OS1': 4.53, 'OS3': 3.89, 'OS2': 4.5, 'OS5': 4.25, 'OS4': 4.44, 'OS7': 3.64, 'OS6': 3.08, 'OKS': 4.08, 'SM': 5.81, 'D6': 4.97, 'D7': 5.61, 'D4': 6.08, 'D5': 4.47, 'D2': 5.78, 'D3': 5.42, 'D1': 5.25}, 'Karte': {'OS15': 5.34, 'OS14': 4.66, 'OS17': 3.79, 'OS16': 4.16, 'OS11': 3.42, 'OS10': 4.61, 'OS13': 4.76, 'OS12': 4.92, 'OS19': 3.55, 'OS18': 3.79, 'OS9': 4.42, 'OS8': 4.82, 'PedNav': 2.92, 'OS1': 4.87, 'OS3': 3.84, 'OS2': 3.95, 'OS5': 5.05, 'OS4': 4.29, 'OS7': 3.24, 'OS6': 3.37, 'OKS': 3.66, 'SM': 5.55, 'D6': 5.05, 'D7': 5.76, 'D4': 6.08, 'D5': 5.37, 'D2': 6.08, 'D3': 5.53, 'D1': 5.68}}:
		print "Aufgabe 3b) sieht soweit gut aus"
	else:
		print "Aufgabe 3b) ist noch nicht fertig (nur benoetigt, wenn Sie sich das Seminar im Masterstudium anrechnen lassen moechten)"
		
	if datenAnalyseInstanz.unterschiedSchlechtOrientierteGutOrientierte() == {'d6': {'badOS': 5.22, 'goodOS': 4.82}, 'd7': {'badOS': 5.61, 'goodOS': 5.76}, 'd4': {'badOS': 5.97, 'goodOS': 6.18}, 'd5': {'badOS': 4.69, 'goodOS': 5.16}, 'd2': {'badOS': 6.03, 'goodOS': 5.84}, 'd3': {'badOS': 5.75, 'goodOS': 5.21}, 'd1': {'badOS': 5.53, 'goodOS': 5.42}}:
		print "Aufgabe 3c) sieht soweit gut aus"
	else:
		print "Aufgabe 3c) ist noch nicht fertig"