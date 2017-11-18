import constants
from SlushConfig import motor

# STEPPER NOTES:
#
# Wire colours, besy guess so far
#   Red Wire   ->  A
#   Blue Wire  -> -A
#   Green Wire ->  B
#   Black WIre -> -B


class Stepper():
    def __init__(self):
        self.motor = motor
    
    def moveRelative(self, movement):
        if (movement < 0):
            self.moveLeft(-1 * movement)
        else:
            self.moveRight(movement)

    def moveLeft(self, movement):
        self.waitUntillDone()
        self.motor.move(int(-1 * movement*constants.STEPS_PER_CM))
        self.waitUntillDone()

    def moveRight(self, movement):
        self.waitUntillDone()
        self.motor.move(int(movement*constants.STEPS_PER_CM))
        self.waitUntillDone()

    def test(self):
        self.waitUntillDone()
        self.motor.move(1000)
        self.waitUntillDone()
        self.motor.move(-1000)
        self.waitUntillDone()

    def waitUntillDone(self):
        while(self.motor.isBusy()):
            continue       
        
        



