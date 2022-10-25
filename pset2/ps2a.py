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