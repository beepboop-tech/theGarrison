from Dispenser import Dispenser
import time

class Optic(Dispenser):

    def __init__(self, position, name, startingAmount, actuator):
        super(Optic, self).__init__(position, name, startingAmount)
        self.actuator = actuator

    def dispense(self, amount):
        # for _ in amount:
        #     self.actuator.press()
        pass
