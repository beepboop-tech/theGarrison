import unittest

from Actuator import Actuator
from Actuator import ActuatorObserver

class TestActuatorObserver(ActuatorObserver):
    def __init__(self):
        self.raised  = False
        self.lowered = False

    def actuatorRaised(self, actuator):
        self.raised  = True
        self.lowered = False

    def actuatorLowered(self, actuator):
        self.raised  = False
        self.lowered = True


class TestActiuatorMethods(unittest.TestCase):
    def setUp(self):
        self.actuator = Actuator()

        ob1 = TestActuatorObserver()
        ob2 = TestActuatorObserver()

        self.observers = [ob1, ob2]

        self.actuator.resgisterObserver(ob1)
        self.actuator.resgisterObserver(ob2)

    def tearDown(self):
        del self.actuator
        del self.observers

    # Tests the trolley calls the `trolleyMovedHome` method for
    # observers is called.
    def testRaisedCalled(self):
        self.actuator.extend()

        raised  = map(lambda observer: observer.raised,  self.observers)
        lowered = map(lambda observer: observer.lowered, self.observers)

        self.assertTrue(all(raised))
        self.assertFalse(any(lowered))

    # Tests the trolley calls the `trolleyMovedHome` method for
    # observers is called.
    def testLoweredCalled(self):
        self.actuator.retract()

        raised  = map(lambda observer: observer.raised,  self.observers)
        lowered = map(lambda observer: observer.lowered, self.observers)

        self.assertTrue(all(lowered))
        self.assertFalse(any(raised))



if __name__ == '__main__':
    unittest.main()
