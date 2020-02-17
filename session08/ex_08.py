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
    #     if letter == ' ':
    #         continue
    #     else:
        price += (ord(letter) - 96)
    return price

def receipt():
    item_list = ['bananas', 'rice', 'paprika', 'potato chips']
    total_price =  0
    for item in item_list:
        print(f'{item} ${item_price(item)}')
        total_price += item_price(item)
    print('-' * 20)
    print(f'Total ${total_price}')


def main():
    # guess_game_whileloop()
    # guess_game_forloop()
    print(count('queenie', 'e'))
    print(item_price('potato chips'))
    receipt()


if __name__ == '__main__':
    main()