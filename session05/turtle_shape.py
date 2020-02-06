import turtle
import math

def polyline(t, n, length, angle):
    """
    Draws n line segments with given length and angle (in degrees) between them.
    t is a turtle.
    """
    for _ in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, length, n):
    """
    Draws a n-sided polygon with given length
    t is a turtle
    """
    angle = 360 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    """
    Draws an arc with radius r and angle
    t is a turtle
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length/3) + 1
    step_length = arc_length / n
    step_angle = angle / n 
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    """
    Draws a circle with radius r
    t is a turtle
    """
    arc(t, r, 360)

def move(t, x, y):
    """
    Moves Turtle (t) to (x,y) without leaving a trail
    Leaves the pen down
    """
    t.pu()
    t.setpos(x, y)
    t.pd()
    