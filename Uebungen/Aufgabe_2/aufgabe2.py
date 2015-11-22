# An der Loesung dieser Aufgabe waren folgende Personen beteiligt:
# Markus Guder, Philipp Mai, Benedikt Hierl, Christian Weber
# No animals were harmed during the creation of this program

from PIL import Image
import math

class KomplexeZahl(object):
	def __init__(self, re, im = None):
		self.re = re
		self.im = im

	# Addition ist hier definiert
	# (a + b * i) + (c + d * i) = (a + c) + (b + d) * i
	def __add__(self, other):
		returnedComplexNumber = KomplexeZahl(self.re + other.re, self.im + other.im)

		return returnedComplexNumber

	# Subtraktion ist hier definiert
	# (a + b * i) - (c + d * i) = (a - c) + (b - d) * i
	def __sub__(self, other):
		returnedComplexNumber = KomplexeZahl(self.re - other.re, self.im - other.im)

		return returnedComplexNumber

	# Multiplikation ist hier definiert
	# (a + b * i) * (c + d * i) = (a* c - b * d) + (a * d + b * c) * i
	def __mul__(self, other):
		realPart = (self.re * other.re) - (self.im * other.im)
		imaginaryPart = (self.re * other.im) + (self.im * other.re)

		returnedComplexNumber = KomplexeZahl(realPart, imaginaryPart)

		return returnedComplexNumber

	# Division ist hier definiert
	# ... = [((a * c) + (b * d)) / ((c * c) + (d * d))]   +   [((b * c) - (a * d)) / {((c * c) + (d * d))}] * i
	def __div__(self, other):
		realPart_upper = (self.re * other.re) + (self.im * other.im)
		realPart_lower = (other.re * other.re) + (other.im * other.im)

		ImaginaryPart_upper = (self.im * other.re) - (self.re * other.im)
		ImaginaryPart_lower = realPart_lower

		returnedComplexNumber = KomplexeZahl(realPart_upper / realPart_lower, ImaginaryPart_upper / ImaginaryPart_lower)

		return returnedComplexNumber

	# Ausgabe bei print-Befehl ist hier definiert
	def __str__(self):
		valuePositive = "+"

		# Wenn imaginaerer Part negativ ist
		if self.im < 0:
			return str(self.re) + str(self.im) + "*i"
		else:
			return str(self.re) + valuePositive + str(self.im) + "*i"


	# Absolute Betraege sind hier definiert
	def __abs__(self):
		squareReal = self.re * self.re
		squareImaginary = self.im * self.im
		squareRootOfSelf = math.sqrt(squareReal + squareImaginary)

		return squareRootOfSelf


if __name__ == "__main__":
	# Dimensionen
	breite, hoehe = 640, 480
	xMin = -2.2
	xMax = 0.8
	yMin = -1.3
	yMax = 1.3
	# Maximale Iterationszahl
	miz = 20
	# Obere Grenze
	dvbg = 2.0
	colourDeFolgee = (255, 0, 255) # Pink ist das neue Schwarz

	plakat = Image.new('RGB', (breite, hoehe))
	pixels = plakat.load()

	# Ueber Hoehe und Breite iterieren und dann entsprechend der Folge die Pixelfarbe setzen
	for h in range(hoehe):
		for b in range(breite):
			cCoords = KomplexeZahl(xMin + (xMax - xMin) * b / breite, yMin + (yMax - yMin) * h / hoehe)
			konv = KomplexeZahl(0, 0)

			for i in range(miz+1):
				konv = konv * konv + cCoords
				if abs(konv) >= dvbg:
					break

			if i >= miz:
				pixels[b, h] = colourDeFolgee
			else:
				pixels[b, h] = ((i * 17) % 256, (i * 13) % 256, (i * 23) % 256)

	plakat.save("plakat.png")


# !!! Uebungsaufgabe 1 !!!
instanzEinerKomplexenZahl_1 = KomplexeZahl(8,4)
instanzEinerKomplexenZahl_2 = KomplexeZahl(2,2)


# Exemplarische Rechenbeispiele
Rechnung_Addition = instanzEinerKomplexenZahl_1 + instanzEinerKomplexenZahl_2
Rechnung_Subtraktion = instanzEinerKomplexenZahl_1 - instanzEinerKomplexenZahl_2
Rechnung_Multiplikation = instanzEinerKomplexenZahl_1 * instanzEinerKomplexenZahl_2
Rechnung_Division = instanzEinerKomplexenZahl_1 / instanzEinerKomplexenZahl_2


# Calculator zur Ueberpruefung ob unser Code korrekt ist : https://www.mathsisfun.com/numbers/complex-number-calculator.html
print "Nachfolgend werden beide komplexen Zahlen abgebildet: "
print instanzEinerKomplexenZahl_1
print instanzEinerKomplexenZahl_2

print "Nachfolgend werden die Rechenoperationen durchgefuehrt: "
print Rechnung_Addition
print Rechnung_Subtraktion
print Rechnung_Multiplikation
print Rechnung_Division
