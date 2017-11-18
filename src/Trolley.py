from abc import ABC, abstractmethod
from Stepper import Stepper
import constants

class Trolley():
    def __init__(self, stepper=Stepper(), homePosition=45.5):
        self.stepper      = stepper
        self.homePosition = homePosition
        self.observers    = []


    def reset(self):
        self.resetPosition()
        self.currentPosition = 0
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

        for observer in self.observers:
            observer.trolleyMoving(self)

        movement = position - self.currentPosition
        self.stepper.moveRelative(movement)
        self.currentPosition = position                                         # TODO Test
        for observer in self.observers:
            if isHome:
                observer.trolleyMovedHome(self)
                observer.trolleyFinishedMove(self)
            else:
                observer.trolleyFinishedMove(self)

    def goHome(self):
        self.__moveTo(self.homePosition, isHome=True)

    def moveTo(self, position):
        if(position > constants.MAX_RIGHT):
            position = constants.MAX_RIGHT
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

    @abstractmethod
    def trolleyMoving(self, trolley):
        pass
