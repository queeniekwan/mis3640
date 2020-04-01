import math
import copy

class Point:
    '''Represents a point in 2D space
    attributes: x, y
    '''

class Rectangle:
    '''Represents a rectangle
    attributes: width, height, corner
    '''

class Circle():
    '''Represents a circle
    attributes: center, radius
    ''' 

def print_point(p):
    print(f'({p.x}, {p.y})')

def distance_between_points(p1, p2):
    return math.sqrt((p1.x  - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

def point_in_circle(p, c):
    '''
    returns True if p lies in or the boundary of the circle
    p is a Point, c is a Circle
    '''
    return distance_between_points(p, c.center) <= c.radius

def rect_in_circle(r, c):
    p = Point()
    p.x = r.corner.x + r.width
    p.y = r.corner.y + r.height
    return point_in_circle(r.corner, c) and point_in_circle(p, c)

def rect_circle_overlap(r, c):
    '''
    returns True if any of the corners of r fall inside c
    r is a Rectangle
    c is a Circle
    '''
    p1 = Point()
    p1.x = r.corner.x + r.width
    p1.y = r.corner.y
    p2 = Point()
    p2.x = r.corner.x
    p2.y = r.corner.y + r.height
    p3 = Point()
    p3.x = r.corner.x + r.width
    p3.y = r.corner.y + r.height

    return point_in_circle(p1, c) or point_in_circle(p2, c) or point_in_circle(p3, c) or point_in_circle(r.corner, c)

def rect_circle_overlap_2(r, c):
    '''
    returns True if any part of r overlap with c
    r is a Rectangle
    c is a Circle
    '''
    p = copy.copy(r.corner)
    for w in range(r.width):
        p.y = r.corner.y
        for h in range(r.height):
            if point_in_circle(p, c):
                return True
            p.y += 1
        p.x += 1
    return False

def main():
    p1 = Point()
    p1.x = 0
    p1.y = 0
    p2 = Point()
    p2.x = 3
    p2.y = 4

    print(distance_between_points(p1, p2))

    box = Rectangle()
    box.width = 100
    box.height = 200
    box.corner = Point()
    box.corner.x = 0
    box.corner.y = 0

    print_point(find_center(box))

    c = Circle()
    c.center = Point()
    c.center.x = 150
    c.center.y = 100
    c.radius = 75

    print(point_in_circle(p2, c))
    p3 = Point()
    p3.x = 150
    p3.y = 75
    print(point_in_circle(p3, c))

    print(rect_in_circle(box, c))
    r = Rectangle()
    r.corner = Point()
    r.corner.x = 0
    r.corner.y = 0
    r.width = 150
    r.height = 200
    print(rect_in_circle(r, c))

    print(rect_circle_overlap(r, c))
    print(rect_circle_overlap(box, c))
    print(rect_circle_overlap_2(box, c))


if __name__ == '__main__':
    main()