import turtle

t = turtle.Turtle()

t.shape("turtle")
t.speed(5)


def zeichne_viereck():
    for i in range(4):
        t.forward(100)
        t.left(90)


def zeichne_sechseck():
    for i in range(6):
        t.forward(80)
        t.left(60)


def zeichne_spirale():
    for i in range(30):
        t.forward(i * 5)
        t.left(90)


def zeichne_vieleck(anzahl_seiten, laenge):
    for i in range(anzahl_seiten):
        t.pencolor("blue")
        t.forward(laenge)
        t.left(360/anzahl_seiten)


def zeichne_verdrehte_quadrate():
    for i in range(36):
        for j in range(4):
            t.forward(100)
            t.left(90)
        t.left(10)


# for i in range(5):
#     t.forward(100)
#     t.right(144)

zeichne_verdrehte_quadrate()

t.done()
