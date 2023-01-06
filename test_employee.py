import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_email(self):
        emp_1 = Employee('Corey', 'Schafer', 5000)
        emp_2 = Employee('Sue','Smith', 10000)

        self.assertEqual(emp_1.email, 'corey.schafer@email.com')
        self.assertEqual(emp_2.email, 'sue.smith@email.com')


    def test_fullname(self):
        emp_1 = Employee('Corey', 'Schafer', 5000)
        emp_2 = Employee('Sue', 'Smith', 10000)

        self.assertEqual(emp_1.fullname(), 'Corey Schafer')
        self.assertEqual(emp_2.fullname(), 'Sue Smith')

    def test_apply_raise(self):
        emp_1 = Employee('Corey', 'Schafer', 5000)
        emp_2 = Employee('Sue','Smith', 10000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 5250)
        self.assertEqual(emp_2.pay, 10500)
        



