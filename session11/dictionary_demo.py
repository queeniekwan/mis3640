names = ['sean', 'queenie', 'chris']
scores = [90, 100, 80]

def find_score(name, score):
    return score[name.index('chris')]

print(find_score(names, scores))

# how to create a dictionary
grades = dict()
# grades = {}

grades['queenie'] = 100
print(grades)

grades = {'sean':95, 'queenie':100, 'chris':90}

print(len(grades))
print(grades['chris'])
# dictionary doesn't have order

for name, grade in grades.items():
    print(f'{name} got {grade} in python class')

for name in grades.keys():
    print(name)

for grade in grades.values():
    print(grade)

print(100 in grades.values())
print('queenie' in grades.keys())
print('queenie' in grades) #just check the keys
print(100 in grades) #false

# get a value with a key, and any value if the key doesn't exist
print(grades.get('queenie'))
print(grades.get('ivy', 0))

# dictionary as a collection of counters
def histogram(s):
    d = {}
    
    for letter in s:
        # if letter not in d:
        #     d[letter] = 1
        # else:
        #     d[letter] += 1
        d[letter] = d.get(letter, 0) + 1

    return d

print(histogram('queenie'))



