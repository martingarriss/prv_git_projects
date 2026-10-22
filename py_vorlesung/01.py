# Operatoren:
# +, -, *, /, //, %, **
# Zuweisungen:
# x += 5 # x = x + 5 (genauso mit allen anderen Operatoren)
# f-String:
abstand = 15.456
print(f"Abstand: {abstand:.2f} cm")  # rundet auf 2 Nachkommastellen

# Kontrollflussanweisungen
distanz = 15
if distanz < 20:
    print("Roboter stoppen")
elif distanz < 50:
    print("Langsam fahren")
else:
    print("Normale fahren")  # 4 Leerzeichen Einrückung

# Eingabeabfrage
alter = int(input("Wie alt bist du?"))
print("Also bist du", alter, "Jahre alt.")
print(alter, "ist aus der", type(alter))

# Listen
werte = [13, 56, 40]
werte.sort()  # Werte werden aufsteigend sortiert
werte.sort(reverse=True)  # Werte werden absteigend sortiert
sortierte_werte = sorted(werte)
# speichert die sortierten Werte in sortierte_werte. werte bleibt unverändert
ausschnitt = werte[2:3]  # gibt ab der 2. Zahl bis vor der 3. Zahl zurück
# [:3] > die ersten 3 Werte
# [3:] > ab Index 3 bis Ende
# [-3:] > die letzten 3 Werte
werte.append(40)  # hängt an Werte die Zahl 40 an
# enumerate(liste) gibt index, wert zurück
# enumerate(liste, start) - start gibt den Startindex an
len(werte)  # Anzahl der Elemente
sum(werte)  # Summ der Elemente
werte.insert(10, 2)  # Element 10 an Index 2 einfügen
werte.extend(sortierte_werte)  # Liste an die Liste anhängen
werte.remove(13)  # Element mit Wert 13 entfernen
werte.pop(2)  # Element an Index 2 entfernen
werte.clear()  # alle Elemente entfernen
werte.index(40)  # Index von Element mit Wert 40 bestimmen
werte.count(13)  # Anzahl der Werte 13
werte.reverse()  # Reihenfolge umkehren
werte.copy()  # Kopie der Liste erzeugen

# Funktionen


def addiere(_x, _y=0):
    return _x + _y
# Wenn nur mit 1 Zahl aufgerufen, wird für y 0 angenommen.
# (5) -> 5
# (5,10) -> 15

# main Methode


def main():
    _x = 3
    _y = 5
    _ergebnis = _x + _y
    print(_ergebnis)


if __name__ == "__main__":
    main()
# Hauptprogramm wird nur aufgerufen, wenn Datei direkt aufgerufen wird
