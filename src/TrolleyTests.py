import unittest

from Trolley import Trolley
from Trolley import TrolleyObserver

class TestObserver(TrolleyObserver):
    def __init__(self):
        self.movedHome     = False
        self.finishedMoved = False

    def trolleyMovedHome(self, trolley):
        self.movedHome = True

    def trolleyFinishedMove(self, trolley):
        self.finishedMoved = True


class TestTrolleyMethods(unittest.TestCase):
    def setUp(self):
        self.trolley = Trolley()

        ob1 = TestObserver()
        ob2 = TestObserver()

        self.observers = [ob1, ob2]

        self.trolley.resgisterObserver(ob1)
        self.trolley.resgisterObserver(ob2)

    def tearDown(self):
        del self.trolley
        del self.observers

    # Tests the trolley calls the `trolleyMovedHome` method for
    # observers is called.
    def testMovedHomeCalled(self):
        self.trolley.goHome()

        movedHomes    = map(lambda observer: observer.movedHome, self.observers)
        finishedMoves = map(lambda observer: observer.finishedMoved, self.observers)

        self.assertTrue(all(movedHomes))
        self.assertFalse(any(finishedMoves))

    # Tests the trolley calls the `trolleyFinishedMove` method for
    # observers is called.
    def testFinishedMoveCalled(self):
        self.trolley.moveTo(0)

        movedHomes    = map(lambda observer: observer.movedHome, self.observers)
        finishedMoves = map(lambda observer: observer.finishedMoved, self.observers)

        self.assertTrue(all(finishedMoves))
        self.assertFalse(any(movedHomes))

if __name__ == '__main__':
    unittest.main()
