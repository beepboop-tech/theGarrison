from Stepper   import Stepper
from Trolley   import Trolley, TrolleyObserver
from Dispenser import Dispenser
from Actuator  import Actuator, ActuatorObserver

d0 = Dispenser(0,  'gin', 30)
d1 = Dispenser(18, 'empty', 200)
d2 = Dispenser(36, 'peach', 10)
d3 = Dispenser(54, 'vodka', 15)
d4 = Dispenser(72, 'rum', 40)
d5 = Dispenser(88, 'empty', 200)

class BarTender(TrolleyObserver, ActuatorObserver):
    def __init__(self):

        # Trolley observer
        self.trolleyStill  = True
        self.trolleyAtHome = True
        self.trolley       = Trolley(stepper=Stepper())
        self.trolley.resgisterObserver(self)
        self.trolley.reset()

        # Actuator Observer
        self.actuatorDown = True
        self.actuator = Actuator()
        self.actuator.resgisterObserver(self)


        self.dispensers = []
        self.queue      = []

        for dispenser in [d0,d1,d2,d3,d4,d5]:
            self.addDispenser(dispenser)



    def addDispenser(self, dispenser):
        """
        After checking if the position is free, adds a dispenser to the
        Bartenders dispensers
        """
        if (dispenser.position not in [owned.position for owned in self.dispensers]):
            self.dispensers.append(dispenser)

    def make(self, drink):
        if not self.canMake(drink):
            return False
        for ingredient in drink:
            for dispenser in self.dispensers:
                if (dispenser.name == ingredient):
                    self.trolley.moveTo(dispenser.position)
                    self.actuator.press()
                    dispenser.amount -=1
        self.trolley.goHome()
        return True

    def canMake(self, drink):
        for ingredient in drink:
            hasIngredient = False
            for dispenser in self.dispensers:
                if (ingredient == dispenser.name) and (dispenser.amount > 1):
                    hasIngredient = True
            if not hasIngredient:
                return False
        return True


    def shutDown(self):
        self.trolley.moveTo(0)
        self.trolley.stepper.motor.free()



    # Trolley Observer
    def trolleyMovedHome(self, trolley):
        self.trolleyStill  = True
        self.trolleyAtHome = True

    def trolleyFinishedMove(self, trolley):
        self.trolleyStill  = True
        self.trolleyAtHome = False

    def trolleyMoving(self, trolley):
        self.trolleyStill  = False

    #Actuator observer
    def actuatorRaised(self, actuator):
        self.actuatorDown = False

    def actuatorLowered(self, actuator):
        self.actuatorDown = True
