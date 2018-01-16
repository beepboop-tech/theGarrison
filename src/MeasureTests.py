import unittest

from Measures import *

class TestMeasuresMethods(unittest.TestCase):
    ##################
    # Addition Tests #
    ##################

    # Tests the amount of two units is added together.
    def testAddAmounts(self):
        a = Shot(1)
        b = Shot(2)
        c = a + b

        self.assertEqual(c.amount, 3)

    # Tests that, when adding two units, the name does not change.
    def testAddNames(self):
        a = Shot(1)
        b = Shot(2)
        c = a + b

        self.assertEqual(c.name, "shots")

    # Tests that a type error is thrown when two units of different types are
    # subtracted.
    def testAddTypeError(self):
        a = Shot(1)
        b = Mil(1)
        f = lambda: a + b
        self.assertRaises(TypeError, f)


    #####################
    # Subtraction Tests #
    #####################

    # Tests the amount of two units subtracted.
    def testSubAmounts(self):
        a = Shot(5)
        b = Shot(2)
        c = a - b

        self.assertEqual(c.amount, 3)

    # Tests that, when subtracting two units, the name does not change.
    def testSubNames(self):
        a = Shot(5)
        b = Shot(2)
        c = a - b

        self.assertEqual(c.name, "shots")

    # Tests that a type error is thrown when two units of different types are
    # subtracted.
    def testSubTypeError(self):
        a = Shot(1)
        b = Mil(1)
        f = lambda: a - b
        self.assertRaises(TypeError, f)

    ####################
    # Less Equal Tests #
    ####################

    # Tests that the <= function works with units
    def testLessEqual(self):
        a = Shot(1)
        b = Shot(5)

        self.assertTrue (a <= b)
        self.assertFalse(b <= a)
        self.assertTrue (b <= b)
    # Tests that a type error is thrown when two units of different types are
    # compared.
    def testLETypeError(self):
        a = Shot(1)
        b = Mil(1)
        f = lambda: a <= b
        self.assertRaises(TypeError, f)

    ##################
    # Equality Tests #
    ##################

    def testEqual(self):
        a = Shot(1)
        b = Shot(1)
        self.assertEqual(a, b)

    def testEqualType(self):
        a = Shot(1)
        b = Mil(1)
        f = lambda: a == b
        self.assertRaises(TypeError, f)

    def testNotEqual(self):
        a = Shot(1)
        b = Shot(2)
        self.assertNotEqual(a, b)

    ##################
    # Iterable Tests #
    ##################

    def testIterateCorrectNumberOfTimes(self):
        a   = Shot(5)
        lst = []
        for _ in a:
            lst.append("x")
        self.assertEqual(len(lst), 5)


    ##################
    # String Tests   #
    ##################

    def testString(self):
        a   = Shot(5)
        self.assertEqual('5 shots', str(a))



if __name__ == '__main__':
    unittest.main()
