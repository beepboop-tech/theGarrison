import time
import constants

class Impeller():
    
    def pour(self, mils):
        # Turn on the pump relay
        time.sleep(constants.SECONDS_PER_MIL * mils)
        # Turn off the pump relay
