from abc import ABC, abstractmethod

import time
import constants

# ACTUATOR NOTES:
#
# To Extend:
#     Red wire   -> negitive
#     Black wire -> positive
#
# To Retract:
#     Red wire   -> positive
#     Black wire -> negitive

class Actuator():

    def __init__(self, upPin=constants.ACTUATOR_UP, downPin=constants.ACTUATOR_DOWN):
        self.observers = []
        self.upPin     = upPin
        self.downPin   = downPin

    # Adds observer as an observer of the actuator. It will be notified when the
    # actuator moves.
    def resgisterObserver(self, observer):
        if (issubclass(type(observer), ActuatorObserver)):
            self.observers.append(observer)
        else:
            raise TypeError("observer must be a ActuatorObserver.")

    def press(self):
        time.sleep(constants.TIME_TO_WAIT_BETWEEN_PRESSES)
        self.extend()
        time.sleep(constants.TIME_TO_EMPTY_OPTIC)
        self.retract()

    def extend(self):
        # Implament the relay control here
        for observer in self.observers:
            observer.actuatorRaised(self)

    def retract(self):
        # Implament the relay control here
        for observer in self.observers:
            observer.actuatorLowered(self)


# This class describes objects that can observe the actions of
# an Actuator, and get notified when certain actions are carried out.
class ActuatorObserver():
    # Called when the actuator is Rasied
    @abstractmethod
    def actuatorRaised(self, actuator):
        pass

    # Called when the actuator is lowered
    @abstractmethod
    def actuatorLowered(self, actuator):
        pass
