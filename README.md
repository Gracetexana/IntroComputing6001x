# Introduction to Computer Science and Programming Using Python

# [MITx 6.00.1x through edX](https://www.edx.org/course/introduction-to-computer-science-and-programming-7)

On my quest to become a data scientist, I enrolled in this course from August 25, 2022 to October 27, 2022. I learned much more than I expected; of course I learned and relearned some Python basics, but I also learned how to think computationally.  
Additionally, we also briefly covered the Python package, Pylab. After working on [my last repository](https://github.com/Gracetexana/Rosalind), I was hoping to learn a little bit more about Python packages, so I was pleased that we did in this course.

## Unit 1: Python Basics

#### Material Covered:  

1. Introduction to Python  
2. Core Elements of Programs  

#### [Problem Set 1](pset1):  

- [Problem 1](pset1/ps1a.py)  
  >Assume s is a string of lower case characters.  
  >Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.  
  >For example, if s = 'azcbobobegghakl', your program should print:  
  >\
  >**Number of vowels: 5**

- [Problem 2](pset1/ps1b.py)  
  >Assume s is a string of lower case characters.  
  >Write a program that prints the number of times the string 'bob' occurs in s.  
  >For example, if s = 'azcbobobegghakl', then your program should print:  
  >\
  >**Number of times bob occurs is: 2**

- [Problem 3](pset1/ps1c.py)  
  >Assume s is a string of lower case characters.  
  >Write a program that prints the longest substring of s in which the letters occur in alphabetical order.  
  >For example, if s = 'azcbobobegghakl', then your program should print:  
  >\
  >**Longest substring in alphabetical order is: beggh**  
  >\
  >In the case of ties, print the first substring.  
  >For example, if s = 'abcbcd', then your program should print:  
  >\
  >**Longest substring in alphabetical order is: abc**  
  


## Unit 2: Simple Programs
  
#### Material Covered:  

3. Simple Algorithms  

   - [Simple Algorithms "Finger Exercise"](simpalgfex.py)  
     >The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!  

4. Functions  

- [Complete Programming Experience: polysum](polysum.py)  
  >A regular polygon has n number of sides. Each side has length s.  
  >The area of a regular polygon is: $(0.25ns^2)/(tan(\pi/n))$  
  >The perimeter of a polygon is: length of the boundary of the polygon  
  >Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.

#### [Problem Set 2: Credit Card Payments](pset2)  

- [Problem 1 - Paying Debt Off in a Year; Minimum Monthly Payment](pset2/ps2a.py)  
  >Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.  
  >The following variables contain values as described below:  
  >- balance - the outstanding balance on the credit card  
  >- annualInterestRate - annual interest rate as a decimal  
  >- monthlyPaymentRate - minimum monthly payment rate as a decimal  
  >
  >\
  >For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy.


- [Problem 2 - Paying Debt Off in a Year; Fixed Payment](pset2/ps2b.py)  
  >Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.  
  >In this problem, we will not be dealing with a minimum monthly payment rate.  
  >The following variables contain values as described below:  
  >- balance - the outstanding balance on the credit card  
  >- annualInterestRate - annual interest rate as a decimal  
  >
  >\
  >The program should print out one line, the lowest monthly payment that will pay off all debt in under 1 year, for example:  
  >\
  >**Lowest Payment: 180**  
  >\
  >Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay.


- [Problem 3 - Using Bisection Search to Make the Program Faster](pset2/ps2c.py)  
  >You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates.  
Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!  
The following variables contain values as described below:  
  >- balance - the outstanding balance on the credit card  
  >- annualInterestRate - annual interest rate as a decimal  
  >
  >\
  >Write a program that uses bisection search to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year.  



## Unit 3: Structured Types

#### Material Covered:  

5. Tuples and Lists  
6. Dictionaries  

#### [Problem Set 3: Hangman](pset3)  

- Problem 1 - Is the Word Guessed
  >First, implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.
  
- Problem 2 - Getting the User's Guess
  >Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord.
  
- Problem 3 - Printing Out All Available Letters
  >Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.
  
- Problem 4 - The Game
  >Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

- [Completed Assignment](pset3/ps3_hangman.py)  
  


## Unit 4: Good Programming Practices

#### Material Covered:  

7. Testing and Debugging  
8. Exceptions and Assertions  

#### [Problem Set 4: Scrabble](pset4)  

- Scoring Rules
  - The score for the hand is the sum of the scores for each word formed.

  - The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all n letters are used on the first word created.

  - Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble letter value.

  - For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, then multiply by len('weed') to get (4+1+1+2)*4 = 32). Be sure to check that the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!

  - As another example, if n=7 and you make the word 'waybill' on the first try, it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105, plus an additional 50 point bonus for using all n letters).

- Problem 1 - Word Scores
  >The function getWordScore should accept as input a string of lowercase letters (a word) and return the integer score for that word, using the game's scoring rules.  
  
- Problem 2 - Dealing with Hands
  >The majority of this problem consists of learning how to read code, which is an incredibly useful and important skill.  
  >A hand is the set of letters held by a player during the game. The player is initially dealt a set of random letters. In our program, a hand will be represented as a dictionary: the keys are (lowercase) letters and the values are the number of times the particular letter is repeated in that hand.  
  >One useful function we've defined for you is getFrequencyDict, defined near the top of ps4a.py. When given a string of letters as an input, it returns a dictionary where the keys are letters and the values are the number of times that letter is represented in the input string.  
  >Given a hand represented as a dictionary, we want to display it in a user-friendly way. We have provided the implementation for this in the displayHand function.  
  >The hand a player is dealt is a set of letters chosen at random. We provide you with the implementation of a function that generates this random hand, dealHand. The function takes as input a positive integer n, and returns a new object, a hand containing n lowercase letters.  
  >The player starts with a hand, a set of letters. As the player spells out words, letters from this set are used up. Your task is to implement the function updateHand, which takes in two inputs - a hand and a word (string). updateHand uses letters from the hand to spell the word, and then returns a copy of the hand, containing only the letters remaining.  
  
