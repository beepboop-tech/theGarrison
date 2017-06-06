from abc import ABC, abstractmethod

import time
import constants

# ACTUATOR NOTES:
#
# To Extend:
#     Red wire   -> negitive
#     Black wire -> positive
#
# To retract:
#     Red wire   -> positive
#     Black wire -> negitive

class Actuator():

    def __init__(self):
        self.observers = []

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


class ActuatorObserver():
    # Called when the actuator is Rasied
    @abstractmethod
    def actuatorRaised(self, actuator):
        pass

    # Called when the actuator is lowereds
    @abstractmethod
    def actuatorLowered(self, actuator):
        pass
