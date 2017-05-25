""" Used to make hoverable buttons that complete different tasks when clicked.
To make a button that does something when clicked, create a new button class
that inherits the super class but overrides the Activate() function.
First the button must be checked to see if the mouse is hovering it, if it is,
change the image to hovering. Then when there is a mouse click it will check
if the button is hovered, if it then it will be held down. Once the mouse
click is released, if it is still hovered it will do whatever Activate() is"""


class Button:
    def __init__(self, strip, function=None):
        self.non_hovered_image = strip[0]
        self.hovered_image = strip[1]
        self.clicked_image = strip[2]
        self.image = self.non_hovered_image
        self.rect = self.image.get_rect()
        self.hovered = False
        self.pressed = False
        self.Activate = function

    def SetPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def Update(self, mouse_position):
        if self.rect.collidepoint(mouse_position):
            self.Hover()
        else:
            self.UnHover()

    def Hover(self):
        if not self.hovered:
            self.hovered = True
            self.image = self.hovered_image.copy()

    def UnHover(self):
        if self.hovered:
            self.hovered = False
            self.image = self.non_hovered_image.copy()

    def CheckPress(self):
        if self.hovered:
            self.pressed = True
            self.image = self.clicked_image.copy()

    def CheckRelease(self):
        if self.pressed:
            self.pressed = False
            self.image = self.hovered_image.copy()
            self.Activate()

    def Activate(self):
        pass
