# Schleifen
# Code mehrmals ausführen
# Zwei Schleifen: while-Schleife, for-Schleife

# while
# Enthält eine Bedingung; Schleife wird ausgeführt, solange die Bedingung True ist
i = 0
while i < 10:
	print(i)
	i += 1  # kein ++ in Python

# break und continue
# break: Beendet die Schleife (wird immer mit einer if kombiniert)
# continue: Springt zum Schleifenkopf zurück (überspringt allen Code danach)

# break
j = 0
while j < 10:
	print(j)
	j += 1
	if j > 5:
		break

# continue
k = 0
while k < 10:
	k += 1
	if k % 2 == 0:
		continue
	print(k)

# else bei Schleifen
# Wenn die Schleife erfolgreich abgeschlossen wird (kein break, Absturz), wird dieser Block ausgeführt
l = 0
while l < 10:
	print(l)
	l += 1
else:
	print("Schleife fertig")

# Endlosschleife
while True:
	print("Hallo")
	break

# Bis-Schleife
# Wartet, bis ein bestimmtes Ereignis eintritt
import time
while True:
	if time.time() % 10 == 0:
		print("Zeit endet mit 0")
	break

#############################################################

# for-Schleife
# Schleife, welche immer eine Liste benötigt
# Enthält immer eine Laufvariable, die über einen Variablennamen bereitgestellt wird
zahlen = [1, 2, 3, 4, 5]
for x in zahlen:
	print(x)

# Andere Listentypen: list, tuple, set, dict, range, str
text = "Hallo Welt"
for z in text:
	print(z)

# Schleife mit einer Range
for r in range(10):  # for (i = 0; i < 10; i++)
	print(r)

# Verschachtelte Schleife
for x in range(5):  # Für jeden Durchlauf der äußeren Schleife wird die innere Schleife vollständig ausgeführt
	for y in range(5):  # für 1x außen, 5x innen
		print("Tag " + str(x) + ": " + "Zwiebel " + str(y) + " geschnitten")

#############################################################

# fstring
# Code in Strings einbetten
zahl = 5
print("Die Zahl ist: " + str(zahl))
print(f"Die Zahl ist: {zahl}")

for x in range(5):
	for y in range(5):
		print(f"Tag {x}: Zwiebel {y} geschnitten")