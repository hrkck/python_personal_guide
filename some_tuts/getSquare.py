
# My super busy function:
def makeMeLookLikeBusy():
    import time
    time.sleep(0.1)
    print("EXITING....")

n = 0
mistakes = 0

print("ENTERING THE 'WHILE' LOOP. TYPE 'break' TO END THE PROGRAM CUV UCV UVCCCVVV")
print()
print()
print()

while(True):
    try:
        myInput = input("enter a number: ")
        n = int(myInput) # Typecasting to Integer! # It is bug-prone
        # Must be treated with exception handling
    except ValueError:
        if(myInput == "break"): # True or False: a Boolean value. Bool
            print("'BREAK' is entered. Terminating the program in user' wish.")
            for i in range(20):
                makeMeLookLikeBusy()
            break

        mistakes = mistakes + 1
        if(mistakes < 3):
            print("Dude you entered a non-numeric value. Please enter a NUMBER.")
            continue
        if(mistakes >= 3):
            print("Dude, you ve written it three times wrong. My grandies write better you. GETAOUT.")
            break

    b = n * n
    
    print(b)



print("Softare terminated itself. Error code 0")
