print('Hello, world!')

# single or double quotation marks, escape \ backward slash
print()
print('don\'t')
print("don't")

print('1+2+3', 1+2+3)

# assigning input to the variable <name>
# name = input()
# print(name)

# string
print()
message = 'I did somthing cute today!'
print(message)
print('message')

# expression
'hello'
# statement
word = 'hello'

# dynamic variable
print()
name = 'hello'
print(type(name))
name = 123
print(type(name))

# string + and *
print()
first_name = 'Queenie'
last_name = 'Kwan'
print(first_name + ' ' + last_name)
print('stupid \t o \n' * 10) #\t tab, \n next line

# f - string formating
print()
name = 'Wing Q'
print('Hello, {}'.format(name)) # the old way
print(f'Hello, {name}') # the new way, use this :))
print(f'Hello, {first_name} {last_name}!')

# f - number formating
print()

pi = 3.1415926

print(f'Pi equals {pi:.5f}.') # 5f decimals (f - float number)
print(f'Pi equals {pi:.10f}.') # 10f decimals
print(f'Pi equals {pi:8.5f}.') # 8 spaces in total, 5f decimals
print(f'Pi equals {pi:8.2f}.') # 8 spaces in total, 2f decimals

# f - change number notation type
print()

year = 2020
print(f'{year}')
print(f'{year:b}') # b - binary
print(f'{year:x}') # x - hexadecimal
print(f'{year:o}') # x - octal
print(f'{year:e}') # x - scientific

# f - print location
print()

s1 = 'a'
s2 = 'ab'
s3 = 'abc'
s4 = 'abcd'

print(f'{s1:>10}') # to the most right of 10 spaces
print(f'{s2:>10}')
print(f'{s3:>10}')
print(f'{s4:>10}')



