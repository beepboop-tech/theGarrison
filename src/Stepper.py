
# STEPPER NOTES:
#
# Wire colours, besy guess so far
#   Red Wire   ->  A
#   Blue Wire  -> -A
#   Green Wire ->  B
#   Black WIre -> -B


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
