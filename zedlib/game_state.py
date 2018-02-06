import pygame


class GameState:
    def __init__(self, game):
        self.game = game
        self.fps = 60
        self.delta = 0

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4:
                    self.game.running = False

    def handle_input(self):
        pass

    def update(self):
        pass

    def clear_screen(self):
        self.game.screen.fill((0, 0, 0))

    def draw_screen(self):
        pass

    def handle_fps(self):
        """ Control the amount of updates called per second """
        self.delta = self.game.clock.tick(self.fps)

    def set_fps(self, new_fps):
        """ Change the rate at which updates are called """
        self.fps = new_fps
