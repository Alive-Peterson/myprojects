import random

def guess_comp(x):

    low=1
    high=x
    feedback=''
    guess=None
    print(f"Think of a number between{low} & {high} and the computer will guess it !")
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low

        feedback=input(f"is the number {guess} too low (l),too high(h) and correct(c):")
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
        elif feedback!='c':
            print("Enter only h,l and c")


    print(f"Yay, the computer guessed your number correctly! {guess}")

guess_comp(5)





