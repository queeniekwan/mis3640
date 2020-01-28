name = 'Queenie'
score = 100
d = {'Ray': 90, 'Ivy': 98, name: score}

pi = 3.14e-2 # Scientific notation
print(type(pi)) # float

import math
import pprint
print(dir(math))
pprint.pprint(dir(math))
print(math.pi)
print(math.sqrt(85))

import random
print(random.random()) # returns a random number between 0 to 1
print(random.choice([1,2,3,4]))
print(random.choice(['Ray', 'Ivy', 'Chris', 'Queenie']))

"""
large block of comment
Boolean
"""
a = 3 > 4
print(a)
print(type(a))

print(True and True)
print(True and False)
print(False and False)
print(5 > 3 and 3 > 1)
print(5 > 3 and 3 < 1)
print(5 > 3 or 3 < 1)
print(not True)
print(not 2 < 1)
print(3 == 5)
print(4/2 == 4/2.0) #True, in python 3.0 it is True as long as the values are the same

# if statements using boolean 
age = input('What is your age?')
age = int(age) # because everything from input is a string, so we convert

if age >= 21:
    print('yes, you can drink')
else:
    print('sorry, you cant drink')







