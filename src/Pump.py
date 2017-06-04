from Dispenser import Dispenser

class Pump(Dispenser):

    def __init__(self, position, name, startingAmount, pump):
        super(Optic, self).__init__(position, name, startingAmount)
        self.pump = pump

    def dispense(self, amount):
        #self.pump.pour(amount.amount)
        pass
