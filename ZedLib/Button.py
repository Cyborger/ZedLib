import zedlib
import pygame


class Button(zedlib.Surface):
    """ Updates based on mouse position and state of mouse buttons,
    calls given function on release """

    def __init__(self, image_path, function=None, scale=1, n_of_frames=3):
        spritesheet = zedlib.Spritesheet(image_path, n_of_frames, 1, scale)
        super().__init__(spritesheet.get_first_image())

        self.normal_image = self.spritesheet.get_image(0, 0)
        self.hovered_image = self.spritesheet.get_image(1, 0)
        self.clicked_image = self.spritesheet.get_image(2, 0)

        self.hovered = False
        self.pressed = False
        self.pressed_before_hovered = False

        if function:
            self.function = function

    def update(self, mouse_position):
        """ Update image and check for press """
        left_mouse_button_pressed = pygame.mouse.get_pressed()[0]
        # Check for mouse hover
        if self.rect.collidepoint(mouse_position):
            if not self.hovered:
                self.hover()
                if left_mouse_button_pressed: self.pressed_before_hovered = True
        else:
            if self.hovered: self.left()

        # Check for press
        if left_mouse_button_pressed:
            if self.hovered and not self.pressed_before_hovered: self.press()
        # Check for release
        else:
            if self.pressed and self.hovered: self.release()
            self.pressed_before_hovered = False

    def hover(self):
        """ Button is being hovered """
        self.hovered = True
        self.image = self.hovered_image.copy()

    def left(self):
        """ Button is no longer being hovered """
        self.hovered = False
        self.pressed = False
        self.image = self.normal_image.copy()

    def press(self):
        """ Button is being pressed """
        self.pressed = True
        self.image = self.clicked_image.copy()

    def release(self):
        """ Button is being released, calling the function """
        self.pressed = False
        self.image = self.hovered_image.copy()
        self.function()

    def function(self):
        """ Called when press is released """
        print("Click")  # Place holder if function is not overwritten
