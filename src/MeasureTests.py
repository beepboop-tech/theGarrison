import unittest

from Measures import *

class TestMeasuresMethods(unittest.TestCase):

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

        self.assertEqual(c.name, "shot")

    # Tests that a type error is thrown when two units of different types are
    # subtracted.
    def testAddTypeError(self):
        a = Shot(1)
        b = Mil(1)
        f = lambda: a + b
        self.assertRaises(TypeError, f)

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

        self.assertEqual(c.name, "shot")

    # Tests that a type error is thrown when two units of different types are
    # subtracted.
    def testSubTypeError(self):
        a = Shot(1)
        b = Mil(1)
        f = lambda: a - b
        self.assertRaises(TypeError, f)

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


if __name__ == '__main__':
    unittest.main()
