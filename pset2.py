"""
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal
"""

balance = 484
annualInterestRate = .2
monthlyPaymentRate = .04

def cc(balance, annualInterestRate, monthlyPaymentRate, time= 12):
    """
    this function calculates the remaining balance on a credit card after one year if the owner makes only minimum payments

    -balance: float; the starting balance on the card
    -annualInterestRate: float; percent interest as a decimal
    -monthlyPaymentRate: float; minimum required payment rate as a decimal

    returns the final balance after 12 months
    """
    for i in range(time):
        balance -= balance*monthlyPaymentRate #minimum monthly payment
        balance += balance*annualInterestRate/12 #monthly interest
    return round(balance, 2)

print (cc(balance, annualInterestRate, monthlyPaymentRate))




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




"""
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The monthly payment must be correct to the cent and must be the same for all months
"""
balance = 999999
annualInterestRate = 0.18

def minpay(b, ir, t= 12):
    """
    calculates minimum fixed payment on credit card debt to fully pay off within t months of time
    
    -b: starting balance; float
    -ir: annual percent interest rate; float
    -t: time in months; int

    returns lowest fixed payment to pay off credit card debt as a float with 2 decimal places when accounting for interest
    """
    p = b/t #starting guess if there is no interest
    low = 0
    high = b
    while fixedcc(b, ir, p, t) > 0 or fixedcc(b, ir, p, t) < -0.11: #balance below 0 without overpaying
        if fixedcc(b, ir, p, t) < 0:
            high = p #change bounds to check within
            p = (low + high) / 2 #middle of bounds
        else:
            low = p #change bounds to check within
            p = (low + high) / 2 #middle of bounds
    return round(p, 2)

print(minpay(balance, annualInterestRate))