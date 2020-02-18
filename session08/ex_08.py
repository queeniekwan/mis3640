import random

""" guess game using while loop"""
def guess_game_whileloop():
    guess_taken = 0

    name = input('Hello! What is your name?')

    number = random.randint(1,20)
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')

    while guess_taken < 6:
        print('Take a guess.')
        guess = int(input())

        guess_taken += 1

        if guess < number:
            print('Your guess is too low')
        if guess > number:
            print('Your guess is too high')
        if guess == number:
            print(f'Good job, {name}! You guessed my number in {guess_taken} guesses!')
            break

    if guess!= number:
        print(f'Nope. The number I was thinking of was {number}')


""" guess game using for loop """
def guess_game_forloop():
    name = input('Hello! What is your name?')

    number = random.randint(1,20)
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')

    for i in range(6):
        print('Take a guess')
        guess = int(input())

        if guess < number:
            print('Your guess is too low')
        if guess > number:
            print('Your guess is too high')
        if guess == number:
            print(f'Good job, {name}! You guessed my number in {i+1} guesses!')
            break

    if guess!= number:
        print(f'Nope. The number I was thinking of was {number}')


""" String Excercise """

# Looping and Counting / Exercise  2
def count(string, letter):
    count = 0
    for a in string:
        if a == letter:
            count += 1
    return count

# Exercise 4
def item_price(item):
    price = 0
    for letter in item:
        if letter == ' ':
            continue
        else:
            price += (ord(letter) - 96)
    return price

def receipt():
    item_list = ['bananas', 'rice', 'paprika','potato chips','pussy kitty doggo']
    total_price =  0
    width = 0
    money_symbol = '$'
    for item in item_list:
        if len(item) > width:
            width = len(item)

    for item in item_list:
        print(f'{item} {money_symbol:>{width+10-len(item)-len(str(item_price(item)))}}{item_price(item):.2f}')
        total_price += item_price(item)
    
    print('-' * (width+15))
    print(f'Total {money_symbol:>{width+10-5-len(str(total_price))}}{total_price:.2f}')

# Exercise 5
def any_lowercase(s):
    """
    Checks if the first letter in string s is lowercase. Ture if yes, False if not
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    """
    Returns 'Ture' all the time since 'c' is a lowercase
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    """
    Checks if the last letter in string s is lowercase. True if yes, False if not
    """
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """
    Returns True if at least one letter in string s is lowercase, False if all letters are uppercase
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """
    Returns False if at least one letter in string s is uppercase, True if all letters are lowercase
    """
    for c in s:
        if not c.islower():
            return False
    return True

# Exercise 6
def rotate_word(s,i):
    """
    Rotate the word s (string) by i (integer) position
    """
    new_string = ''
    for letter in s:
        new_string += chr(ord(letter)+i)
    return new_string

def main():
    # guess_game_whileloop()
    # guess_game_forloop()
    # print(count('queenie', 'e'))
    # print(item_price('potato chips'))
    # receipt()
    # print(any_lowercase5('aaA'))
    print(rotate_word('IBM',-1))


if __name__ == '__main__':
    main()