import unittest
from math import pi

def circle_area(r):
    if r < 0:
        raise ValueError("radius is less than zero")
    
    if type(r) not in [int, float]:
        raise TypeError("radius is not a number")
    # calculates the area of a circle
    return pi*(r**2)

# print(circle_area(0))