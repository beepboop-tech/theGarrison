import unittest

from Dispenser import Dispenser
from Measures  import Shot

class TestDispenserMethods(unittest.TestCase):

    def testDispenserHas(self):
        d = Dispenser(0, "x", Shot(100))
        self.assertTrue(d.has(Shot(10)))
        self.assertFalse(d.has(Shot(101)))

    def testHasUsed(self):
        d = Dispenser(0, "x", Shot(100))
        d.hasUsed(Shot(10))
        self.assertEqual(d.amount, Shot(90))


if __name__ == '__main__':
    unittest.main()
