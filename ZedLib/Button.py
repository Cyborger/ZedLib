""" Used to make hoverable buttons that complete different tasks when clicked.
To make a button that does something when clicked, create a new button class
that inherits the super class but overrides the Clicked() function"""


class Button:
    def __init__(self, spritesheet):
        self.non_hovered_image = spritesheet.GetImage(0, 0)
        self.hovered_image = spritesheet.GetImage(0, 1)
        self.image = non_hovered_image
        self.rect = self.image.get_rect()
        self.hovered = False
        self.pressed = True

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
            self.image = self.hovered_image

    def UnHover(self):
        if self.hovered:
            self.hovered = False
            self.image = self.non_hovered_image

    def CheckPress(self):
        if self.hovered:
            self.pressed = True

    def CheckRelease(self):
        if self.pressed:
            self.pressed = False
            self.Activate()

    def Activate(self):
        pass
