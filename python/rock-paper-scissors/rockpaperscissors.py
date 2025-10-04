import random

def play_game():
    choices = ["R", "P", "S"]

    while True:
        player1 = input("Enter your choice - rock(R), paper(P), or scissors(S): ").upper()
        if player1 not in choices:
            print("Invalid Input")
            continue

        player2 = random.choice(choices)

        if player1 == player2:
            print("It's a Tie")
        elif (player1 == "R" and player2 == "S") \
            or (player1 == "S" and player2 == "P") \
            or (player1 == "P" and player2 == "R"):
            print(f"Player 1 chose {player1} and Player 2 chose {player2}, Player 1 wins!!")
        else:
            print(f"Player 1 chose {player1} and Player 2 chose {player2}, so Player 2 wins!!")

        play_again = input("Do you want to play again? yes/no (y/n): ")
        if play_again.lower()!= 'y':
            break

play_game()



