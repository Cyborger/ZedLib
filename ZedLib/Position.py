""" A position in 2d space, it is a float but can be rounded
to an int for pygame Rects"""


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def GetRectPosition(self, rect):
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def SetPosition(self, x, y):
        self.pos.x = x
        self.pos.y = y

    def Move(self, x, y):
        self.MoveX(x)
        self.MoveY(y)

    def MoveX(self, amount):
        self.x += amount

    def MoveY(self, amount):
        self.y += amount

    # Calculate the hyp of a triangle for normalized diagonal movement
    def MoveOnAngle(self, angle, distance):
        cos_angle = math.cos(math.radians(angle))
        x = cos_angle * distance
        sin_angle = math.sin(math.radians(angle))
        y = sin_angle * distance
        self.x += x
        self.y += y
