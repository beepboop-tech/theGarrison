from Stepper   import Stepper
from Trolley   import Trolley, TrolleyObserver
from Actuator  import Actuator, ActuatorObserver
from Dispenser import Dispenser, loadDispensers, storeDispensers
from Optic     import Optic
from Pump      import Pump
from Impeller  import Impeller
from Drink     import Drink, loadDrinks, storeDrinks
from Measures  import Unit
import constants



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

        self.dispensers = loadDispensers()
        self.drinks     = loadDrinks()
        self.queue      = []

        self.has_glass  = False


    def make(self, drink):
        if not self.canMake(drink):
            return False
        for ingredient in drink:
            for dispenser in self.dispensers:
                if (dispenser.name == ingredient.name):
                    self.trolley.moveTo(dispenser.position)
                    dispenser.dispense(ingredient.measure)
                    dispenser.hasUsed(ingredient.measure)

        self.trolley.goHome()
        storeDispensers(self.dispensers)
        return True

    def canMake(self, drink):
        for ingredient in drink:
            hasIngredient = False
            for dispenser in self.dispensers:
                if (ingredient.name == dispenser.name) and (dispenser.has(ingredient.measure)):
                    hasIngredient = True
            if not hasIngredient:
                return False
        return True


    def shutDown(self):
        storeDispensers(self.dispensers)
        self.trolley.moveTo(0)
        self.trolley.stepper.motor.free()

    def addDispenser(self, name, dispenser_type, index, remaining: Unit):
        if (dispenser_type == 'optic'):
            new_dispenser = Optic(constants.DISPENSER_LOCATIONS[index], name, remaining, self.actuator)
        elif (dispenser_type == 'pump'):
            impeller      = Impeller(constants.PUMP_TO_PIN[index])
            new_dispenser = Pump(constants.DISPENSER_LOCATIONS[index], name, remaining, impeller)

        self.dispensers[index] = new_dispenser
        storeDispensers(self.dispensers)


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
