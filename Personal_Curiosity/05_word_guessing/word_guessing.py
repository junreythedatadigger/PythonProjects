from random_word import RandomWords
r = RandomWords()

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

# random_word = "Hello world!"
random_word = r.get_random_word()
print(f"{print_blank_word(random_word)}  : Length: {len(get_unique_letters(random_word))}")
guessed_word = ""
guessed_letter = ""
typed_letters = ""
while random_word != guessed_word:
    guessed_letter = input("Enter letter: ")
    typed_letters += guessed_letter
    guessed_word, is_correct = validate_guess(random_word,guessed_word,guessed_letter)
    print(guessed_word, typed_letters)