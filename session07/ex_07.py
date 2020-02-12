from math import sqrt
from tabulate import tabulate

def mysqrt(a):
    x = a / 2
    while True:
        y = (x + a / x) / 2
        if x == y:
            break
        x = y
    return x

def test_square_root():
    results = [(a, mysqrt(a), sqrt(a), sqrt(a) - mysqrt(a)) for a in range(1,10)]
    print(tabulate(results, headers=['a', 'mysqrt(a)', 'math.sqrt(a)', 'diff'], numalign='left'))


def main():
    # print(mysqrt(9))
    test_square_root()

if __name__ == "__main__":
    main()
