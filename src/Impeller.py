from abc import ABC, abstractmethod

import time
import constants

class Impeller():

    def __init__(self):
        self.observers = []

    # Adds observer as an observer of the impeller. It will be notified when the
    # impeller is turned on or off.
    def resgisterObserver(self, observer):
        if (issubclass(type(observer), ImpellerObserver)):
            self.observers.append(observer)
        else:
            raise TypeError("observer must be a ImpellerObserver.")


    def pour(self, mils):
        self.turnOn()
        time.sleep(constants.SECONDS_PER_MIL * mils)
        self.turnOff()

    def turnOn(self):
        # Turn on the pump relay
        for observer in self.observers:
            observer.impellerOn(self)

    def turnOff(self):
        # Turn off the pump relay
        for observer in self.observers:
            observer.impellerOff(self)


class ImpellerObserver():
    # Called when the impeller is turned on
    @abstractmethod
    def impellerOn(self, impeller):
        pass

    # Called when the impeller is turned off
    @abstractmethod
    def impellerOff(self, impeller):
        pass
