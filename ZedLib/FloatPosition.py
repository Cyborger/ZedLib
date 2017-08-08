class FloatPosition:
    """ 2D position using floats """
    def __init__(self, rect, x=0.0, y=0.0):
        self.x = x
        self.y = y
        self.rect = rect
        self.UpdateRectX()
        self.UpdateRectY()

    def MoveX(self, distance):
        """ Move float position horizontally """
        self.x += distance

    def MoveY(self, distance):
        """ Move float position vertically """
        self.y += distance

    def SetX(self, x_position):
        """ Move float position horizontally to a specific x value """
        self.x = x_position

    def SetY(self, y_position):
        """ Move float position vertically to a specific y value """
        self.y = y_position
        
    def UpdateRectX(self):
        """ Update rect.x position using current float position """
        self.rect.x = int(self.x)

    def UpdateRectY(self):
        """ Update rect.y position using current float position """
        self.rect.y = int(self.y)

    def UpdatePositionX(self):
        """ Update horizontal float position using current rect.x """
        self.x = float(self.rect.x)

    def UpdatePositionY(self):
        """ Update vertical float position using current rect.y """
        self.y = float(self.rect.y)
