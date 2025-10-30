# Fehlerbehandlung
# Abstürze verhindern

# Wenn der User einen Buchstaben eingibt, wird das Programm hier abstürzen
# eingabe = input("Gib eine Zahl ein: ")
# print(int(eingabe))
# Zwei Lösungen:
# - if
# - try-except

# In den meisten kann eine if-Anweisung verwendet werden
# Manchmal kann ein Absturz nicht vorhergesehen werden

try:  # Code, welcher abstürzen könnte
	eingabe = input("Gib eine Zahl ein: ")
	x = int(eingabe)  # ValueError
	print(x)  # Wenn eine vorherige Zeile abstürzt, wird das print ausgeführt
except ValueError:  # Wenn der Code im try-Block abstürzen würde, wird stattdessen der except-Block ausgeführt
	print("Keine Zahl eingegeben")
except EOFError:  # Fehler 2
	print("Programm mit Strg + D beendet")
except:  # Alle anderen Fehler
	print("Anderer Fehler")
else:  # Wenn kein except-Block ausgeführt wird, wird der else-Block ausgeführt
	print("Try ohne Fehler")
finally:  # Wird ausgeführt, egal ob ein Fehler passiert ist oder nicht
	print("Wird immer ausgeführt")

# raise: Lasse das Programm abstürzen
# raise SystemError("Hallo")

# Warum würde ich mein Programm abstürzen lassen wollen?
# Im obigen Bespiel wurde immer print verwendet
# Was ist, wenn wir eine Webseite haben?
# Mithilfe von try-except und raise können Fehlermeldungen bei beliebigen Outputs ausgegeben werden
# z.B.: Logfile, Webseite, GUI, Datenbank, Mobile Benachrichtigung, ...

try:
	raise SystemError("Hallo")
except SystemError as e:
	print("Fehler")  # Fehler in die Konsole schreiben
	import traceback
	with open("Log.txt", "a") as log:  # Fehler in das Log schreiben
		for z in traceback.format_exception(e):
			log.write(z)