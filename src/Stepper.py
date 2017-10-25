
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
        # TODO Implement motor control
        pass

    def moveRight(self, movement):
        # TODO Implement motor control
        pass
