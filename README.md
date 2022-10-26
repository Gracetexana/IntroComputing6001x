# Introduction to Computer Science and Programming Using Python
## MITx 6.00.1x through edX
On my quest to become a data scientist, I enrolled in this course from August 25, 2022 to October 27, 2022. I learned much more than I expected; of course I learned and relearned some Python basics, but I also learned how to think computationally.  
Additionally, we also briefly covered the Python package, Pylab. After working on [my last repository](https://github.com/Gracetexana/Rosalind), I was hoping to learn a little bit more about Python packages, so I was pleased that we did in this course.
## Units 
  <details><summary><h3>
Unit 1: Python Basics
  </h3></summary>

#### Material Covered:  
1. Introduction to Python  
2. Core Elements of Programs  

#### [Problem Set](pset1):
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
  
</details>

<details><summary><h3>
  
Unit 2: Simple Programs
  
</h3></summary>

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

#### [Problem Set](pset2):
- [Problem 1](pset2/ps2a.py)  
  >Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.  
  >The following variables contain values as described below:  
  >- balance - the outstanding balance on the credit card  
  >- annualInterestRate - annual interest rate as a decimal  
  >- monthlyPaymentRate - minimum monthly payment rate as a decimal  
  >
  >\
  >For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy.


- [Problem 2](pset2/ps2b.py)  
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


- [Problem 3](pset2/ps2c.py)  
  >You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates.  
Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!  
The following variables contain values as described below:  
  >- balance - the outstanding balance on the credit card  
  >- annualInterestRate - annual interest rate as a decimal  
  >
  >\
  >Write a program that uses bisection search to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year.  
</details>
