# ---------------------------------------------------------
# Messwerte
# ---------------------------------------------------------
abstaende_cm = [
    82, 76, 68, 59, 1, 51, 43, 35, 28, -3, 22, 18,
    15, 231, 13, 12, 11, 0, 14, 18, 25, 34, 46, 58,
    12, 10, 9
]
anzahl_werte = len(abstaende_cm)
print(f"Anzahl Messwerte: {anzahl_werte}",)

print(f"Erster Messwert: {abstaende_cm[0]}",)

for abstaende in abstaende_cm:
    print(f"Abstand: {abstaende} cm")
