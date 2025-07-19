game_round_count = 1

while True:
    print(f"\n Game Round : {game_round_count} ")

    secret_word = "None"
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    while guess != secret_word and not out_of_guesses:
        if guess_count < guess_limit:
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
