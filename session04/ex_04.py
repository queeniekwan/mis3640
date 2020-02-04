# modify my_abs to return 
def absolute_value (x):
    if x < 0:
        a = -x
    else:
        a = x
    return a

# print(absolute_value(3))

# Modify the function my_abs to first only allow integers and floating numbers
def absolute_value_number (x):
    """
    x: an integer or a floating number
    return the absolute value of a number
    """
    if isinstance(x, (int,float)) == True:
        if x < 0:
            return -x
        else:
            return x
    else:
        return 'enter numbers only'
 
# print(absolute_value_number('a'))
# print(absolute_value_number(-5.5))
# print(absolute_value_number(-5))


# Define a function quadratic(a, b, c) to solve a quadratic equation: ax^2 + bx + c = 0
def quadratic(a, b, c):
    if (isinstance(a, (int,float)) and
        isinstance(b, (int,float)) and
        isinstance(c, (int,float))) == True:
            x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
            x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
            return x1, x2
    else:
        return 'a, b, c should be numbers'

# print(quadratic(1, -6, -16))
# print(quadratic('a', 'b', 'c'))
