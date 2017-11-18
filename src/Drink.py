class Drink():
    def __init__(self, name, ingredients):
        self.name        = name
        self.ingredients = ingredients

    def __eq__(self, otherDrink):
        ## TODO SHould this take in to account ingredients?
        return self.name == otherDrink.name

    def __iter__(self):
        return self.ingredients.__iter__()


drinks = [Drink('Gin on the Rocks', ['gin']),
          Drink('Double Gin', ['gin', 'gin']),
          Drink('Vodka on the Rocks', ['vodka', 'vodka']),
          Drink('Peach Shnapps',['peach']),
          Drink('Sex on the Beach',['vodka', 'peach'])
          ]
