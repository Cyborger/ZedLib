import pygame


class RenderWindow:
    def __init__(self, width, height, fullscreen=False):
        self.fullscreen = fullscreen
        self.window_width = width
        self.window_height = height
        display_info = pygame.display.Info()
        self.fullscreen_width = display_info.current_w
        self.fullscreen_height = display_info.current_h
        self.current_width = self.window_width
        self.current_height = self.window_height
        self.screen = None
        if fullscreen:
            self.SetFullscreenWindow()
        else:
            self.SetResizableWindow()


    def SetFullscreenWindow(self):
        self.fullscreen = True
        self.current_width = self.fullscreen_width
        self.current_height = self.fullscreen_height
        self.screen = pygame.display.set_mode((self.current_width,
                                               self.current_height),
                                               pygame.FULLSCREEN)

    def SetResizableWindow(self):
        self.fullscreen = False
        self.current_width = self.window_width
        self.current_height = self.window_height
        self.screen = pygame.display.set_mode((self.current_width,
                                               self.current_height),
                                              pygame.RESIZABLE)

    def ResizeWindow(self, new_width, new_height):
        if not self.fullscreen:
            self.window_height = new_width
            self.window_height = new_height
            self.current_width = self.window_width
            self.current_height = self.window_height
