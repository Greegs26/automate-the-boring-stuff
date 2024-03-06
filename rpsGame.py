#coding a Rock, Paper & Scissors game for Chapter 2
import random, sys

wins=0
loss=0
ties=0
letters_dict={'r':'ROCK','p':'PAPER','s':'SCISSORS'}    #starting to regret this, not even needed. Will fix this later
phrase=", ".join(letters_dict.values())
print(phrase)

while True:
    print(str(wins)+" wins, "+str(loss)+" losses, "+str(ties)+" ties.")
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    user_input=input().lower()

    if user_input=="q":
        sys.exit()

    elif user_input in letters_dict:
        user_choice=letters_dict[user_input]
        print(user_choice+" versus...")

        random_key=random.choice(list(letters_dict.keys()))
        versus=letters_dict[random_key]
        print(versus)

        if user_choice==versus:
            print("It is a tie.")
            ties=ties+1
        elif (user_choice=="ROCK" and versus=="SCISSORS") or \
        (user_choice=="PAPER" and versus=="ROCK") or \
        (user_choice=="SCISSORS" and versus=="PAPER"):
            print("You win!")
            wins=wins+1
        else:
            print("You lose...")
            loss=loss+1

    else:
        print("This is not a valid choice.")
