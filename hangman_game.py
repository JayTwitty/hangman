
### This is a Welcome Message that asks the user to enter their name and stores their name as a variable.

print("Welcome to the Mystery Word Game App!")
name = input("What is your name?")

### This is where the computer grabs the list of words and stores them in a variable called contents

with open("words.txt") as words_file:
    contents = words_file.readlines()

### This is where the computer chooses a random word from the contents
import random
guess_word = list(random.choice(contents).rstrip("\n"))
word_display = ["_" for char in guess_word]
used_characters = ""

counter = 0
print("\n")
print(guess_word)

turn_counter = 8
print(name + ", There are {} letters in the word, You have {} tries to guess the word correctly...".format(len(guess_word),turn_counter))
print("\n")

while True:
    print(word_display)
    guess = input("Guess a letter?")
    for character in guess_word:
        if character == guess:
            word_display[counter] = guess
            print("\n")
            print("That letter is in the word, You have {} more guesses".format(turn_counter))
        counter += 1



print(str(guess_word))