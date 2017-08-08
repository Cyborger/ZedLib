import pygame


class Camera:
    """ A camera that follows a given rect"""
    def __init__(self, screen_width, screen_height,
                 location_width=0, location_height=0):
        self.rect = pygame.Rect(0, 0, location_width, location_height)
        self.screen_width = screen_width
        self.half_screen_width = self.screen_width / 2
        self.screen_height = screen_height
        self.half_screen_height = self.screen_height / 2

    def ApplyToRect(self, target_rect):
        """ Return rect at an offset to the currently targeted rect """
        updated_rect = target_rect.move(self.rect.left, self.rect.top)
        return updated_rect

    def UpdateLocationSize(self, location_width, location_height):
        """ Change dimensions of the location """
        self.rect.width = location_width
        self.rect.height = location_height

    def UpdateTarget(self, target_rect):
        """ Update the rect that the camera is following """
        left, top, _, _ = target_rect
        _, _, width, height = self.rect
        left, top, _, _ = (-left + self.half_screen_width,
                           -top + self.half_screen_height, width, height)

        left = min(0, left)
        left = max(-(self.rect.width - self.screen_width), left)
        top = max(-(self.rect.height - self.screen_height), top)
        top = min(0, top)
        self.rect = pygame.Rect(left, top, width, height)
