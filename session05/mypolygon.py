import turtle
import math

# print(andrew)

# draw a square
# for i in range(4):
#     andrew.fd(100)
#     andrew.lt(90)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polyline(t, n, length, angle):
    """
    Draws n line segments with given length and angle (in degrees) between them.
    t is a turtle.
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, length, n):
    """
    Draws a n-sided polygon with given length
    t is a turtle
    """
    angle = 360 / n
    polyline(t, n, length, angle)

# def circle(t, r):
#     c = 2 * math.pi * r
#     length = c / 60
#     polygon(t,length,60)

# circle(andrew,100)

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


def main():
    # andrew = turtle.Turtle()
    # square(andrew,200)
    # polyline(andrew, n = 4, length = 50, angle = 60)
    # polygon(andrew, length = 50, n = 6)
    # arc(andrew, r = 100, angle = 360)
    # circle(andrew, n = 100)
    turtle.mainloop()
    
if __name__ == "__main__":
    main()

