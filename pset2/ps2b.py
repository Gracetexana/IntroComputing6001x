"""
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The monthly payment must be a multiple of $10 and is the same for all months.
"""

balance = 3926
annualInterestRate = 0.2

def fixedcc(b, ir, p, t= 12):
    """
    calculates the balance on a credit card after paying the same amount each month

    -balance: starting balance; float
    -annualInterestRate: percent yearly interest; float
    -p: fixed monthly payment; float
    -t: how long in months that the payment is made for; int
    
    returns balance after making fixed payment p for t time"""
    if t == 0:
        return b
    else:
        prebal = fixedcc(b, ir, p, t-1) #balance from previous month
        return (prebal - p) * (1 + ir/12) #balance after paying and then applying interest

def minpay10(b, ir, t= 12):
    """
    calculates minimum fixed payment on credit card debt to fully pay off within t months of time
    
    -b: starting balance; float
    -ir: annual percent interest rate; float
    -t: time in months; int

    returns lowest fixed payment to pay off credit card debt as an int divisible by 10 when accounting for interest
    """
    p = round(b/t, -1) #starting guess if there is no interest
    while fixedcc(b, ir, p, t) > 0:
        p += 10
    return int(p)

print(minpay10(balance, annualInterestRate))