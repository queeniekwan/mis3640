"""
built-in functions that take string(s) as a parameter:
input()
print()
int()/float()/bool()
type()
help()
len()

"""

team = 'New England Patriots'
print(team[1])
print(team[0])
# print(team[1.5]) string indices must be integers
print(len(team))
print(team[len(team)-1])
print(team[-1]) # count from the last

# Traversal - processing a string one character at a time
index = 0
while index < len(team):
    letter = team[index]
    print(letter)
    index += 1
# same as above, easier way
for letter in team:
    print(letter)

# Print names of ducks
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    # if letter == 'O' or letter =='Q':
    if letter in 'OQ':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)

# String slicing
team = 'New England Patriots'
print(team[0:11]) # starts at 0 and stops at 10 (before 11)
print(team[:11]) # same as above
print(team[12:20])
print(team[12:]) # same as above
# the whole string 
print(team[0:20])
print(team[:]) 
# the whole string with a step size of 2
print(team[::2]) 
# reverse of the whole string
print(team[::-1]) 


# Strings are immutable - we can't change the partial content in existed strings
# doesn't work
# team[12:20] = 'Seahawks'
new_team = team[:12] + 'Seahawks'
print(new_team)
print(team)

# Search - traversing a sequence and returning when we find what we are looking for
def find(word, letter):
    for i, c in enumerate(word): # i = index; c = item
        if c == letter:
            return i
    return -1

print(find(team, 'E'))
print(find(team, 'z'))






