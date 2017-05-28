class Trolley():

    def __init__(self):
        self.queue = []                                                         # [(position, completedMove, finished)]
        self.queueIndex = None

    def press(self, completedPress):
        # TODO: Press the actuator
        completedPress()

    def done(self):
        self.queue[self.queueIndex][2] = True                                   # Sets the flag in the current queue entry to be False
        if (any(map(lambda p, c, f: f==False, self.queue))):
            nextMove()
        else:
            # move(0, lambda : print "Done")
            # nextMove() # TODO HACK NOTE This needs call move and NextMove
            pass


    def move(self, position, completedMove):
        queueEntry = (position, completedMove, False)
        self.queue.append(queueEntry)

    def nextMove(self):
        currPos, _ , _  = self.queue[self.queueIndex]
        notFinished     = list(filter(lambda i, e: e[2]==False, enumerate(self.queue)))
        index, element  = min(notFinished, key=lambda i, element: abs(currPos - element[0]))
        # TODO: Move the Motor here
        element[1]()                                                            # This is the completion handler of the queue entry
        self.queueIndex = index                                                 # Updates the queueIndex

    def startMoving(self):
        self.queueIndex = 0
        nextMove()
