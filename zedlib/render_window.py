import pygame


#TODO: Handle resizing

class RenderWindow:
    """ Game window """
    def __init__(self, width, height, flag=0):
        self.flag = flag

        self.window_width = width
        self.window_height = height
        display_info = pygame.display.Info()
        self.fullscreen_width = display_info.current_w
        self.fullscreen_height = display_info.current_h

        self.current_width = width
        self.current_height = height
        self.screen = None
        self.set_window()

    def set_window(self):
        """ Set the dimensions and type of window """
        self.screen = pygame.display.\
                set_mode((self.current_width, self.current_height), self.flag)

    def get_dimensions(self):
        return (self.current_width, self.current_height)
