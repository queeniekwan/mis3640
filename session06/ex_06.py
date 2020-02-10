def factorial(n):
    """
    return the factorial number for integer n 
    """
    if isinstance(n, int):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    else:
        return 'Please enter an integer'

def fibonacci(n):
    """
    return the nth fibonacci number
    """
    if n ==1 or n ==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def gcd(x1, x2):
    """
    returns the greatest common divisor of two positive integers x1 and x2
    """
    if isinstance(x1, int) and isinstance(x2, int) and x1 > 0 and x2 > 0:
        a = max(x1, x2)
        b = min(x1, x2)
        r = a % b
        if r == 0:
            return b
        else:
            return gcd(b, r)
    else:
        return 'Please enter two positive integers'

def move(n, source, bridge, destination):
    if n == 3:
        return (f'{source} --> {destination}\n'
            f'{source} --> {bridge}\n'
            f'{destination} --> {bridge}\n'
            f'{source} --> {destination}\n'
            f'{bridge} --> {source}\n'
            f'{bridge} --> {destination}\n'
            f'{source} --> {destination}\n')
    else:
        return (move(n-1, source, destination, bridge) + 
            f'{source} --> {destination}\n' +
            move(n-1, bridge, source, destination))
        

def main():
    # print(factorial(0))
    # print(factorial('6'))
    # print(factorial(6))
    # print(fibonacci(4))
    # print(gcd(1071, 462))
    # print(gcd(12, 6))
    # print(gcd(12, 9))
    # print(gcd(-4, '5'))
    # print(move(3, 'a', 'b', 'c'))
    print(move(4, 'a', 'b', 'c'))


if __name__ == "__main__":
    main()