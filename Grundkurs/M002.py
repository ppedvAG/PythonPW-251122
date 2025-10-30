# Kommentare
# Alle Kommentare müssen mit einer Raute beginnen
# Keine mehrzeiligen Kommentare
print("Hallo")  # Inline Kommentar

# Variablen
# Behälter für Werte/Daten
x = 5
print(x)

# Datentypen
# int: Ganze Zahlen
# Beliebig große Zahlen
x = 5356728197423869174940135867901358749104765794025764

# float: Kommazahlen
# Beliebig große Zahlen
y = 23587948120547635403257579241034857623.3645728794365493574649237695

# str: String
# Beliebig lange Zeichenkette
# Muss mit Hochkomma definiert werden (einzelne oder doppelte)
print("Hallo Welt")
print('Hallo Welt')

# bool: Wahr-/Falschwert
b = True
f = False

# complex: Komplexe Zahlen
c = 1 + 2j

# Index
# Einzelteile von Listen angreifen
text = "Hallo Welt"

print(text[0])  # H
print(text[-1])  # t
print(text[3:5])  # Obergrenze nicht inkludiert (lo)

print(text[:5])  # 0-4: Hallo
print(text[3:])  # 3-Ende: lo Welt

# Stringfunktionen
print(text.lower())  # Verändert nicht den originalen String
print(text)

print(text.upper())

print(text.count("l"))

print(text[0].islower())  # Ist der Anfangsbuchstabe lowercase?

print(text.capitalize())
print(text.title())

print(len(text))  # len: Gesamtanzahl der Elemente

# Arithemtische Operatoren
# +, -, *, /
# %, **, //

z1 = 5
z2 = 8
print(z1 + z2)  # z1 und z2 bleiben unverändert
print(z1)  # Bleibt 5
print(z2)  # Bleibt 8

z1 += z2  # Bildet die Summe, und schreibt diese in z1
# z1 = z1 + z2

print(z1 / z2)  # 13 / 8 = 1.625

print(z1 // z2)  # Ganzzahldivision: 13 / 8 = 1

print(z1 % z2)  # Modulo: Rest einer Division (5) - 13 / 8 = 1, 5R.

print(z1 ** z2)  # Potenzoperator: x^y (815730721) - 13 ^ 8 = 815730721