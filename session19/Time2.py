class Time:
    """ Represents the time of day. """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute 
        self.second = second

    def __str__(self):
        return f'{self.hour:02}:{self.minute:02}:{self.second:02}'

    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    # def print_time(self):
    #     print(f'{self.hour:02}:{self.minute:02}:{self.second:02}')
    
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

def int_to_time(seconds):
    t = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60) 
    return t

class Point:
    """ Represents a point in a 2 dimentional space """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x},{self.y})'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

def main():
    # start = Time()
    # start.hour = 9
    # start.minute = 45
    # start.second = 0
    start = Time(9, 45)
    duration = Time(1, 35)

    # Time.print_time(start)
    # start.print_time()
    print(start)
    print(start + duration)

    a = Point(2, 3)
    b = Point(1, 1)
    print(a)
    print(a+b)

if __name__ == "__main__":
    main()