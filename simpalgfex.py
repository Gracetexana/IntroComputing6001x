# The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

low = 0
high = 100
x = ""

print("Please think of a number between 0 and 100!")

while (x != "c" and x != "C"):
    half = (low + high) // 2
    print("Is your secret number " + str(half) + "?")
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if x == "l" or x =="L":
        low = half
    elif x == "h" or x == "H":
        high = half
    elif x == "c" or x == "C":
        break
    else:
        print("Sorry, I did not understand your input.")

print("Game over. Your secret number was: " + str(half))