"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

LJ
Cambio de color (rosa y morado)
<<<<<<< HEAD
agregar un circulo 

se hizo el circulo 
=======
agregar un circulo gato
....
>>>>>>> 0939f9888ebf46329ecdf6a9b7732f6e574bb848
#se agrego rectangulo y triangulo
"""

from turtle import *

from freegames import vector





def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def circulo (start, end):
    up()
    goto(start.x,start.y)
    down()
    begin_fill()
    r=45
    circle(r)
    end_fill()

def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def rectangle(start, end):
    up()
    goto(start.x,start.y)
    down()
    begin_fill()

    for i in range(2):
        forward(300)
        right(90)
        forward(150)
        right(90)
    end_fill()


def triangle(start, end):
    up()
    goto(start.x,start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        left(150)
    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value



state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('pink'), 'C')
onkey(lambda: color('purple'), 'P')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circulo), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
