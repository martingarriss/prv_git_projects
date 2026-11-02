import turtle
import random

t = turtle.Turtle()
r = random.Random()

r.seed()
t.speed(5)
turtle.colormode(255)

# t.left(90)
# t.forward(100)
# t.right(45)
# t.forward(71)
# t.right(90)
# t.forward(71)
# t.right(45)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(135)
# t.forward(142)
# t.left(135)
# t.forward(100)
# t.left(135)
# t.forward(142)


def draw_house(wandlaenge=100, x_koordinate=0, y_koordinate=0, richtung=0):
    t.color(r.randint(1, 255), r.randint(1, 255), r.randint(1, 255))
    t.teleport(x_koordinate, y_koordinate)
    t.setheading(richtung)
    t.backward(wandlaenge/2)
    t.left(90)
    t.forward(wandlaenge)
    t.right(45)
    t.forward(((wandlaenge ** 2 + wandlaenge ** 2) ** 0.5)/2)
    t.right(90)
    t.forward(((wandlaenge ** 2 + wandlaenge ** 2) ** 0.5)/2)
    t.right(45)
    t.forward(wandlaenge)
    t.right(90)
    t.forward(wandlaenge)
    t.right(135)
    t.forward((wandlaenge ** 2 + wandlaenge ** 2) ** 0.5)
    t.left(135)
    t.forward(wandlaenge)
    t.left(135)
    t.forward((wandlaenge ** 2 + wandlaenge ** 2) ** 0.5)
    t.left(45)
    t.backward(wandlaenge/2)
    t.color(1, 1, 1)


def forward_no_mark(len):
    t.penup()
    t.forward(len)
    t.pendown()


def draw_street(t_direction='horizontal', size=400,
                x_origin=-200, y_origin=0, anzahl_haeuser=4):
    t.teleport(x_origin, y_origin)
    z_direction = 0
    if t_direction == 'horizontal':
        z_direction = 0
    else:
        z_direction = 90
    t.setheading(z_direction)
    t.pensize(5)
    t.forward(size)
    t.teleport(x_origin, y_origin)
    t.penup()
    t.right(90)
    t.forward(30)
    t.left(90)
    t.pendown()
    t.forward(size)
    t.teleport(x_origin, y_origin)
    t.pensize(1)
    abstand = int(size/(anzahl_haeuser+1))
    forward_no_mark(abstand)
    draw_house(r.randint(10, int(abstand/1.5)), t.xcor(), t.ycor(),
               z_direction)
    forward_no_mark(abstand)
    draw_house(r.randint(10, abstand), t.xcor(), t.ycor(), z_direction)
    forward_no_mark(abstand)
    draw_house(r.randint(10, abstand), t.xcor(), t.ycor(), z_direction)
    forward_no_mark(abstand)
    draw_house(r.randint(10, int(abstand/1.5)), t.xcor(), t.ycor(),
               z_direction)
    forward_no_mark(abstand)
    # return t.xcor(), t.ycor()


# r.randint(10, abstand)
def draw_block(street_length=400, x_start=-200, y_start=-200):
    draw_street('horizontal', street_length, x_start, y_start)
    draw_street('vertikal', street_length, x_start + street_length, y_start)
    draw_street('horizontal', street_length, x_start, y_start + 30
                + street_length)
    draw_street('vertikal', street_length, x_start - 30, y_start)


draw_block()
turtle.done()
