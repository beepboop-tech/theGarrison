class Drink():
    def __init__(self, name, ingredients):
        self.name        = name
        self.ingredients = ingredients

    def __eq__(self, otherDrink):
        ## TODO SHould this take in to account ingredients?
        return self.name == otherDrink.name

    def __iter__(self):
        return self.ingredients.__iter__()


drinks = [Drink('gin-on-the-rocks', ['gin']),
          Drink('double-gin', ['gin', 'gin']),
          Drink('vodka-on-the-rocks', ['vodka', 'vodka']),
          Drink('peach-shnapps',['peach']),
          Drink('sex-on-the-beach',['vodka', 'peach'])
          ]
