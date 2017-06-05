import time
import constants

class Actuator():

    def press(self):
        time.sleep(constants.TIME_TO_WAIT_BETWEEN_PRESSES)
        self.extend()
        time.sleep(constants.TIME_TO_EMPTY_OPTIC)
        self.retract()

    def extend(self):
        # Implament the relay control here
        pass
    def retract(self):
        # Implament the relay control here
        pass
