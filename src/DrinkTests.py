import unittest
from Drink import Drink

class TestMeasuresMethods(unittest.TestCase):
    def testDrinkEquality(self):
        d1 = Drink("testDrink1", ["ing1", "ing2", "ing3"])
        d2 = Drink("testDrink2", ["ing1", "ing2", "ing3"])
        d3 = Drink("testDrink1", ["ing1"])
        self.assertTrue(d1==d3)
        self.assertFalse(d1==d2)

    def testDrinkIterator(self):
        d1 = Drink("testDrink1", ["ing1", "ing2", "ing3"])
        lst = []
        for ingredient in d1:
            lst.append(ingredient)
        self.assertEqual(lst, ["ing1", "ing2", "ing3"])

if __name__ == '__main__':
    unittest.main()
