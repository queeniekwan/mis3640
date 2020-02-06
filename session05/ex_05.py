import turtle
import math
from turtle_shape import circle, arc, polygon, move

def circle_flower (t, r):
    """
    Draws a circle flower, t is a turtle, r is the radius of the circle
    """
    for _ in range(6):
        arc(t,r,60)
        t.lt(60)
        arc(t,r,120)
        t.lt(60)


def yinyang (t):
    """
    Draws a yinyang symbol, t is a turtle
    """
    # draws the outter circle
    circle(t,100)

    # draws the two arcr
    for _ in range(2):
        move(t,0,100)
        arc(t,50,180)

    # draws the two small circle
    move(t,0,35)
    circle(t,15)
    move(t,0,135)
    circle(t,15)

def circle_triangle (t, r):
    """
    Draws a pattern of circles within triangles within circle, 
    t is a turtle, r is the radius of the outter circle 
    """
    # draws the big circle
    circle(t,r)

    # draws the four triangles
    move(t,0,r)
    t.lt(60)
    for _ in range(4):
        t.lt(90)
        polygon(t,r,3)
    
    # calculations for small circles
    degree30 = math.radians(30)
    degree60 = math.radians(60)
    r_s = r / 2 / math.tan(degree60)
    height = r * math.cos(degree30)

    # draws the bottom small circle
    y1 = 100 - height
    move(t,0,y1)
    t.rt(60)
    circle(t,r_s)

    # draws the top small circle
    y2 = 100 + height
    move(t,0,y2)
    t.lt(180)
    circle(t,r_s)

    #draws the left small circle
    x1 = -height
    move(t, x1, r)
    t.lt(90)
    circle(t,r_s)

    # draws the right small circle
    x2 = height
    move(t,x2,r)
    t.lt(180)
    circle(t,r_s)

def main():
    t = turtle.Turtle()
    t.speed(0)
    circle_flower(t,100)
    # yinyang(t)
    # circle_triangle(t, 100)

    turtle.Screen().mainloop()

if __name__ == "__main__":
    main()