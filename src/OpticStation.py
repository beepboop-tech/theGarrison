from Station import Station

class OpticStation(Station):

    def __init__(self, pressTrolley):
        self.pressTrolley = pressTrolley
        
    def pour(self):
        self.pressTrolley(self.doneTrolley)
