abstaende_cm = [
    82, 76, 68, 59, 1, 51, 43, 35, 28, -3,
    22, 18, 15, 231, 13, 12, 11, 0, 14, 18,
    25, 34, 46, 58
    ]

# Die Funktion


def roboter_steuerung(sensor_liste):
    anzahl_stopp = 0
    for wert in sensor_liste:
        if wert > 30:
            print("FREI")
        elif wert >= 15:
            print("WARNUNG")
        else:
            print("STOP")
            anzahl_stopp += 1
    return anzahl_stopp


# Aufruf der Funktion
roboter_steuerung(abstaende_cm)
