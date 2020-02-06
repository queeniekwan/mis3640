import turtle
import math
from turtle_shape import circle, arc, polygon, move

def draw_two_circles(t):
    """
    Draws two circles. t is a turtle.
    """
    # large circle
    circle(t, 100)
    move(t, 100, 0)

    # another large circle
    circle(t, 100)

def circle_flower (t):
    """
    Draws a circle flower, t is a turtle
    """
    for _ in range(6):
        arc(t,100,60)
        t.lt(60)
        arc(t,100,120)
        t.lt(60)

def yinyang (t):
    """
    Draws a yinyang symbol, t is a turtle
    """
    circle(t,100)
    move(t,0,100)
    arc(t,50,180)
    move(t,0,100)
    arc(t,50,180)
    move(t,0,35)
    circle(t,15)
    move(t,0,135)
    circle(t,15)

def circle_triangle (t, r):
    """
    Draws a pattern of circles within triangles within circle, t is a turtle 
    """
    circle(t,r)
    move(t,0,r)
    t.lt(60)
    for _ in range(4):
        t.lt(90)
        polygon(t,r,3)
    t.rt(60)

    move(t,0,(100 - (r * math.cos(math.radians(30)))
    # r_small = r * abs(math.tan(60))
    # circle(t, r_small)
    
        
    

    
def main():
    t = turtle.Turtle()
    t.speed(0)
    # circle_flower(t)
    # yinyang(t)
    circle_triangle(t,100)
    turtle.Screen().mainloop()


if __name__ == "__main__":
    main()