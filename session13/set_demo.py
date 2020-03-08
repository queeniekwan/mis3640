def unique_letters(word):
    unique_letters = []
    for letter in word:
        if letter not in unique_letters:
            unique_letters.append(letter)

    return unique_letters

print(unique_letters('bookkeeper'))

# set is a function and type that returns unique elements in an item
word = 'bookkeeper'
s = set(word)
print(s, type(s))
s.add('a')
print(s)

# intersection between two sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2) #intersection
print(s1 | s2) #union
print(s1.difference(s2)) #what's in s1 that s2 doesn't have



