
### This is a Welcome Message that asks the user to enter their name and stores their name as a variable.

while True:
    print('')
    print("Welcome to the Mystery Word Game App!")
    print('')
    start = input("Press 'enter/return' to START, or enter 'Q' to QUIT... ")
    if start.lower() == 'q':
        print("Goodbye!")
        break
    print('')
    name = input("What is your name? ")

### This is where the computer grabs the list of words and stores them in a variable called contents

    with open("words.txt") as words_file:
        contents = words_file.readlines()

### This is where the computer chooses a random word from the contents. I also made two empty lists to hold each bad or correct letters guessed

    import random
    word_to_guess = random.choice(contents).rstrip("\n")
    bad_guess_letters = []
    good_guess_letters = []

### This is the beginning of the game where we set the logic of how the game will continue until the end
### The number of bad guesses is limited to 8

    while len(bad_guess_letters) < 8 and len(good_guess_letters) != len(list(word_to_guess)):

### Drawing guessed letters, spaces, and turns to show the game board

        #print("The Secret Word to guess is...{} ".format(word_to_guess))
        print("The Secret Word to guess is... ")
        for letter in word_to_guess:
            if letter in good_guess_letters:
                print(letter, end='')
            else:
                print('_ ', end='')

### Message letting the user know how many letters are in the word and how many turns they have left.

        print('\n')
        print("{}, there are a Total of {} letters in the word".format(name, len(list(word_to_guess))))
        print('You have used {} of 8 turns. Only {} more left'.format(len(bad_guess_letters), 8 - len(bad_guess_letters)))
        print('')

### Take the user's guess

        print("_______________")
        guess = input("Guess a letter: ").lower()
        print("_______________")
        print("\n")

### Error messages if user inputs a number, more than one letter, or a letter that has already been used.

        if len(guess) != 1:
            print("{}, you can only guess one letter at a time!".format(name))
        elif len(guess) == 0:
            print("You did not enter a letter... Try again")
        elif guess in bad_guess_letters or guess in good_guess_letters:
            print("{}, that letter has already been used or guessed incorrectly!".format(name))
        elif not guess.isalpha():
            print("{}, you can only guess a letter!".format(name))
            continue

### If the user enters letters that are in the word they are guessing

        if guess in word_to_guess:
            good_guess_letters.append(guess)
            print("Great Job... That letter is in the word. See below and keep going...")
            if len(good_guess_letters) == len(list(word_to_guess)):
                print("Congratulations... You win! The word is {}!".format(word_to_guess))
                break

### If the user enters letters that are not in the word they are guessing

        else:
            bad_guess_letters.append(guess)
            print("The letter(s) {} is NOT in the word... Try again!".format(bad_guess_letters))

### If the while loop ends because the user has used up their 8 turns
    else:
        print("You are out of turns! The word was '{}'. Game Over!".format(word_to_guess))
        break