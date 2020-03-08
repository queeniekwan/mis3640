# convert between different data structures
# string and list
s = 'queenie'
l = list(s)

college = 'Babson College'
college_list = college.split()
college_str = ''.join(college_list)

# list and dictionary
def list_to_dict(l):
    hist = {}
    for letter in l:
        hist[letter] = hist.get(letter, 0) + 1
    return hist

def dict_to_list(hist):
    new_list = []
    for letter, freq in hist.items():
        new_list.extend([letter] * freq)
    return new_list

# list and tuple
new_list = [1, 2, 3]
letter_tuple = (new_list, )
letter_tuple = tuple(new_list)
list_two = list(letter_tuple)

# list and set
newset = set(list_two)
list_three = list(newset)

# string and set
name = 'queenie'
name_set = set(name)
name_sort = sorted(set(name))

# string and dict
def string_to_dict(s):
    d = {}
    for letter in s:
        d[letter] = d.get(letter, 0) + 1
    return d

def dict_to_string(d):
    s = ''
    for letter, freq in d.items():
        s += letter * freq
    return s

# string and tuple
name = 'queenie'
t = tuple(name)
name = ''.join(t)

# tuple and set
t = tuple(name)
s = set(t)
unique_t = tuple(s)

# dict and tuple
d = {'a': 1, 'b': 2}
t = tuple(d.keys())
t = tuple(d.values())
t_pair = tuple(d.items())

# dict and set
s = set(d.keys())
s = set(d.values())
s_pair = set(d.items())

# string, list, and dict
s = 'abc'
a = [1, 2, 3]
d = dict(zip(s, a))

s = 'abc'
b = [1, 2]
d = dict(zip(s, a)) #will return a dict with 2 elements (take the short one)
