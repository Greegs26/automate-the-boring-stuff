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


import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
