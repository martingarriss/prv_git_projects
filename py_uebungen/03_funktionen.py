# def begreussung():
#     print("Willkommen zu TINpy")


# for i in range(3):
#     begreussung()
# # cmd + k dann cmd + c -> auskommentieren
# # cmd + k dann cmd + u -> zurück kommentar weg machen


# def rechteck_flaeche(_breite, _hoehe):
#     return _breite * _hoehe


# print(rechteck_flaeche(12, 4))


# def celsius_zu_fahrenheit(_celsius):
#     return _celsius * 1.8 + 32


# print(celsius_zu_fahrenheit(0))
# print(celsius_zu_fahrenheit(20))
# print(celsius_zu_fahrenheit(100))


def berechne_strecke(_geschw, _zeit):
    return _geschw * _zeit


def ausgabe_strecke(_strecke):
    print(f"Die zurückgelegte Strecke beträgt {_strecke:.2f}m.")


ausgabe_strecke(berechne_strecke(0.25, 12))
