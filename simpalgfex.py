# The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

low = 0
high = 100
x = ""

print("Please think of a number between 0 and 100!")

# while computer has not guessed correctly
while (x != "c" and x != "C"):
    # bisection search-- start with halfway between low and high
    half = (low + high) // 2
    print("Is your secret number " + str(half) + "?")
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    # if guess is low...
    if x == "l" or x =="L":
        # ...change lower bound
        low = half
    
    # if guess is high...
    elif x == "h" or x == "H":
        # ...change upper bound
        high = half
    
    # if guess is correct...
    elif x == "c" or x == "C":
        # ...end loop
        break
    
    # if input is not a guess, ask again
    else:
        print("Sorry, I did not understand your input.")

print("Game over. Your secret number was: " + str(half))