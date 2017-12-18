class Position:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def move_x(self, amount=0):
        """ Move the postion horizontally by a given amount """
        self.x += amount

    def move_y(self, amount=0):
        """ Move the position vertically by a given amount """
        self.y += amount

    def move(self, x=0, y=0):
        """ Move the position by a given amount on each axi """
        self.move_x(x)
        self.move_y(y)

    def set_x(self, x_cord):
        """ Move the x position to a new coordinate """
        self.x = x_cord

    def set_y(self, y_cord):
        """ Move the y position to a new coordinate """
        self.y = y_cord

    def set_position(self, x_cord, y_cord):
        """ Move to a new position """
        self.set_x(x_cord)
        self.set_y(y_cord)

    def get_position(self):
        """ Get the current x and y position """
        return (self.x, self.y)
