import unittest

from Impeller import Impeller
from Impeller import ImpellerObserver

class TestImpellerObserver(ImpellerObserver):
    def __init__(self):
        self.on      = False
        self.off     = True

    def impellerOn(self, actuator):
        self.on      = True
        self.off     = False

    def impellerOff(self, actuator):
        self.on      = False
        self.off     = True


class TestActiuatorMethods(unittest.TestCase):
    def setUp(self):
        self.impeller = Impeller()

        ob1 = TestImpellerObserver()
        ob2 = TestImpellerObserver()

        self.observers = [ob1, ob2]

        self.impeller.resgisterObserver(ob1)
        self.impeller.resgisterObserver(ob2)

    def tearDown(self):
        del self.impeller
        del self.observers

    # Tests the trolley calls the `trolleyMovedHome` method for
    # observers is called.
    def testImpellerOnCalled(self):
        self.impeller.turnOn()

        ons  = map(lambda observer: observer.on,  self.observers)
        offs = map(lambda observer: observer.off, self.observers)

        self.assertTrue(all(ons))
        self.assertFalse(any(offs))

    # Tests the trolley calls the `trolleyMovedHome` method for
    # observers is called.
    def testImpellerOffCalled(self):
        self.impeller.turnOff()

        ons  = map(lambda observer: observer.on,  self.observers)
        offs = map(lambda observer: observer.off, self.observers)

        self.assertTrue(all(offs))
        self.assertFalse(any(ons))


if __name__ == '__main__':
    unittest.main()
