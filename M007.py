# Funktionen
# Code wiederverwenden

# Einfache Funktion
def halloWelt():
	print("Hallo Welt")

halloWelt()
halloWelt()
halloWelt()

# Funktion mit Parameter
def hallo(deinName):
	print(f"Hallo {deinName}")

hallo("Lukas")
hallo("Jacqueline")

# Funktion mit Rückgabewert
def addiere(x, y):
	return x + y  # return muss immer das letzte Statement in einer Funktion sein
	print("Hallo")  # Nicht erreichbar

addiere(3, 4)  # Um das Ergebnis der Funktion verwenden zu können, muss hier eine Variable angelegt werden
summe = addiere(3, 4)  # Ergebnis in die summe Variable schreiben
print(summe)

print(addiere(3, 4))  # Ergebnis direkt verwenden
print(addiere(3.5, 6.7))
print(addiere("Hallo", "Welt"))  # Sollte nicht möglich sein
print(addiere([1, 2, 3], [4, 5, 6]))  # Sollte nicht möglich sein
# print(addiere("Hallo", 123))  # Sollte nicht möglich sein

#####################################################################

# Typempfehlung
# Bei Parametern kann ein Datentyp angegeben werden
# Das ist ein Hinweis für den User, das der Parameter einen bestimmten Wert bekommen soll
def addiere2(x: int, y: int):
	return x + y

print(addiere2(3, 5))
print(addiere2("Hallo", "Welt"))  # Funktioniert trotzdem

# Typvergleich: Wenn wichtig ist, das die Typen passen
def addiere3(x: int, y: int):
	if type(x) == int and type(y) == int:
		return x + y
	raise TypeError("x oder y haben nicht den richtigen Typen")

print(addiere3(3, 4))
# print(addiere3("Hallo", "Welt"))

# Mehrere Typempfehlungen
def addiere4(x: int | float, y: int | float):
	return x + y

#####################################################################

# Default Parameter
# Optionale Parameter
# Haben einen Standardwert, und können mitgegeben werden, müssen aber nicht
def hallo(name = ""):
	if name == "":
		print("Hallo Welt")
	else:
		print(f"Hallo {name}")

hallo("Lukas")
hallo()

# Stichwort: Funktionen konfigurieren

def komplexeFunktion(a: int = 0, b: str = "", c:float = 0, d: bool = False):
	print("...")

# Nachdem hier alle Parameter optional sind, können hier beliebige Parameter angesprochen und übergeben werden
komplexeFunktion(b = "Hallo", d = True)
komplexeFunktion(a = 5, c = 10)
komplexeFunktion(a = 9, d = True)
komplexeFunktion(b = "Welt")
komplexeFunktion()

#####################################################################

# Arbitrary Arguments
# Erlaubt es, bei einem Parameter beliebig viele Werte einzugeben
# Der Parameter ist innerhalb der Funktion ein Tupel
def summe(*zahlen):
	s = 0
	for x in zahlen:  # Kann mit einer Schleife iteriert werden
		s += x
	return s

print(summe(1, 2, 3, 4))
print(summe(1, 2, 3))
print(summe(1, 2))
print(summe(1))
print(summe())

#####################################################################

# Arbitrary Keyword Arguments
# Sammlung von BENANNTEN Argumenten
# Funktioniert wie *args, ist aber ein Dictionary
def test(**dict):
	for key, value in dict.items():
		print(f"Schlüssel: {key}, Wert: {value}")

test(Teilnehmer1 = "Jacqueline", Trainer = "Lukas")

#####################################################################

# Unpacking
# Listentypen in ihre Einzelteile zerlegen
# Funktioniert auch mit Dictionaries
# print(summe([1, 2, 3]))  # Funktioniert nicht
print(summe(*[1, 2, 3]))  # Funktioniert

# Beispiel: range(10) bei summe übergeben
print(summe(*range(10)))

person = {
	"Vorname": "Max",
	"Nachname": "Mustermann",
	"Alter": 33,
	"Adresse": "Zuhause"
}

test(**person)