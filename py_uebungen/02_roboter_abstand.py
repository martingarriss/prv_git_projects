# Roboter Projekt um Abstandsssensoren auszuwerten
# 23.10.2026 MG

abstaende_cm = [45, 38, 12, 231, 55, 27, 18, 0, 62, 31]


def print_abstaende(_liste):
    for i in _liste:
        print(f"Abstand: {i} cm")
        if i < 20:
            print("Achtung: Hindernis erkannt!")


def get_kleine_werte(_liste, _grenze=20):
    _zaehler = 0
    for i in _liste:
        if i < _grenze:
            _zaehler += 1
    return _zaehler, _grenze


def calculate_mittlerer_wert(_liste):
    _summe = sum(_liste)
    _anzahl = len(_liste)
    return _summe / _anzahl


def calculate_gleitender_mittelwert(_liste, _mittelwert=3):
    _grenze = len(_liste) - _mittelwert
    i = 0
    _liste_mittelwert = []
    while i <= _grenze:
        _liste_mittelwert.append((sum(_liste[i, i+_mittelwert]))/_mittelwert)

# main
# 1) print_abstaende(abstaende_cm)

# 2) anz_hindernisse_klein, grenze = get_kleine_werte(abstaende_cm)
# 2) print(f"Es sind {anz_hindernisse_klein} Werte kleiner als {grenze}.")


# 3) mittlerer_wert = calculate_mittlerer_wert(abstaende_cm)
# 3) print(f"Der Mittlere Wert der Liste ist {mittlerer_wert:.2f}.")
