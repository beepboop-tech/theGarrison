from abc import ABC, abstractmethod
from Stepper import Stepper

class Trolley():
    def __init__(self, stepper=Stepper(), homePosition=0):
        self.stepper = stepper
        self.resetPosition()
        self.currentPosition = 0
        self.homePosition = homePosition
        self.observers = []
        self.goHome()

    # Adds observer as an observer of the trolley. It will be notified when the
    # trolley moves home, and finishes a move.
    def resgisterObserver(self, observer):
        if (issubclass(type(observer), TrolleyObserver)):
            self.observers.append(observer)
        else:
            raise TypeError("observer must be a TrolleyObserver")

    # NOTE: This should block as the current position is initialised to zero
    # afterwards.
    def resetPosition(self):
        # Go left until a button is pressed.
        pass

    # Moves to position.
    def __moveTo(self, position, isHome=False):

        movement = position - self.currentPosition
        self.stepper.moveRelative(movement)
        self.currentPosition = position                                         # TODO Test
        for observer in self.observers:
            if isHome:
                observer.trolleyMovedHome(self)
            else:
                observer.trolleyFinishedMove(self)

    def goHome(self):
        self.__moveTo(self.homePosition, isHome=True)

    def moveTo(self, position):
        self.__moveTo(position)

    def safeToMove(self):
        # return buttonIsPressed
        pass


class TrolleyObserver():
    # Called when the trolley returns to the home position.
    @abstractmethod
    def trolleyMovedHome(self, trolley):
        pass

    # Called when the trolley moves to not the home position.
    @abstractmethod
    def trolleyFinishedMove(self, trolley):
        pass
