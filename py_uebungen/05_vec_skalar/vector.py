class Vektor:
    def __init__(self, name="no name", a=0.0, b=0.0, c=0.0):
        self.werte = [a, b, c]
        self.name = name

    def ausgabe(self):
        print(f"--- Vektor {self.name} ---")
        for i, wert in enumerate(self.werte):
            print(f"Wert {i}: {wert}")


# Test Code:

a = Vektor("a", 1, 2, 3)
a.ausgabe()
