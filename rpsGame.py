#coding a Rock, Paper & Scissors game for Chapter 2
import random, sys

wins=0
loss=0
ties=0
letters_dict={'r':'ROCK','p':'PAPER','s':'SCISSORS'}
phrase=", ".join(letters_dict.values())
print(phrase)

while True:
    print(str(wins)+" wins, "+str(loss)+" losses, "+str(ties)+" ties.")
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    response=input()
    if response.lower()=="q":
        sys.exit()
    elif response.lower()=="r" or "p" or "s":
        print("ok")
        #versus=random.choice(letters)
        #if response.lower()=="r":
            #print("ROCK versus...")
            #print()
    else:
        print("This is not a valid choice.")
