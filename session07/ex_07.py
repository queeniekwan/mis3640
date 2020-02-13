from math import sqrt
from tabulate import tabulate

def mysqrt(a):
    x = a / 2
    while True:
        y = (x + a/x) / 2
        if x == y:
            break
        x = y
    return x

def test_square_root(min, max):
    results = [(a, mysqrt(a), sqrt(a), abs(sqrt(a) - mysqrt(a))) for a in range(min,max)]
    print(tabulate(results, headers=['a', 'mysqrt(a)', 'math.sqrt(a)', 'diff'], numalign='left'))

    print(f"{'a':3} {'mysqrt(a)':14} {'math.sqrt(a)':14} {'diff':14}")
    print(f"{'-'*3:3} {'-'*14:14} {'-'*14:14} {'-'*14:14}")
    
    for a in range(min, max):
        print(f"{a:<3.1f} {mysqrt(a):<14.10f} {sqrt(a):<14.10f} {abs(sqrt(a)-mysqrt(a)):<14.10f}")

def main():
    # print(mysqrt(9))
    test_square_root(1, 10)

if __name__ == "__main__":
    main()
