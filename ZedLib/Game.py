""" The core of the game. Handles states, the screen, the game loop,
and is also passed to certain objects that need to have access to different
parts of the game"""
import pygame
from ZedLib import RenderWindow

class Game:
    def __init__(self, screen_width, screen_height, fullscreen=False):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.Surface((self.screen_width, self.screen_height))
        self.render_screen = RenderWindow.RenderWindow(self.screen_width,
                                                       self.screen_height,
                                                       fullscreen)
        self.current_state = None
        self.clock = pygame.time.Clock()
        self.running = True

    def Draw(self, image, position):
        self.render_screen.screen.blit(image, position)

    def ChangeState(self, new_state):
        self.current_state = new_state

    def Loop(self):
        while self.running:
            self.current_state.HandleEvents()
            self.current_state.Update()
            self.current_state.DrawScreen()
            self.current_state.UpdateDisplay()
            self.current_state.HandleFPS()
