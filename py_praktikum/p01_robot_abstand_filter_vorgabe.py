# ---------------------------------------------------------
# Technische Informatik - Praktikum 1
# Roboter mit Hinderniserkennung
# ---------------------------------------------------------
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# Funktionen
# ---------------------------------------------------------
def roboter_steuerung(sensor_liste):
    anzahl_stopp = 0
    for wert in sensor_liste:
        if wert > 30:
            print("FREI")
        elif wert < 15:
            print("STOP")
            anzahl_stopp += 1
        else:
            print("WARNUNG")

    print("Anzahl STOPP:", anzahl_stopp)
    return anzahl_stopp


def mittelwert3(liste):
    gefilterte_liste = []
    for i in range(2, len(liste)):
        gefilterte_liste.append((liste[i-2] + liste[i-1] + liste[i])/3)
        print("test")

    print("Gleitender Mittelwert:")
    print(gefilterte_liste)
    return gefilterte_liste


def median3(liste):
    gefilterte_liste = []
    for i in range(2, len(liste)):
        ausschnitt = sorted(liste[i-2:i+1])
        gefilterte_liste.append(ausschnitt[1])

    print("Median:")
    print(gefilterte_liste)
    return gefilterte_liste


def ema_filter(liste, alpha):
    """Berechnet den Exponential Moving Average."""
    gefilterte_liste = []
    # Erster Messwert = erster Filterwert
    ema_alt = liste[0]
    gefilterte_liste.append(ema_alt)
    _gefiltert = liste[0]

    for abstand in liste:
        _gefiltert = alpha * abstand + (1 - alpha) * _gefiltert
        gefilterte_liste.append(_gefiltert)

    print("EMA:")
    print(gefilterte_liste)

    return gefilterte_liste


# ---------------------------------------------------------
# Messwerte
# ---------------------------------------------------------
abstaende_cm = [
    82, 76, 68, 59, 1, 51, 43, 35, 28, -3, 22, 18,
    15, 231, 13, 12, 11, 0, 14, 18, 25, 34, 46, 58,
    12, 10, 9
]

# ---------------------------------------------------------
# Aufgabe 1 - Sensordaten untersuchen
# ---------------------------------------------------------
print("\n--- Aufgabe 1 ---")
print("Anzahl Messwerte:", len(abstaende_cm))
print("Erster Messwert:", abstaende_cm[0])

for wert in abstaende_cm:
    print(f"Abstand: {wert} cm")

# ---------------------------------------------------------
# Aufgabe 2 - Hindernisse erkennen
# ---------------------------------------------------------
print("\n--- Aufgabe 2 ---")
roboter_steuerung(abstaende_cm)

# ---------------------------------------------------------
# Aufgabe 3 - Gleitender Mittelwert
# ---------------------------------------------------------
print("\n--- Aufgabe 3: Gleitender Mittelwert ---")
abstaende_mittelwert = mittelwert3(abstaende_cm)
roboter_steuerung(abstaende_mittelwert)
# ---------------------------------------------------------
# Aufgabe 4 - Medianfilter
# ---------------------------------------------------------
print("\n--- Aufgabe 4: Medianfilter ---")
abstaende_cm_median = median3(abstaende_cm)  # Filter anwenden
# Roboterentscheidung mit Medianwerten
roboter_steuerung(abstaende_cm_median)

# ---------------------------------------------------------
# Aufgabe 5 - EMA-Filter
# ---------------------------------------------------------
print("\n--- Aufgabe 5: EMA-Filter ---")
alpha = 0.2
abstaende_ema = ema_filter(abstaende_cm, alpha)

roboter_steuerung(abstaende_ema)

# ---------------------------------------------------------
# Aufgabe 6 - Vergleich der Filter
# ---------------------------------------------------------
print("\n--- Aufgabe 6: Diagramm ---")

# Originalwerte
plt.plot(
    range(len(abstaende_cm)),
    abstaende_cm,
    marker="x",
    label="Original"
)

"""
# Medianfilter
# Die gefilterte Liste ist um zwei Werte kürzer.
# Die Ergebnisse werden deshalb ab Index 1 dargestellt.
plt.plot(
    range(1, len(abstaende_cm) - 1),
    abstaende_cm_median,
    marker="o",
    label="Median"
)

# Gleitender Mittelwert
# Die gefilterte Liste ist um zwei Werte kürzer.
# Die Ergebnisse werden deshalb ab Index 1 dargestellt.
plt.plot(
    range(1, len(abstaende_cm) - 1),
    abstaende_mittelwert,
    marker="o",
    label="Gleitender Mittelwert"
)

# EMA
plt.plot(
    range(len(abstaende_cm)),
    abstaende_ema,
    marker="o",
    label="EMA"
)
"""

plt.xlabel("Messwert Nr.")
plt.ylabel("Abstand [cm]")
plt.title("Vergleich verschiedener Filter")
plt.grid()
plt.legend()
plt.show()