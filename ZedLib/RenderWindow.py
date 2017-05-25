import pygame


class RenderWindow:
    def __init__(self, width, height, fullscreen=False):
        self.width = width
        self.height = height
        if fullscreen:
            self.screen = pygame.display.set_mode((self.width, self.height),
                                                  pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.width, self.height),
                                              pygame.RESIZABLE)
        self.display_info = pygame.display.Info()

    def Resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
        self.screen = pygame.display.set_mode((self.width, self.height),
                                              pygame.RESIZABLE)
