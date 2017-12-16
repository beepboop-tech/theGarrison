import pickle
import os

class Drink():
    def __init__(self, name, ingredients):
        self.name        = name
        self.ingredients = ingredients

    def __eq__(self, otherDrink):
        ## TODO SHould this take in to account ingredients?
        return self.name == otherDrink.name

    def __iter__(self):
        return self.ingredients.__iter__()

def loadDrinks(pickle_file = 'pickles/drinks.pickle'):
    if (not os.path.isfile(pickle_file)):
        generateDrinks()
        loadDrinks()
    with open(pickle_file, 'rb') as handle:
         drinks = pickle.load(handle)
    return drinks

def storeDrinks(drinks, pickle_file = 'pickles/drinks.pickle'):
    with open(pickle_file, 'wb') as handle:
        pickle.dump(drinks, handle, protocol=pickle.HIGHEST_PROTOCOL)

def generateDrinks():
    drinks = []
    storeDrinks(dispensers)
