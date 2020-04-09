class Point:
    """ Represents a point in a 2 dimentional space
    attributes: x, y
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x},{self.y})'

    # we overload a special method 
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

def main():
    a = Point(2, 3)
    b = Point(1, 1)
    print(a)
    print(a+b)
    print(a-b)

if __name__ == "__main__":
    main()