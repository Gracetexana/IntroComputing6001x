from math import tan
from math import pi

def polysum(n,s):
    """
    n: number of sides in polygon; int > 2
    s: length of sides; positive int or float
    return area + perimeter^2 rounded to 4 decimal places
    """

    # equation provided by course
    area = 0.25*n*s**2/tan(pi/n)
    persq = (n*s)**2
    return round(area + persq, 4)