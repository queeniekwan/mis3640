# Tuples are immutable
# to create a tuple variable with only one element, close the statement with a ','

t = 'a',
print(t)

a = tuple('Babson')
print(a)

b = tuple([1, 2, 3])
print(b)

# to modify tuple
b = (0, ) + b[:]
print(b)

# using tuple to swap values of two variables
x = 10
y = 90
x, y = y, x 
print(x, y)

# using tuple to split a string and store elements in variables
email = 'yguan3@babson.edu'
id, domain = email.split('@')
print(f'id: {id}; domain: {domain}')

tel = '508-333-0452'
area, _, local = tel.split('-')
print(area)
print(local)

# Tuples as reurn values
t = divmod(7, 3) 
print(t)

def f():
    return 1, 2

type(f()) # is a tuple
a, b = f()
print(a)
print(b)

# Variable-length argument tuples
def sumall(*nums):
    result = 0
    for num in nums:
        result += num
    return result

print(sumall(1))
print(sumall(1, 2, 3))

def multall(*nums):
    result = 1
    for num in nums:
        result = result * num
    return result

print(multall(2, 3, 4, 5))


