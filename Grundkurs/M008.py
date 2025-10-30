# Module
# Effektiv Python Skripte, die in andere Skripte eingebunden werden

# import
# Mit import kann ein anderes Skript hier verwendet werden
# Bei einem Import wird Zugriff auf alle Member gewährt (Variablen, Funktionen, Klassen)
# WICHTIG: Bei einem Import wird IMMER das gesamte Skript ausgeführt
import M000
print(M000.text)
M000.countCase("Hallo")

# from import
# Der from import importiert aus einem Skript bestimmter Member (nicht alle)
# Wenn dadurch ein Member eingebunden wird, kann dieser ohne Prefix aufgerufen werden
# WICHTIG: Bei einem Import wird IMMER das gesamte Skript ausgeführt
from M000 import countCase
# print(text)  # Nicht möglich
countCase("Hallo")  # ohne M000.

###########################################################

# Modul Suchpfade
# Bei einem Import werden bestimmte Pfade nach dem gesuchten Skript gesucht
import sys
for pfad in sys.path:
	print(pfad)
sys.path.append("C:\\Users\\lk3\\Dekstop")  # Eigenen Suchpfad hinzufügen

# 1. Derselbe Ordner wie das jetzt ausführende Skript
# 2. Die Python Standardbibliothek
# 3. Global Installierte Pakete
# 4. Lokal Installierte Pakete
# 5. Eigene Pfade
# Wenn Modul nicht gefunden: ModuleNotFoundError

###########################################################

# Externe Pakete
# Neue Funktionalitäten hinzufügen
# z.B. Numpy, Pandas, Requests, ...

# 2 Optionen
# - Python Packages
# - pip (Python Package Installer)

###########################################################

# Die Main-Methode
# Startpunkt des Skripts
# Generell, werden Skripte nur für den Import vorgesehen
# Falls das Skript dann direkt ausgeführt wird, passiert nichts
# Falls das Skript Code enthalten soll, der bei direkter Ausführung passieren soll, kann eine Main-Methode verwendet werden

# __name__
# Variable, welche immer verfügbar ist
# Zwei Inhalte: __main__ (bei direkter Ausführung), Der Name des Skriptes selbst (wenn es importiert wird)
print(__name__)

if __name__ == "__main__":  # Wenn das Skript nur importiert wird, wird dieser Code übersprungen
	print()