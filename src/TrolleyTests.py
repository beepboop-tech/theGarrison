import unittest
from Trolley import Trolley

class MockStation(Station):

    def __init__(self, position, moveTrolley, doneTrolley):
        super.__init__(position, moveTrolley, doneTrolley)
        self.didPour = False

    def pour():
        self.didPour = True

class TestTrolleyMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
