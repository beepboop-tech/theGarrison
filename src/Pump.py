from Dispenser import Dispenser
from Measures import Mil

class Pump(Dispenser):
    def __init__(self, position, name, startingAmount, impeller):
        super(Pump, self).__init__(position, name, startingAmount)
        self.impeller = impeller

    def dispense(self, measure: Mil):
        self.impeller.pour(measure.amount)
