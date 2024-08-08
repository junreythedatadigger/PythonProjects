from random_word import RandomWords
r = RandomWords()

from PyDictionary import PyDictionary
dictionary=PyDictionary()

import random
import json

def load_words(filename):
    try:
        with open(filename, 'r') as file:
            words_json = json.load(file)
    except FileNotFoundError:
        words_json = {}
    return words_json


def validate_guess(random_word, incomplete_word, guessed_letter):
    is_guess_correct = False
    # guessed_word = ""

    if incomplete_word:
        guessed_word = [i for i in incomplete_word]
    else:
        guessed_word = [i for i in print_blank_word(random_word)]

    for i in range(len(random_word)):
        if random_word[i].lower() == guessed_letter:
            guessed_word[i] = random_word[i]
            is_guess_correct = True

    return "".join(guessed_word), is_guess_correct


def print_blank_word(random_word):

    display_word = ""
    for i in random_word:
        if i != " ":
            display_word += "*"
        else:
            display_word += " "
    return display_word


def get_unique_letters(random_word):
    unique_letters = ""
    random_word_list = [i for i in random_word]
    random_word_list.sort()

    for i in random_word_list:
        if i not in unique_letters:
            unique_letters += i
    return unique_letters


def show_number_of_life(number):
    return "♡" * number


def show_remaining_letters(alphabet,letter):
    alphabet_list = [i for i in alphabet]
    for i, let in enumerate(alphabet_list):
        if let == letter:
            alphabet_list[i] = "_"
    return "".join(alphabet_list)


# def display_on_console(random_word, guessed_word, number_of_life, alphabet):
#     print(f"Try to guess this {len(get_unique_letters(random_word))} letter word.")
#     print(f"Word: {print_blank_word(random_word)}")
#     print(f"Life: {show_number_of_life(number_of_life)}")
#     print(f"Left: {show_remaining_letters(alphabet, "")}")


def main():
    number_of_life = 10
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # random_word = "Hello world!"
    filename = "words_list.json"
    words_dictionary = load_words(filename)
    # print(len(words_dictionary))
    word_from_dictionary = random.choice(words_dictionary)
    print(word_from_dictionary[0])
    # random_word = r.get_random_word()
    # random_word = word_from_dictionary[0]
    # display_on_console(random_word, number_of_life, alphabet)
    # print(random_word)
    # print(dictionary.meaning(random_word))
    print(f"Try to guess this {len(word_from_dictionary[0])} letter word.")
    print(f"Word: {print_blank_word(word_from_dictionary[0])}")
    print(f'Category: {word_from_dictionary[1]}')
    print(f'Definition: {word_from_dictionary[2]}')
    print(f"Life: ({number_of_life}) {show_number_of_life(number_of_life)}")
    print(f"Left: {show_remaining_letters(alphabet, "")}")
    guessed_word = ""
    typed_letters = ""
    letters_left = ""
    while word_from_dictionary[0] != guessed_word and number_of_life > 0:
        guessed_letter = input("Enter letter: ")
        typed_letters += guessed_letter
        guessed_word, is_correct = validate_guess(word_from_dictionary[0],guessed_word,guessed_letter)
        if is_correct == False:
            number_of_life -= 1
        print("")
        print(f"Try to guess this {len(word_from_dictionary[0])} letter word.")
        print(f"Word: {guessed_word}")
        print(f'Category: {word_from_dictionary[1]}')
        print(f'Definition: {word_from_dictionary[2]}')
        print(f"Life: ({number_of_life}) {show_number_of_life(number_of_life)}")
        letters_left = show_remaining_letters(alphabet, guessed_letter)
        print(f"Left: {letters_left}")
        alphabet = letters_left

    if word_from_dictionary[0] == guessed_word:
        print("")
        print(f"Congratulations! You got the word {guessed_word}.")
    elif number_of_life == 0:
        print("")
        print(f"Sorry, you did not get the word {word_from_dictionary[0]}.")

if __name__ == "__main__":
    main()