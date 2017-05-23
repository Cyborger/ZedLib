""" A position in 2d space, it is a float but can be rounded
to an int for pygame Rects"""


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def SetRectPosition(self, rect):
        rect.x = int(self.x)
        rect.y = int(self.y)

    def SetPosition(self, x, y):
        self.SetX(x)
        self.SetY(y)

    def SetX(self, x):
        self.x = x

    def SetY(self, y):
        self.y = y

    def Move(self, x, y):
        self.MoveX(x)
        self.MoveY(y)

    def MoveX(self, amount):
        self.x += amount

    def MoveY(self, amount):
        self.y += amount
