# Excercise 1 - index of list
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']    
]

print(len(L)) # 3
print(L[0][0]) # Apple
print(L[1][2][1]) # On Rail
print(L[1][2][1][2]) # the space "" in "On Rail"
print(L[-1][-1]) # Lisa

# Traversing a list
AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Giants']

for team in AFC_east:
    print(team)

numbers = [2, 0, 1, 6, 9]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)

# doesn't work as the following
# for number in numbers:
#     number = number * 2 

# print(numbers)

# make a copy
numbers_2 = numbers[:]
# numbers_2 = numbers # this is wrong, nothing will assign to numbers_2 
print(numbers_2)
numbers_2 == numbers # True
numbers_2 is numbers # False

# How to create another list from an existing list and perform calculation
for i, number in enumerate(numbers):
    print(i, number)
    numbers_2[i] = number / 2

print(numbers_2)

# Addition of list is like addition of string - concatinate 
a = [1, 2]
b = [3, 4]
c = a + b
print(c)
print(a * 4)

# to perform element level addition
d = []
for i, number in enumerate(a):
    d.append(number + b[i])
print(d)

# or we can use numpy


# built-in functions
a = [1]

# Append - Add an item to the end of the list
a.append('append')
print(a)

# Extend - Extend the list by appending all the items from the iterable.
a.extend([2, 3])
print(a)
a.extend('extend')
print(a)
a.extend(['extend'])
print(a)

# Insert - Insert an item at a given position. 
# The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list
a.insert(0, 0)
print(a)
a.insert(len(a), 'last')
print(a)
a.insert(0, [00, 000]) # will insert the ONE item as a list
print(a)

# Reverse - Reverse the elements of the list in place
a.reverse()
print(a)

# Sort - list.sort(key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
b = [3, 9, 4, 1, 0, 2, 5, 6, 8, 7]
b.sort()
print(b)
b.sort(reverse=True)
print(b)

name = ['ava', 'bella', 'jessica', 'david', 'cami']
name.sort(key=len) # sort by the length of each element in the list
print(name)

