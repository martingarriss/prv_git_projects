# Programm zur Berechnung des Body Mass Index
# 19.10.2026 MG

# benötigte Eingaben
# Alter
# Größe
# Gewicht


def werteeingabe():
    print("Berechnung des Body-Mass-Index BMI")
    _alter = int(input("Wie alt sind Sie?"))
    _groesse = float(input("Wie gross sind Sie in m?"))
    _gewicht = int(input("Wie schwer sind Sie in kg?"))
    return _alter, _groesse, _gewicht


def bmi_grenze_ermitteln(_alter):
    if _alter < 19:
        print("Dein Alter ist zu gering um deinen BMI auszurechnen")
    elif _alter < 25:
        _bmi_min = 19
        _bmi_max = 24
    elif _alter < 35:
        _bmi_min = 20
        _bmi_max = 25
    elif _alter < 45:
        _bmi_min = 21
        _bmi_max = 26
    elif _alter < 55:
        _bmi_min = 22
        _bmi_max = 27
    elif _alter < 65:
        _bmi_min = 23
        _bmi_max = 28
    else:
        _bmi_min = 24
        _bmi_max = 29
    return _bmi_min, _bmi_max


def bmi_berechnen(_groesse, _gewicht):
    _bmi = _gewicht / (_groesse ** 2)
    return _bmi


def bmi_auswerten(_bmi_min, _bmi_max, _bmi):
    print(f"Ihr BMI ist {_bmi:.2f}")
    if _bmi < _bmi_min:
        print("Sie haben Untergewicht!")
    elif _bmi > _bmi_max:
        print("Sie habne Übergewicht!")
    else:
        print("Sie haben Normalgewicht!")


alter, groesse, gewicht = werteeingabe()
bmi = bmi_berechnen(groesse, gewicht)
bmi_min, bmi_max = bmi_grenze_ermitteln(alter)
bmi_auswerten(bmi_min, bmi_max, bmi)
