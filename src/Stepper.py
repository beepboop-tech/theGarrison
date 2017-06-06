class Stepper():
    def moveRelative(self, movement):
        if (movement < 0):
            self.moveLeft(-1 * movement)
        else:
            self.moveRight(movement)

    def moveLeft(self, movement):
        pass

    def moveRight(self, movement):
        pass
