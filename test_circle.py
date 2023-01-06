import unittest
from math import pi
from circle import circle_area

class TestCircleArea(unittest.TestCase):

    def test_area(self):
        # check for correct calculation of area
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(2.1), pi*(2.1**2))

    def test_values(self):
        # ensure that valueError is raised when necessary
        self.assertRaises(ValueError,circle_area,-2)

    def test_type(self):
        self.assertRaises(TypeError, circle_area, 2+3j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")