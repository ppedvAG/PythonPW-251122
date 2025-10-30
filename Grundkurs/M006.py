# List Comprehension
# Kurzschreibweise zur Erstellung von Listen
zahlen = []
for x in range(10):
	zahlen.append(x)
print(zahlen)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

zahlenLC = [x for x in range(10)]  # Schleife schreiben, x an den Anfang setzen
print(zahlenLC)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# if-Anweisungen
zahlenDurch2 = []
for x in range(10):
	if x % 2 == 0:
		zahlenDurch2.append(x)
print(zahlenDurch2)  # [0, 2, 4, 6, 8]

zahlenDurch2LC = [x for x in range(10) if x % 2 == 0]
print(zahlenDurch2LC)  # [0, 2, 4, 6, 8]

# Linke Seite verändern
print([x for x in range(10)])  # Liste von ints

# Beispiel: Liste mit 10x True erzeugen
t = []
for x in range(10):
	t.append(True)
print(t)

print([True for x in range(10)])  # x hier irrelevant

# Beispiel: Zahlen in Form von i^2 ausgeben
zahlenHoch2 = []
for x in range(1, 11):
	zahlenHoch2.append(f"{x}^2={x ** 2}")
print(zahlenHoch2)

zahlenHoch2LC = [f"{x}^2={x ** 2}" for x in range(1, 11)]
print(zahlenHoch2LC)

# Verschachtelte Schleifen

# Beispiel: Kleines 1x1
einMalEins = []
for x in range(1, 11):
	for y in range(1, 11):
		einMalEins.append(f"{x}x{y}={x * y}")
print(einMalEins)

einMalEinsLC = [f"{x}x{y}={x * y}" for x in range(1, 11) for y in range(1, 11)]
print(einMalEinsLC)

# Ternary Operator
fizzBuzz = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else
			"Fizz" if i % 3 == 0 else
			"Buzz" if i % 5 == 0 else
			i for i in range(1, 101)]
print(fizzBuzz)