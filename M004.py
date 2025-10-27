# if-Abfragen

z1 = 5
z2 = 8

if z1 > z2:  # Führt das print-Statement nur aus, wenn z1 größer als z2 ist
	print("z1 ist größer als z2")  # WICHTIG: Einrückungen beachten


if z1 > z2:  # WICHTIG: Doppelpunkt nicht vergessen
	print("z1 ist größer als z2")  # WICHTIG: Einrückungen beachten
elif z1 < z2:  # WICHTIG: Doppelpunkt nicht vergessen
	print("z1 ist kleiner als z2")  # WICHTIG: Einrückungen beachten
else:  # WICHTIG: Doppelpunkt nicht vergessen
	print("z1 ist gleich z2")  # WICHTIG: Einrückungen beachten

# Vergleichsoperatoren
# ==, !=
# <, >=
# >, <=

# Logische Operatoren
# and, or / &, |
# not / ~
# in / not in

# in
# Prüft, ob ein Element in einer Liste vorhanden ist (contains)

# Aufgabe: Ist die Zahl 4 in einer Liste enthalten?
l = [1, 2, 3, 4, 5]
if 4 in l:
	print("4 ist in l enthalten")

print(4 in l)

# Ternary Operator
# Kurzschreibweise für if/elif/else Blöcke
if z1 > z2:  # WICHTIG: Doppelpunkt nicht vergessen
	print("z1 ist größer als z2")  # WICHTIG: Einrückungen beachten
elif z1 < z2:  # WICHTIG: Doppelpunkt nicht vergessen
	print("z1 ist kleiner als z2")  # WICHTIG: Einrückungen beachten
else:  # WICHTIG: Doppelpunkt nicht vergessen
	print("z1 ist gleich z2")  # WICHTIG: Einrückungen beachten

print("z1 ist größer als z2") if z1 > z2 else print("z1 ist kleiner als z2") if z1 < z2 else print("z1 ist gleich z2")

print("z1 ist größer als z2" if z1 > z2 else "z1 ist kleiner als z2" if z1 < z2 else "z1 ist gleich z2")