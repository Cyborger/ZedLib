import pygame


class GameState:
    """ Represents a different style or menu of a game, inherit this class
        and change the core functions"""
    def __init__(self, game):
        self.game = game
        self.buttons = []
        self.surfaces = []
        self.fps = 60
        self.delta = 0

    def HandleEvents(self):
        """ Calls all the event functions """
        events = pygame.event.get()
        self.HandleBasicEvents(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.HandleKeyDownEvent(event.key)

    def Update(self):
        """ Override to choose what to update every frame """
        self.UpdateButtons()
        self.UpdateSprites()

    def DrawScreen(self):
        self.DrawSprites()
        self.DrawButtons()
        self.DrawSurfaces()

    def HandleFPS(self):
        """ Set the rate at which the game loop runs """
        self.delta = self.game.clock.tick(self.fps)

# ------------------------------------------------------------------------------
    def HandleBasicEvents(self, events):
        """ Deal with basic events such as window closing and resizing """
        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.game.running = False
            elif event.type == pygame.VIDEORESIZE:
                self.game.render_screen.ResizeWindow(event.w, event.h)

    def HandleKeyDownEvent(self, key):
        pass

    def GetMousePosition(self):
        """ Get mouse position on screen """
        unscaled_mouse_pos = pygame.mouse.get_pos()

        screen_width = self.game.screen_width
        render_screen_width = self.game.render_screen.current_width
        x_modifier = screen_width / render_screen_width

        screen_height = self.game.screen_height
        render_screen_height = self.game.render_screen.current_height
        y_modifier = screen_height / render_screen_height

        mouse_pos = (unscaled_mouse_pos[0] * x_modifier,
                     unscaled_mouse_pos[1] * y_modifier)
        return mouse_pos

    def UpdateSprites(self):
        pass

    def UpdateButtons(self):
        """ Update the state of all buttons using the state of the mouse """
        mouse_pos = self.GetMousePosition()
        left_mouse_button_pressed = pygame.mouse.get_pressed()[0]
        for button in self.buttons:
            button.Update(mouse_pos, left_mouse_button_pressed)


    def AddButtons(self, *buttons):
        """ Add buttons to GameState.buttons """
        for button in buttons:
            self.buttons.append(button)

    def AddSurfaces(self, *surfaces):
        """ Add surfaces to GameState.surfaces """
        for surface in surfaces:
            self.surfaces.append(surface)

    def DrawSprites(self):
        pass

    def DrawSurfaces(self):
        for surface in self.surfaces:
            self.game.screen.blit(surface.image, surface.rect)

    def DrawButtons(self):
        """ Draw all the buttons in GameState.buttons """
        for button in self.buttons:
            self.game.screen.blit(button.image, button.rect)

    def SetFPS(self, new_fps):
        """ Change the rate at which the game loop runs """
        self.fps = new_fps
