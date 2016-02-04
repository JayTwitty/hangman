
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
print(word_display)

print(name + ", There are {} letters in the word, You have {} tries to guess the word correctly...".format(len(guess_word), -int(counter) + 8))

while counter < 8:
    for character in guess_word:
        guess = input("Guess a letter?")
        if character == guess:
            word_display[counter] = guess
            print("That letter is in the word, You have {} more guesses".format(counter))
            guess = input("Guess another letter?")
            print("You have {} guesses left".format(counter))
        else:
            counter += 1
            print("That letter is Not in the word")
            guess = input("Guess another letter")


print(str(guess_word))