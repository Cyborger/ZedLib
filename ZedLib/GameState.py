import pygame

class GameState:
    def __init__(self, game):
        self.game = game
        self.buttons = []

    def HandleEvents(self):
        events = pygame.event.get()
        self.HandleBasicEvents(events)

    def Update(self):
        pass

    def HandleBasicEvents(events):
        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                self.game.running = False

    def HandleMouseEvents(events):
        for event in events:
            if event.type ==
