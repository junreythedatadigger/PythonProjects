def check_guess(random_word, guessed_letter):

    indexes = []
    for i in range(len(random_word)):
        if random_word[i].lower() == guessed_letter:
            indexes.append(i)

    return indexes

def print_blank_word(random_word):
    display_word = "*" * len(random_word)
    return display_word

