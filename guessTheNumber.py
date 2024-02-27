#example project to try to get a user to guess the number
import random, sys

print("I am thinking of a number between 1 and 20.")
number=random.randint(1,20)
#print(number)   #comment this later, used to view number.
counter=0
#Note: would like to add a feature to give a maximum amount of guesses.
while True:
    print("Take a guess.")
    guess=int(input())
    
    if guess==number:
        print("Good job! You guessed my number in "+str(counter+1)+" guesses!")
        sys.exit()  #could of just used "break" and not even need to import "sys" I believe? Whatever.
    else:
        counter=counter+1
        if counter==5:
            print("Nope. The number was "+str(number)+".")
            sys.exit()  #break would work here instead, no?
        elif guess>number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")





