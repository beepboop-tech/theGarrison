from abc import ABC, abstractmethod
import pickle

# Defines the Super Class for Optics and pumps, as well as mechanisms
# for dispensers to keep track of how much fluid they have remaning
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

def loadDispensers(pickle_file = 'pickles/dispensers.pickle'):
    with open(pickle_file, 'rb') as handle:
         dispensers = pickle.load(handle)
    return dispensers

def storeDispensers(dispensers, pickle_file = 'pickles/dispensers.pickle'):
    with open(pickle_file, 'wb') as handle:
        pickle.dump(dispensers, handle, protocol=pickle.HIGHEST_PROTOCOL)
