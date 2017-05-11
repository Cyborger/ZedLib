import pygame

class RenderWindow:
    def __init__(self, width, height, fullscreen=False):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height),
                                              pygame.RESIZABLE)
        if fullscreen:
            pygame.display.toggle_fullscreen()
        self.display_info = pygame.display.Info()

    def Resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
        self.screen = pygame.display.set_mode((self.width, self.height),
                                              pygame.RESIZABLE)
