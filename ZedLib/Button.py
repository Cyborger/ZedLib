import ZedLib


class Button(ZedLib.Surface):
    """ Changes images depending on mouse location and if clicking on it,
        calls given function on release after pressing button """
    def __init__(self, image_set, function=None, x=0, y=0):
        super().__init__(image_set[0], x, y)
        self.normal_image = image_set[0]
        self.hovered_image = image_set[1]
        self.clicked_image = image_set[2]

        self.hovered = False
        self.pressed = False
        self.pressed_before_entering = False

        if function is not None:
            self.Activate = function

    def Update(self, mouse_position, left_click_pressed):
        """ Update the state of the button """
        if self.rect.collidepoint(mouse_position):
            if not self.hovered:
                self.__Hover()
                if left_click_pressed:
                    self.pressed_before_entering = True
        else:
            if self.hovered:
                self.__UnHover()
                self.pressed_before_entering = False

        if left_click_pressed:
            if self.hovered and not self.pressed_before_entering:
                self.__Press()
        else:
            if self.pressed and self.hovered:
                self.__Release()
            self.pressed_before_entering = False

    def __Hover(self):
        self.hovered = True
        self.image = self.hovered_image.copy()

    def __UnHover(self):
        self.hovered = False
        self.pressed = False
        self.image = self.normal_image.copy()

    def __Press(self):
        self.pressed = True
        self.image = self.clicked_image.copy()

    def __Release(self):
        self.pressed = False
        self.image = self.hovered_image.copy()
        self.Activate()

    def Activate(self):
        print("Button is activating but doesn't half a function to run")
