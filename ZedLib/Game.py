import pygame

class Game:
    def __init__(self, screen_width, screen_height):
        pygame.__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.Surface((self.screen_width, self.screen_height))
        self.display_info = pygame.display.Info()
        self.rendering_screen = pygame.display.set_mode(
                                               (self.display_info.current_w,
                                                self.display_info.current_h))
        self.current_state = None
        self.running = True

    def ChangeState(self, new_state):
        self.current_state = new_state

    def Loop(self):
        while self.running:
            self.current_state.HandleEvents()
            self.current_state.Update()
            self.current_state.DrawScreen()
            self.current_state.UpdateDisplay()
            self.current_state.HandleFPS()
