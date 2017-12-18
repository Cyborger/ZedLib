import pygame
from zedlib import render_window
from zedlib import game_state


class Game:
    """ Main class that handles the game window and all the game states """
    def __init__(self, screen_width, screen_height, fullscreen=False):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_middle = [self.screen_width /2, self.screen_height / 2]
        self.screen = pygame.Surface((self.screen_width, self.screen_height))
        self.render_window = render_window.RenderWindow(self.screen_width,
                                                        self.screen_height,
                                                        fullscreen)
        self.current_state = game_state.GameState(self)
        self.clock = pygame.time.Clock()
        self.running = True

    def change_state(self, new_state):
        """ Update the current state that is running """
        self.current_state = new_state

    def loop(self):
        """ Calls main functions every frame """
        while self.running:
            self.current_state.handle_events()
            self.current_state.handle_input()
            self.current_state.update()
            self.current_state.clear_screen()
            self.current_state.draw_screen()
            self.update_display()
            self.current_state.handle_fps()

    def update_display(self):
        """ Scale the screen then update the screen """
        dimensions = self.render_window.get_dimensions()
        scaled_screen = pygame.transform.scale(self.screen, dimensions)
        self.render_window.screen.blit(scaled_screen, (0, 0))
        pygame.display.flip()
