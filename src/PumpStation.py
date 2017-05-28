from Station import Station

class PumpStation(Station):
    
    def __init__(self, usePump):
        self.usePump = usePump

    def pour(self):
        self.usePump(self.doneTrolley)
