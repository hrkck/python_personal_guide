import random
import time

currentEtherium = 1.0 # 1 ETH = 1 USD
dollarWallet = 100.0 # I have 100 USD in the first place
etheriumWallet = 10.0 # I got 10 ETH in the first place

while dollarWallet < 1000: # the goal is to reach 1000 USD

    # Amounts to invest:
    # I made up these first two number. It is an investment strategy  I chose. Could be something else.
    USD_ToSell = 10.0 # There is no particular reason why it is 10. See below.
    ETH_ToSell = 2 # There is no particular reason why it is '0.1'. See below.
    ETH_ToBuy = 0.0 # Because we haven't calculated yet. See below.
    USD_ToBuy = 0.0 # Because we haven't calculated yet. See below.

    # NOTE: I completely made up this math below:
    # I tried to imitate the change of the currency,
    # in the real economic world.
    # Basically,
    # At every step of "While" loop,
    # Etherium changes with a value between,
    # - 1.0, 1.0 (could be 0.3 or -0.7)
    # randomly...
    # Look up how 'random' package works on internet for details...
    randomNumber = random.randint(1.0, 10.0) / 10.0 # returns a value between 0.0, 1.0
    minusOrPlus = random.randint(-1, 1) # return either 0, 1 or -1
    changeOfEtherium = randomNumber * minusOrPlus # See?

    currentEtherium = currentEtherium + changeOfEtherium # Apply our calculation to the Etherium.

    if(currentEtherium <= 0): # If ETH goes below 0 USD. This can happen and we don't want this. It is not realistic.
        currentEtherium = 1 # Reset the value of ETH
        continue # Ignore rest of the loop and start again. You may want to look what 'continue' is on internet. Also check what "break" does.

    # NOTE: Now our pretty simple strategy to invest money comes:
    # Normally we ought to use highly complex finance strategies, I guess.
    # This code below responds to the immediate changes of ETH to constantly make money,
    # in this simple imitated economic world.
    if(currentEtherium < 0.5): # When ETH is cheap enough to BUY!
        if(dollarWallet >= 10): # When we have more than 10 USD
            dollarWallet = dollarWallet - USD_ToSell # we invested some USD.
            ETH_ToBuy =  USD_ToSell / currentEtherium # Makes sense right? ^^ .
            # Actually, I am not sure if this calculation is correct. I don't really know how economics work. But we can improve the code as we go through it in the future.
            etheriumWallet = etheriumWallet + ETH_ToBuy # now we have ETH
        if(dollarWallet < 10): # When we are running out of USD!
            USD_ToSell = dollarWallet # We will invest all the money!
            dollarWallet = dollarWallet - dollarWallet # we just invested all money we have! Now we have 0 USD!
            ETH_ToBuy = USD_ToSell / currentEtherium
            etheriumWallet = etheriumWallet + ETH_ToBuy # now we have ETH
        if(dollarWallet == 0):
            pass # We are miserable. Look up what is 'pass' keyword. It is basically "Do nothing"
    if(currentEtherium > 2.0): # When ETH is expensive enough to SELL!
        if(etheriumWallet >= 2):
            etheriumWallet = etheriumWallet - ETH_ToSell
            USD_ToBuy = currentEtherium * ETH_ToSell
            dollarWallet = dollarWallet + USD_ToBuy
        if(etheriumWallet < 2):
            ETH_ToSell = etheriumWallet
            etheriumWallet = etheriumWallet - etheriumWallet
            USD_ToBuy = currentEtherium * ETH_ToSell
            dollarWallet = dollarWallet + USD_ToBuy
        if(etheriumWallet == 0):
            pass

    # NOTE: Normally I would personally use 'functions' in the code above.
    # It would make everything far easier and more readable.
    # Once you get this, I will also share a version with 'functions' used.

    # NOTE: The below print statement might look little advanced.
    # The cool thing about it,
    # it prints our variables which are,
    # (currentEtherium, etheriumWallet, dollarWallet)
    # and it prints them all on the same line on terminal!
    # So we don't have hundreds of lines of printed sentences on our screen.
    # Comment below code and uncomment the other code and run, to see the difference.

    printString = "ETH currency: %.2f USD | Etherium Wallet: %.2f | Dollar Wallet: %.2f"
    print(printString  % (currentEtherium, etheriumWallet, dollarWallet), "\r" * len(printString), end='')
    # print(printString  % (currentEtherium, etheriumWallet, dollarWallet))

    time.sleep(0.3) # Computers are fast. So let's make the process intentionally slower.

print() # To print a new line
print("1000 USD Goal reached. Program ends.")
