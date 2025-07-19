import random
from words import word_list  # Make sure this file exists and contains a list called word_list

def hangman():
    word = random.choice(word_list)
    guessed_letters = []
    tries = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while tries > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            tries -= 1
            print(f"Wrong guess! Tries left: {tries}")

        # Show guessed letters
        print("\nUsed Letters:", " ".join(guessed_letters))

        # Display word progress
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(display_word.strip())

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word 🎉")
            break
    else:
        print(f"Game Over! The word was '{word}'.")

hangman()
