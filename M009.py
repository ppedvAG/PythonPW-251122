# Input & Output

# Input
# Nimmt einen String als Parameter und erwartet dann vom User einen Input über die Konsole
# x = input("Gib deinen Namen ein: ")  # Hält das Programm auf, bis die Eingabe getätigt wurde
# print(f"Hallo {x}")

# open
# Dateien öffnen zum Lesen/Schreiben
# Modi: w -> Write, r -> Read
file = open("Test.txt", "w")  # Datei öffnen
file.write("Hallo 1\n")  # In den Buffer Inhalte schreiben
file.write("Hallo 2\n")  # In den Buffer Inhalte schreiben
file.write("Hallo 3")  # In den Buffer Inhalte schreiben
file.flush()  # Buffer in die Datei weiterleiten
file.close()  # WICHTIG: Schließt den Stream

# Escape-Sequenzen
# Backslash + Code
# \n: Zeilenumbruch
# https://learn.microsoft.com/de-de/cpp/c-language/escape-sequences?view=msvc-170

# File lesen
file2 = open("Test.txt", "r")
lines = file2.readlines()
file2.close()
print(lines)

# with-Statement
# Schließt Dateien am Ende des Blockes automatisch
with open("Test.txt", "r") as file3:
	linesNeu = file3.readlines()
	print(linesNeu)
# Kein close() notwendig
# file3 hier unten nicht verfügbar

# rstring
# Raw String
# Interpretiert keine Escape-Sequenzen
pfad = "C:\Users\lk3\source\repos\Python_Grundkurs_2025_10_27\.venv\Scripts\python.exe"
pfadR = r"C:\Users\lk3\source\repos\Python_Grundkurs_2025_10_27\.venv\Scripts\python.exe"