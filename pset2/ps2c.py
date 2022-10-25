"""
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The monthly payment must be correct to the cent and must be the same for all months
"""
from ps2b import fixedcc

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

    # starting guess for payment is balance/time (if there is no interest)
    p = b/t
    # lowest payment would be no payment
    low = 0
    # highest payment would be full balance
    high = b
    # lowest allowed endBalance; from here, payment could be reduced by 1 cent and the endBalance would be 0
    lowEndBalance = -0.01 * t

    while (True):
        endBalance = fixedcc(b, ir, p, t)

        # payment will be correct to the cent when end balance is between 0 (inclusive) and lowEndBalance (exclusive)
        if endBalance <= 0 and endBalance > lowEndBalance:
            break

        # payment will be too large if end balance is less than lowEndBalance (inclusive)
        if endBalance <= lowEndBalance:
            high = p
            p = (low + high) / 2

        # payment will be too small if end balance is greater than 0 (exclusive) (balance is not fully paid off)
        if endBalance > 0:
            low = p
            p = (low + high) / 2

    return round(p, 2) # p rounded to nearest cent

print(minpay(balance, annualInterestRate))