from abc import ABC, abstractmethod

class Dispenser():

    def __init__(self, position, name, startingAmount):
        self.amount   = startingAmount
        self.position = position
        self.name     = name                                                    

    def has(self, amount):
        return amount <= self.amount

    def hasUsed(self, amount):
        self.amount -= amount

    @abstractmethod
    def dispense(self, amount):
        pass
