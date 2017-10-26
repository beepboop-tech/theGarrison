from Stepper   import Stepper
from Trolley   import Trolley, TrolleyObserver
from Dispenser import Dispenser

class BarTender(TrolleyObserver):
    def __init__(self):

        # Trolley observer
        self.trolleyStill  = True
        self.trolleyAtHome = True
        self.trolley       = Trolley(stepper=Stepper()) 
        self.trolley.resgisterObserver(self)
        self.trolley.reset()


        self.dispensers = []
        self.queue      = []




    def addDispenser(self, dispenser):
        """
        After checking if the position is free, adds a dispenser to the
        Bartenders dispensers
        """
        if (dispenser.position not in [owned.position for owned in self.dispensers]):
            self.dispensers.append(dispenser)


    # Trolley Observer
    def trolleyMovedHome(self, trolley):
        self.trolleyStill  = True
        self.trolleyAtHome = True

    def trolleyFinishedMove(self, trolley):
        self.trolleyStill  = True
        self.trolleyAtHome = False
