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
