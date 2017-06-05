class Unit():

    def __init__(self, amount, name):
        self.amount = amount
        self.name   = name

    def binaryOp(self, otherUnit, op):
        self.checkType(otherUnit)
        total = op(self.amount, otherUnit.amount)
        return type(self)(total)

    def __add__(self, otherUnit):
        return self.binaryOp(otherUnit, lambda x, y: x + y)

    def __sub__(self, otherUnit):
        return self.binaryOp(otherUnit, lambda x, y: x - y)

    def __le__(self, otherUnit):
        self.checkType(otherUnit)
        return (self.amount <= otherUnit.amount)

    def __iter__(self):
        return range(self.amount).__iter__()

    def __eq__(self, otherUnit):
        self.checkType(otherUnit)
        return (self.amount == otherUnit.amount)

    def checkType(self, other):
        if not (type(self) == type(other)):
            raise TypeError("Types of units in binary operation were not the same")


class Shot(Unit):
    """docstring for Shot."""
    def __init__(self, amount):
        super(Shot, self).__init__(amount, "shot")


class Mil(Unit):
    """docstring for Mil."""
    def __init__(self, amount):
        super(Mil, self).__init__(amount, "mil")
