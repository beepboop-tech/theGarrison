from Dispenser import Dispenser

class Pump(Dispenser):

    def __init__(self, position, name, startingAmount, impeller):
        super(Pump, self).__init__(position, name, startingAmount)
        self.impeller = impeller

    def dispense(self, amount):
        #self.impeller.pour(amount.amount)
        pass
