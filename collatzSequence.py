import sys, time 
# 20204/03/19 - trying to add 'try' and 'except' statements to detect if user inputs a non-integer.
# note: does the collatzSequence work with decimals?? My code certainly doesnt.
# note2: will my second while loop still work with decimals?? Nope.

def collatz(number):
    if number%2==1: #if number is odd, 3*number+1
        number=3*number+1
    else:   #if number is not odd, number//2
        number=number//2
    print(number)
    return number

while True:
    print("Enter number:")
    user_input=input()

    try:
        #only work if user_input will be an int
        number=int(user_input)
        break #exit the loop
    except ValueError:
        print("That is not a valid number.")

while number!=1:
    new_number=collatz(number)
    time.sleep(0.1) #pause for 0.1 seconds
    number=new_number