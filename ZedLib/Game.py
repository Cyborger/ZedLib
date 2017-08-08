import pygame
from ZedLib import RenderWindow
from ZedLib import GameState

class Game:
    """ Core class that handles the game window and all of the game states"""
    def __init__(self, screen_width, screen_height, fullscreen=False):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_middle = [self.screen_width / 2, self.screen_height / 2]
        self.screen = pygame.Surface((self.screen_width, self.screen_height))
        self.render_screen = RenderWindow.RenderWindow(self.screen_width,
                                                       self.screen_height,
                                                       fullscreen)
        self.current_state = None
        self.empty_game_state = GameState.GameState(self)
        self.ChangeState(self.empty_game_state)
        self.clock = pygame.time.Clock()
        self.running = True

    def ChangeState(self, new_state):
        """ Update the current state that is running """
        self.current_state = new_state

    def Loop(self):
        """ Calls needed functions every frame """
        while self.running:
            self.current_state.HandleEvents()
            self.current_state.Update()
            self.ClearScreen()
            self.current_state.DrawScreen()
            self.UpdateDisplay()
            self.current_state.HandleFPS()

    def ClearScreen(self):
        """ Clear the screen with black """
        self.screen.fill((0, 0, 0))

    def UpdateDisplay(self):
        """ Scale the screen then blit it to the display """
        new_width = self.render_screen.current_width
        new_height = self.render_screen.current_height
        scaled_screen = pygame.transform.scale(self.screen,
                                               (new_width, new_height))
        self.render_screen.screen.blit(scaled_screen, (0, 0))
        pygame.display.flip()
