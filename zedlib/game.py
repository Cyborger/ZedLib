import pygame
from zedlib import render_window
from zedlib import game_state


class Game:
    """ Main class that handles the game window and all the game states """
    def __init__(self, screen_width, screen_height, fullscreen=False):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_size = (self.screen_width, self.screen_height)
        self.screen = pygame.Surface((self.screen_width, self.screen_height))

        self.render_window = render_window.\
                RenderWindow(self.screen_width, self.screen_height, fullscreen)
                
        self.current_state = game_state.GameState(self)
        self.clock = pygame.time.Clock()
        self.running = True

    def change_state(self, new_state):
        """ Update the current state that is running """
        self.current_state = new_state

    def loop(self):
        """ Calls main functions every frame """
        while self.running:
            self.current_state.handle_events(pygame.event.get())
            self.current_state.handle_input()
            self.current_state.update()
            self.clear_screen()
            self.current_state.draw_screen()
            self.update_display()
            self.current_state.handle_fps()

    def clear_screen(self):
        self.screen.fill((0, 0, 0))

    def update_display(self):
        """ Scale the screen then update the display """
        dimensions = self.render_window.get_window_size()
        scaled_screen = pygame.transform.scale(self.screen, dimensions)
        self.render_window.screen.blit(scaled_screen, (0, 0))

        pygame.display.flip()

    def get_mouse_position(self):
        """ Get scaled position of the mouse """
        unscaled_mouse_pos = pygame.mouse.get_pos()

        screen_w = self.screen_width
        render_screen_w = self.render_window.get_window_size()[0]
        x_modifier = screen_w / render_screen_w
        x_pos = unscaled_mouse_pos[0] * x_modifier

        screen_h = self.screen_height
        render_screen_h = self.render_window.get_window_size()[1]
        y_modifier = screen_h / render_screen_h
        y_pos = unscaled_mouse_pos[1] * y_modifier

        return (x_pos, y_pos)
