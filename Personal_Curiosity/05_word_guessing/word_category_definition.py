# Code generated by ChatGPT
# https://chatgpt.com/share/8bd5af13-9c0c-4568-89fd-e8758f2215e3

# Resources for using Universal Part-of-Speech (POS) Tag-set
# https://www.nltk.org/book/ch05.html
# https://griesshaber.pages.mi.hdm-stuttgart.de/nlp/03postagging/02PosTagging.html

import random
import nltk
from nltk.corpus import wordnet, brown

from random_word import RandomWords
r = RandomWords()

import json

import time

# Download necessary NLTK data files
# Execute once
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('punkt')

# For universal tag-set. Execute once
# nltk.download('brown')
# nltk.download('universal_tagset')
# nltk.download('wordnet')

# A list of random words
# words_list = [
#     'aberration', 'capricious', 'eclectic', 'gregarious', 'idiosyncratic',
#     'juxtapose', 'loquacious', 'nefarious', 'quixotic', 'recalcitrant',
#     'serendipity', 'ubiquitous', 'vicarious', 'zealous', 'ameliorate'
# ]

def load_words(filename):
    try:
        with open(filename, 'r') as file:
            words_json = json.load(file)
    except FileNotFoundError:
        words_json = {}
    return words_json


def save_words(save_file, words_list):
    with open(save_file, 'w') as file:
        json.dump(words_list, file)


def get_random_word():
    # return random.choice(words)
    return r.get_random_word()

def get_part_of_speech(word):
    tokens = nltk.word_tokenize(word)
    # pos_tagged = nltk.pos_tag(tokens)
    pos_tagged = brown.tagged_sents(tagset="universal")
    return pos_tagged[0][1][1].capitalize()
    # return pos_tagged


def get_definition(word):
    synsets = wordnet.synsets(word)
    if synsets:
        return synsets[0].definition()
    return "Definition not found."


random_word = get_random_word()
part_of_speech = get_part_of_speech(random_word)
definition = get_definition(random_word)

print(f"Random Word: {random_word}")
print(f"Part of Speech: {part_of_speech}")
print(f"Definition: {definition}")

filename = "words.json"
save_file = "words_list.json"
words = load_words(filename)
words_key = list(words.keys())
words_list = []
print(len(words_key))
for i in range(len(words_key)):
# for i in range(50):
    description = get_definition(words_key[i])
    if description != "Definition not found.":
        # print(f"{words_key[i]}: {get_part_of_speech(words_key[i])}:  {get_definition(words_key[i])}")
        words_list.append([words_key[i], get_part_of_speech(words_key[i]), get_definition(words_key[i])])
    if i % 1000 == 0:
        obj = time.localtime()
        t = time.asctime(obj)
        print(f"i = {i}   Timestamp: {t}")

save_words(save_file, words_list)

print("Done")