game_round_count = 1

while True:
    print(f"\nGame Round: {game_round_count}")

    secret_word = "None"
    hint = "Hint: It's a word that means nothing or zero."

    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    print(hint)  # Show the hint once per round

    while guess != secret_word and not out_of_guesses:
        if guess_count < guess_limit:
            remaining_attempts = guess_limit - guess_count
            print(f"Remaining attempts: {remaining_attempts}")
            guess = input("Enter a Guess: ")
            guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("Out of guesses, YOU LOSE !!!")
    else:
        print("You Win!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break

    game_round_count += 1
