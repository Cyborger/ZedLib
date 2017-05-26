""" The GameState class should be inherited when you want to make different
parts of the game (main menu, pause menu, actual gameplay, etc). The class
itself contains a number of functions that will be called each loop
    HandleEvents()
    Update()
    DrawScreen()
    UpdateDisplay()
    HandleFPS()
but also contains functions that make tasks easier, like getting the mouse
position"""
import pygame


class GameState:
    def __init__(self, game):
        self.game = game
        self.buttons = []
        self.splashes = []
        self.fps = 60

    # Handle different types of events
    def HandleEvents(self):
        events = pygame.event.get()
        self.HandleBasicEvents(events)

    # Update sprites
    def Update(self):
        pass

    # Clear screen for next draw
    def ClearScreen(self):
        self.game.screen.fill((0, 0, 0))

    # Draw sprites and images
    def DrawScreen(self):
        pass

    # Scale screen then update the actual display
    def UpdateDisplay(self):
        new_width = self.game.render_screen.width
        new_height = self.game.render_screen.height
        scaled_screen = pygame.transform.scale(self.game.screen,
                                               (new_width, new_height))
        self.game.render_screen.screen.blit(scaled_screen, (0, 0))
        pygame.display.flip()

    def HandleFPS(self):
        self.game.clock.tick(self.fps)

# ------------------------------------------------------------------------------
    # Just deal with window closing
    def HandleBasicEvents(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.game.running = False
            elif event.type == pygame.VIDEORESIZE:
                self.game.render_screen.Resize(event.w, event.h)

    # Deal with mouse button presses
    def HandleMouseEvents(self, events):
        left_click = 1
        middle_click = 2
        right_click = 3
        for event in events:
            if (event.type == pygame.MOUSEBUTTONDOWN
                    and event.button == left_click):
                for button in self.buttons:
                    button.CheckPress()
            elif (event.type == pygame.MOUSEBUTTONUP
                    and event.button == left_click):
                for button in self.buttons:
                    button.CheckRelease()

    # Get accurate mouse pos
    def GetMousePosition(self):
        unscaled_mouse_pos = pygame.mouse.get_pos()
        x_modifier = self.game.screen_width / self.game.render_screen.width
        y_modifier = self.game.screen_height / self.game.render_screen.height
        mouse_pos = (unscaled_mouse_pos[0] * x_modifier,
                     unscaled_mouse_pos[1] * y_modifier)
        return mouse_pos

    def UpdateButtons(self):
        mouse_pos = self.GetMousePosition()
        for button in self.buttons:
            button.Update(mouse_pos)

    def AddSplashes(self, *splashes):
        for splash in splashes:
            self.splashes.append(splash)

    def AddButtons(self, *buttons):
        for button in buttons:
            self.buttons.append(button)

    def DrawSplashes(self):
        for splash in self.splashes:
            self.game.screen.blit(splash.image, splash.rect)

    def DrawButtons(self):
        for button in self.buttons:
            self.game.screen.blit(button.image, button.rect)

    # Change the FPS of the state
    def SetFPS(self, new_fps):
        self.fps = new_fps
