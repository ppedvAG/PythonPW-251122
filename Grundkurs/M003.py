# List
# Sammlung von Werten/Daten
# Wird mit [ ] definiert
l = [1, 2, 3, 4]

print(l)

# Index
print(l[0])
print(l[-1])
print(l[1:3])

# Listenfunktionen

# list.append(Element)
# Neues Element hinzufügen
l.append(5)
print(l)

# list.remove(Element)
# Element suchen und entfernen
l.remove(3)
print(l)

# list.pop(Index)
# Element anhand des Indizes entfernen
l.pop(3)
print(l)

# list.sort()
l.sort()
l.sort(reverse=True)
print(l)

# list.extend(andere Liste)
# Hängt 2 Listen aneinander
x = [1, 2, 3]
l.extend(x)
print(l)

l += x  # += Alternative zu extend
# l.append(x)  # append funktioniert hier nicht
print(l)

###############################################################

# Tupel
# Selbiger Hintergrund wie List, kann aber nicht verändert werden
t = (1, 2, 3)

print(t[0])

# Tupel über Umweg verändern
t2 = list(t)
t2.append(4)
t = tuple(t2)
print(t)

###############################################################

# range
# Bereich von X bis Y
print(range(1, 10))  # Output: range(1, 10) -> Range ist nur ein Generator; dieser muss ausgeführt werden

print(list(range(1, 10)))

print(list(range(100)))

print(list(range(0, 100, 5)))  # Schrittgröße angeben

###############################################################

# set
# Selbiger Hintergrund wie List, kann aber keine Duplikate enthalten
s = {1, 2, 3}
print(s)

s.add(4)
print(s)

s.add(1)  # Wird nicht hinzugefügt, weil schon enthalten
print(s)

###############################################################

# dict
# Liste von Schlüssel-Wert Paaren
# Ähnlich wie ein Set (eindeutige Schlüssel)
person = {
	"Vorname": "Max",
	"Nachname": "Mustermann",
	"Alter": 33,
	"Adresse": "Zuhause"
}

p = ["Max", "Mustermann", 33, "Zuhause"]  # Nachteil: Einzelne Werte können nur schwierig zugeordnet werden

print(person["Vorname"])  # Feld herausgreifen

person["Hoehe"] = 180  # Neues Feld hinzufügen

print(person)

person.setdefault("Hoehe", 200)  # Fügt den Wert nur hinzu, wenn dieser noch nicht existiert

print(person)

person.keys()  # Nur Schlüssel alleine
person.values()  # Nur Werte alleine
print(person.items())  # Alle Inhalte als Liste von Tupeln

###############################################################

# Konvertierung
# Variablen von einem Typen zu einem anderen Typen umwandeln
z = 5
z = float(z)

a = [1, 2 ,3]
a = tuple(a)
a = set(a)
a = list(a)

list(range(10))

print("Die Zahl ist: " + str(z))  # Hier Konvertierung zu str notwendig