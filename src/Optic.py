from Dispenser import Dispenser
import time

class Optic(Dispenser):
    def __init__(self, position, name, startingAmount, actuator):
        super(Optic, self).__init__(position, name, startingAmount)
        self.actuator = actuator

    def dispense(self, amount):
        """
        Presses the actuator the required number of times.
        Uses the `__iter__` method of the unit, so `range` not needed.
        """
        for _ in range(0, amount):
            self.actuator.press()
