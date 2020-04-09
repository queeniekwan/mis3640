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

if __name__ == "__main__":
    main()