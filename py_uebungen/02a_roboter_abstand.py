# Roboter Projekt um Abstandsssensoren auszuwerten
# 23.10.2026 MG

import matplotlib.pyplot as plt

abstaende_cm = [45, 38, 12, 231, 55, 27, 18, 0, 62, 31]


def print_abstaende(_liste):
    for i in _liste:
        print(f"Abstand: {i:.2f} cm")
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
        _liste_mittelwert.append((sum(_liste[i: i+_mittelwert]))/_mittelwert)
        i += 1
    return _liste_mittelwert


def calculate_ema_filter(_liste, _alpha=0.2):
    _neue_liste = []
    _gefiltert = _liste[0]
    for abstand in _liste:
        _gefiltert = _alpha * abstand + (1 - _alpha) * _gefiltert
        _neue_liste.append(_gefiltert)
    return _neue_liste


def calculate_median_filter(_liste, _fenstergroesse=3):
    
    _grenze = len(_liste) - _fenstergroesse
    i = 0
    _liste_median = []
    while i <= _grenze:
        _sortiert = sorted(_liste[i: i+_fenstergroesse])
        _liste_median.append(_sortiert[1])
        i += 1
    return _liste_median


def plot_Messwerte(_liste):
    plt.plot(_liste, label="nicht geglättet")
    plt.xlabel("Zeitverlauf")
    plt.ylabel("Abstand in cm")
    plt.legend()
    plt.show()

# main
# 1) print_abstaende(abstaende_cm)

# 2) anz_hindernisse_klein, grenze = get_kleine_werte(abstaende_cm)
# 2) print(f"Es sind {anz_hindernisse_klein} Werte kleiner als {grenze}.")


mittlerer_wert = calculate_mittlerer_wert(abstaende_cm)
# 3) print(f"Der Mittlere Wert der Liste ist {mittlerer_wert:.2f}.")

gleit_mittlerer_wert = calculate_gleitender_mittelwert(abstaende_cm)
# 4) print_abstaende(gleit_mittlerer_wert)

ema_werte = calculate_ema_filter(abstaende_cm)
# 5) print_abstaende(ema_werte)

median_werte = calculate_median_filter(abstaende_cm)
# 6) print_abstaende(median_werte)

plot_Messwerte(abstaende_cm)
