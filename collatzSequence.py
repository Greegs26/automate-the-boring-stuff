import sys, time 

def collatz(number):
    if number%2==1: #if number is odd, 3*number+1
        number=3*number+1
    else:   #if number is not odd, number//2
        number=number//2
    print(number)
    return number

print("Enter number:")
user_input=int(input())

while user_input!=1:
    new_number=collatz(user_input)
    time.sleep(0.1) #pause for 0.1 seconds
    user_input=new_number