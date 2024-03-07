import time, sys
indent = 0 #starting at no indent, using this variable to create indents and lateral movement
indentIncreasing = True #determine the direction of the lateral movement. True going to the right, False going to the left.

try:
    while True:
        print(" "*indent, end="")
        print("********")
        time.sleep(0.1) #pause for 0.1 seconds

        if indentIncreasing:
            indent=indent+1
            if indent==20:  #check if we stop moving in any direction, limit set at 20 indents
                indentIncreasing=False
        
        else:
            indent=indent-1
            if indent==0:
                indentIncreasing=True

except KeyboardInterrupt:
    sys.exit()