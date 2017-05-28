from abc import ABC, abstractmethod


class Dispenser():
    """ This is a Dispenser"""

    @abstractmethod
    def dispense(self):
        """The Dispense Method"""
        pass
