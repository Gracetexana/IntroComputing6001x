# Hangman game
#

# -----------------------------------
# Start of helper code provided by course
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

# I created the code within this function, but I did not define the function; additionally, the docstring was provided
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i, l in enumerate(secretWord):
      if i is len(secretWord)-1 and l in lettersGuessed:
        return True
      elif l not in lettersGuessed:
        return False

# I created the code within this function, but I did not define the function; additionally, the docstring was provided
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ""
    for l in secretWord:
      if l in lettersGuessed:
        word += l
      else:
        word += "_ "
    return word

# I created the code within this function, but I did not define the function; additionally, the docstring was provided
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    from string import ascii_lowercase as alph
    for l in lettersGuessed:
      alph = alph.replace(l, "")
    return alph
 
# I created the code within this function, but I did not define the function; additionally, the docstring was provided
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 8
    lettersGuessed = []

    print("Welcome to the game of Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    while guesses >= 0:
      print("-------------")
      if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
        guesses = -1
      elif guesses == 0:
        print("Sorry, you ran out of guesses. The word was " + secretWord)
        guesses = -1
      else:
        print("You have " + str(guesses) + " guesses left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        x = input("Please guess a letter: ").lower()
        if x in lettersGuessed:
          print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        elif x in secretWord:
          lettersGuessed.append(x)
          print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        else:
          lettersGuessed.append(x)
          print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
          guesses -= 1

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
