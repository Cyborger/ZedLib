import pygame


class GameState:
    def __init__(self, game):
        self.game = game
        self.fps = 60
        self.delta = 0

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False
        self.handle_other_events(events)

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

    def handle_other_events(self, events):
        pass

    def get_mouse_position(self):
        """ Get scaled position of the mouse """
        unscaled_mouse_pos = pygame.mouse.get_pos()

        screen_w = self.game.screen_width
        render_screen_w = self.game.render_screen.current_width
        x_modifier = screen_w / render_screen_w
        x_pos = unscaled_mouse_pos[0] * x_modifier

        screen_h = self.game.screen_height
        render_screen_h = self.game.render_screen.current_height
        y_modifier = screen_h / render_screen_h
        y_pos = unscaled_mouse_pos[1] * y_modifier

        return (x_pos, y_pos)

    def set_fps(self, new_fps):
        """ Change the rate at which updates are called """
        self.fps = new_fps
