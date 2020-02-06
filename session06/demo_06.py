# age = int(input('Please enter your age >> '))
age = 18

if age >= 18:
    print(f'Your age is {age}.')
    print('You are an adult')
elif age >= 12:
    print('You are a teenager')
else:
    print('You are a kid')


x = 1
y = 2

""" Nested conditional statement """
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

""" functions same as above """
""" Chained conditional statement """
if x == y:
    print('x and y are equal')
elif x < y:
    print('x is less than y')
else:
    print('x is greater than y')


def BMI_Calculator (height, weight):
    """ 
    calculates BMI based on weight (kg) and height (m), entered by user, and prints the catagory
    """
    # height = float(input('Enter your height (m) >> '))
    # weight = float(input('Enter your wight (kg) >> '))
    BMI = weight / height ** 2
    print(f'Your BMI is {BMI:.2f}')
    if BMI <= 18.5:
        print('Underweight')
    elif BMI <= 24.9:
        print('Normal weight')
    elif BMI <= 29.9:
        print('Overweight')
    else:
        print('Obesity')

def compare (a, b):
    """
    """
    if isinstance(a, str) or isinstance(b, str):
        print('string involved')
    else:
        if a > b:
            print('bigger')
        elif a == b:
            print('equal')
        else:
            print('smaller')

def diff21(n):
    """
    Given an int n, return the absolute difference between n and 21, 
    except return double the absolute difference if n is over 21.
    """
    if n <= 21:
        return 21 - n
    else:
        return 2 * (n - 21)

def cigar_party(cigars, is_weekend):
    """
    When squirrels get together for a party, they like to have cigars. 
    A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. 
    Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
    Return True if the party with the given values is successful, or False otherwise.
    """
    if is_weekend and cigars >= 40:
        return True
    else:
        if 40 <= cigars <= 60:
            return True
        else:
            return False

""" Recursive function: a function that calls itself within the function """
def countdown(n):
    import time
    time.sleep(1)

    if n <= 0:
        print('Blastoff!!')
    else:
        print(n)
        countdown(n-1)

def fibonacci(n):
    """
    return the nth fibonacci number
    """
    if n ==1 or n ==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)



def main():
    # BMI_Calculator(1.63, 47)
    # compare(3, 4)
    # compare('a', 'b')
    # compare(2, 1)
    # print(diff21(19))
    # print(diff21(21))
    # print(diff21(23))
    # print(cigar_party(30, False))
    # print(cigar_party(50, False))
    # print(cigar_party(70, True))
    # countdown(5)
    print(fibonacci(1))
    print(fibonacci(3))
    print(fibonacci(10))


if __name__ == "__main__":
    main()


