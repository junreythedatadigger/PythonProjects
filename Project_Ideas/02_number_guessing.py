# Number Guessing Game
# Develop a game where the program randomly selects a number, and the user has
# to guess it. Provide feedback if the guess is too high or too low. This project helps
# you understand loops and conditional statements.

from random import randrange
random_number = randrange(1,100)
guess_number = 0
while guess_number != random_number:
    guess_number = int(input("Enter your guessed number: "))

    if guess_number > random_number:
        print('You guessed a higher number\n')

    elif guess_number < random_number:
        print('You guessed a lower number\n')

print(f'{guess_number} is the random number')