- Problem 3 - Valid Words
  >A valid word is in the word list; and it is composed entirely of letters from the current hand. Implement the isValidWord function.  
  
- Problem 4 - Hand Length
  >Implement the helper calculateHandlen function.  
  
- Problem 5 - Playing a Hand
  >In ps4a.py, note that in the function playHand, there is a bunch of pseudocode. This pseudocode is provided to help guide you in writing your function.
  
- Problem 6 - Playing a Game
  >A game consists of playing multiple hands. We need to implement one final function to complete our word-game program. Write the code that implements the playGame function. For the game, you should use the HAND_SIZE constant to determine the number of cards in a hand.  

- [Completed Assignment Part 1](pset4/ps4a.py)  

- Problem 7 - You and Your Computer
  >If you follow the pseudocode for compChooseWord, you'll see that the code creates a computer player that is legal, but not always the best.
  >The function, compPlayHand allows the computer to play a given hand and is very similar to the earlier version in which a user selected the word, although deciding when it is done playing a particular hand is different.
  >Write the code that re-implements the playGame function. As before, you should use the HAND_SIZE constant to determine the number of cards in a hand.  
  
- [Completed Assignment Part 2](pset4/ps4b.py)
  


## Unit 5: Object Oriented Programming

#### Material Covered:  

9. Classes and Inheritance  
10. An Extended Example  

#### [Problem Set 5: Cipher](pset5)  

- Problem 1 - Build the Shift Dictionary and Apply Shift
  >The Message class contains methods that could be used to apply a cipher to a string, either to encrypt or to decrypt a message (since for Caesar codes this is the same action).  
  >The methods in the Message class already filled in are:
  >- \_\_init\_\_(self, text)
  >- The getter method get_message_text(self)
  >- The getter method get_valid_words(self), notice that this one returns a copy of self.valid_words to prevent someone from mutating the original list.
  >
  >\
  >In this problem, you will fill in two methods:
  >1. Fill in the build_shift_dict(self, shift) method of the Message class. Be sure that your dictionary includes both lower and upper case letters, but that the shifted character for a lower case letter and its uppercase version are lower and upper case instances of the same letter. What this means is that if the original letter is "a" and its shifted value is "c", the letter "A" should shift to the letter "C".
  >2. Fill in the apply_shift(self, shift) method of the Message class. You may find it easier to use build_shift_dict(self, shift). Remember that spaces and punctuation should not be changed by the cipher.
  
- Problem 2 - PlaintextMessage
  >PlaintextMessage is a subclass of Message and has methods to encode a string using a specified shift value. Our class will always create an encoded version of the message, and will have methods for changing the encoding.
  >Implement the methods in the class PlaintextMessage according to the specifications in ps6.py. The methods you should fill in are:
  >- \_\_init\_\_(self, text, shift): Use the parent class constructor to make your code more concise.
  >- The getter method get_shift(self)
  >- The getter method get_encrypting_dict(self): This should return a COPY of self.encrypting_dict to prevent someone from mutating the original dictionary.
  >- The getter method get_message_text_encrypted(self)
  >- change_shift(self, shift): Think about what other methods you can use to make this easier. It shouldn’t take more than a couple lines of code.
  
- Problem 3 - Printing Out All Available Letters
  >Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.
  
- Problem 3 - CiphertextMessage
  >Given an encrypted message, if you know the shift used to encode the message, decoding it is trivial. If message is the encrypted message, and s is the shift used to encrypt the message, then apply_shift(message, 26-s) gives you the original plaintext message.
  >The problem, of course, is that you don’t know the shift. But our encryption method only has 26 distinct possible values for the shift! We know English is the main language of these emails, so if we can write a program that tries each shift and maximizes the number of English words in the decoded message, we can decrypt their cipher! A simple indication of whether or not the correct shift has been found is if most of the words obtained after a shift are valid words. Note that this only means that most of the words obtained are actual words.
  >Fill in the methods in the class CiphertextMessage acording to the specifications in ps6.py. The methods you should fill in are:
  >- \_\_init\_\_(self, text): Use the parent class constructor to make your code more concise.
  >- decrypt_message(self): You may find the helper function is_word(wordlist, word) and the string method split() useful. Note that is_word will ignore punctuation and other special characters when considering whether a word is valid.
  
- Problem 4 - Decrypt a Story
  >Now that you have all the pieces to the puzzle, please use them to decode the file story.txt. The file ps6.py contains a helper function get_story_string() that returns the encrypted version of the story as a string. Create a CiphertextMessage object using the story string and use decrypt_message to return the appropriate shift value and unencrypted story string.

- [Completed Assignment](pset5/ps5.py)  
  


## Unit 6: Algorithmic Complexity

#### Material Covered:  

11. Computational Complexity  
12. Searching and Sorting Algorithms  
  


## Unit 7: Plotting

#### Material Covered:  

13. Plotting
- Summary and Wrap-Up
