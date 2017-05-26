""" Used to make hoverable buttons that complete different tasks when clicked.
To make a button that does something when clicked, create a new button class
that inherits the super class but overrides the Activate() function.
First the button must be checked to see if the mouse is hovering it, if it is,
change the image to hovering. Then when there is a mouse click it will check
if the button is hovered, if it then it will be held down. Once the mouse
click is released, if it is still hovered it will do whatever Activate() is"""


class Button(ZedLib.Surface):
    def __init__(self, strip, function=None, x=0, y=0):
        self.non_hovered_image = strip[0]
        self.hovered_image = strip[1]
        self.clicked_image = strip[2]
        super().__init__(self.non_hovered_image, x, y)
        self.rect = self.image.get_rect()
        self.hovered = False
        self.pressed = False
        if function is not None:
            self.Activate = function

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
        if self.pressed and self.hovered:
            self.pressed = False
            self.image = self.hovered_image.copy()
            self.Activate()

    def Activate(self):
        print("Button is doing whatever it should be, " +
              "but there is nothing to do")
