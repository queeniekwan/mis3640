def absolute_value (x):
    if x < 0:
        x = -x
        print(x)
    else:
        print(x)
    
# absolute_value(-3)
# absolute_value(0)
# absolute_value(9)

def print_twice(whatever):
    print(whatever)
    print(whatever)

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

# cat_twice('Babson', 'College')
# print(cat) -- will be an error cuz 'cat' is not defined, variables inside function is local

# cat_twice(1, 2)
# cat_twice('1', '2')

def give_me_a_break():
    str1 = 'break'
    return str1

# give_me_a_break()
# print(give_me_a_break())

def give_me_two_breaks():
    str1 = 'break'
    return str1 # break the function, never gets to the next line
    # print('another break')

# print(give_me_two_breaks())

import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
