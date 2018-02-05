import pickle
import os
from Measures import Unit


class Ingredient():
    def __init__(self, name, measure: Unit):
        self.name    = name
        self.measure = measure

    @classmethod
    def fromJson(cls, json):
        name = json['name']
        measure = Unit.fromJson(json['measure'])

        return cls(name, measure)

class Drink():
    def __init__(self, name, ingredients):
        self.name        = name
        self.ingredients = ingredients

    def __eq__(self, otherDrink):
        ## TODO SHould this take in to account ingredients?
        return self.name == otherDrink.name

    def __iter__(self):
        return self.ingredients.__iter__()

    def pretty_ingredients(self):
        string = ''
        for ingredient in self.ingredients:
            string = string + str(ingredient.measure) + ' ' + ingredient.name + ', '

        return string[:-2] # removes the last comma and space

        
    def pretty_name(self):
        return self.name.replace('-', ' ').capitalize()

    @classmethod
    def fromJson(cls, json):
        name = json['name']
        ingredients = [Ingredient.fromJson(i) for i in json['ingredients']]

        return cls(name, ingredients)




def loadDrinks(pickle_file = 'pickles/drinks.pickle'):
    if (not os.path.isfile(pickle_file)):
        generateDrinks()

    with open(pickle_file, 'rb') as handle:
         drinks = pickle.load(handle)
    return drinks

def storeDrinks(drinks, pickle_file = 'pickles/drinks.pickle'):
    with open(pickle_file, 'wb') as handle:
        pickle.dump(drinks, handle, protocol=pickle.HIGHEST_PROTOCOL)

def generateDrinks():
    drinks = []
    storeDrinks(drinks)
