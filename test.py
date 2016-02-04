with open("words.txt") as words_file:
    contents = words_file.readlines()

import random
guess_word = random.choice(contents).rstrip("\n")

for index, letter in enumerate(guess_word):
    enume_word = enumerate(guess_word)
    print(index, letter)
