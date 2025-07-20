import random

def guess_num(x):
    random_num=random.randint(1,x)
    guess=0
    while guess!=random_num:
        guess=int(input(f"Enter a num between 1 and {x}:"))
        if guess<random_num:
            print("Sorry,the number is too low")
        elif guess>random_num:
            print("Sorry, the number is too high")

    print("Yay! you guessed it correct")

guess_num(4)