import pygame


class RenderWindow:
    """ Game window """
    def __init__(self, width, height, resizable=False, fullscreen=False):
        self.fullscreen = fullscreen
        self.resizable = resizable

        self.window_dimensions = [width, height]
        display_info = pygame.display.Info()
        self.fullscreen_dimensions = [display_info.current_w,
                                      display_info.current_h]
        self.screen = None
        self.update_window()

    def update_window(self):
        """ Update the display mode """
        flags = []
        if self.fullscreen: flags.append(pygame.FULLSCREEN)
        if self.resizable: flags.append(pygame.RESIZABLE)

        self.screen = pygame.display.set_mode(self.get_window_size(), *flags)

    def get_window_size(self):
        """ Get dimensions of screen """
        if self.fullscreen:
            return self.fullscreen_dimensions
        else:
            return self.window_dimensions

    def resize(self, width, height):
        """ Resize a windowed screen """
        if not self.fullscreen:
            self.window_dimensions[0] = width
            self.window_dimensions[1] = height
            self.update_window()

    def enable_fullscreen(self):
        """ Update display mode as fullscreen """
        self.fullscreen = True
        self.update_window()

    def enable_windowed(self):
        """ Update display mode not as fullscreen """
        self.fullscreen = False
        self.update_window()

    def switch_display_type(self):
        """ Go fullscreen if windowed, or windowed if fullscreen """
        if self.fullscreen:
            self.enable_windowed()
        else:
            self.enable_fullscreen()
