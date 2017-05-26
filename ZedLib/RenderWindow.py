import pygame


class RenderWindow:
    def __init__(self, width, height, fullscreen=False):
        self.fullscreen = fullscreen
        if self.fullscreen:
            display_info = pygame.display.Info()
            self.width = display_info.current_w
            self.height = display_info.current_h
            self.screen = pygame.display.set_mode((self.width,
                                                   self.height),
                                                  pygame.FULLSCREEN)
        else:
            self.width = width
            self.height = height
            self.screen = pygame.display.set_mode((self.width, self.height),
                                              pygame.RESIZABLE)

    def Resize(self, new_width, new_height):
        if not self.fullscreen:
            self.width = new_width
            self.height = new_height
            self.screen = pygame.display.set_mode((self.width, self.height),
                                                  pygame.RESIZABLE)
