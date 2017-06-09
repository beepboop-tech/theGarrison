from abc import ABC, abstractmethod

# Defines the Super Class for Optics and pumps, as well as mechanisms
# for dispensers to keep track of how much flid they have remaning
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
