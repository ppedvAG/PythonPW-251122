# Klassen und Objekte
# Klassen: Strukturen für komplexe Datentypen
# Objekte: Instanzen, die aus den Klassen erzeugt werden, und den Aufbau der Klasse haben

# Das Datentypen Quiz
# - int: Ganze Zahl
# - float: Kommazahl
# - str: Text
# - bool: Wahr-/Falschwert
# - list: Sammlung von Elementen
# - Person: ?

# Person ist ein komplexer Typ -> eigene Klasse

# Eigenschaften von Person:
# - Körpergröße: int
# - Haarfarbe: str
# - Geschlecht: str
# - Vorname: str
# - Nachname: str
# - Charaktereigenschaften: list[str]
class Person:
	# __init__
	# Sog. Konstruktor
	# Wird bei Erstellung des Objektes ausgeführt
	# Legt die Eigenschaften der Klasse/des Objektes an
	def __init__(self):
		self.hoehe = 0
		self.haarfarbe = ""
		self.geschlecht = ""
		self.vorname = ""
		self.nachname = ""
		self.charakter = []

p = Person()  # Erstellung eines Objektes
p.hoehe = 180
p.vorname = "Max"
p.nachname = "Mustermann"
p.geschlecht = "M"
p.haarfarbe = "Blond"
p.charakter = ["...", "...", "..."]

# print(f"Die Person heißt {p.vorname} {p.nachname} und ist {p.hoehe}cm groß.")

# Funktion definieren, welche eine Person als Parameter empfängt, und diese ausgibt
def printPerson(p: Person):
	print(f"Die Person heißt {p.vorname} {p.nachname} und ist {p.hoehe}cm groß.")

p2 = Person()
p2.hoehe = 175
p2.vorname = "Anna"
p2.nachname = "Musterfrau"
p2.haarfarbe = "Schwarz"
p2.charakter = []

printPerson(p)
printPerson(p2)

# Verbesserung Person Klasse

class PersonCool:
	"""
	Verbesserung Person Klasse
	"""
	def __init__(self, hoehe: int, haarfarbe: str, geschlecht: str, vorname: str, nachname: str, charakter: list):
		"""
		Wird ausgeführt, wenn die Person erzeugt wird

		:param hoehe: Die Körpergröße
		:param haarfarbe: Die Haarfarbe
		:param geschlecht: Das Geschlecht
		:param vorname: Der Vorname
		:param nachname: Der Nachname
		:param charakter: Die Charaktereigenschaften
		"""
		self.hoehe = hoehe
		self.haarfarbe = haarfarbe
		self.geschlecht = geschlecht
		self.vorname = vorname
		self.nachname = nachname
		self.charakter = charakter

	def bewegen(self, distanz: int):
		"""
		Über self kann das Objekt angegriffen werden, welches bewegen verwenden möchte
		"""
		print(f"{self.vorname} {self.nachname} bewegt sich um {distanz}m.")

# Direktes Befüllen der Werte möglich
pc = PersonCool(180, "Blond", "M", "Max", "Mustermann", ["...", "...", "..."])
pc2 = PersonCool(175, "Schwarz", "W", "Anna", "Musterfrau", [])

# Um bewegen auszuführen, muss ein Objekt vorliegen
pc.bewegen(10)
pc2.bewegen(10)