from abc       import ABC, abstractmethod
from Dispenser import Dispenser

class Station(Dispenser):
    """Station: A Dispenser that has a definite position"""

    def __init__(self, position, moveTrolley, doneTrolley):
        self.moveTrolley  = moveTrolley
        self.doneTrolley  = doneTrolley

    @abstractmethod
    def pour(self):
        pass

    def dispense(self):
        self.moveTrolley(position, self.pour())
