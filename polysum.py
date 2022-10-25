from math import tan
from math import pi

def polysum(n,s):
    """
    n: int > 2
    s: positive int or float
    return area + perimeter^2
    """
    area = 0.25*n*s**2/tan(pi/n)
    persq = (n*s)**2
    return round(area + persq, 4)