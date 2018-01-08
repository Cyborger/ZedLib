import zedlib
import pygame


class Surface:
    """ An image with a rect """
    def __init__(self, image, x=0, y=0):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface, camera=None):
        """ Draw image on another surface """
        if camera:
            surface.blit(self.image, camera.apply(self.rect))
        else:
            surface.blit(self.image, self.rect)

    def center_horizontal(self, rect):
        """ Center rect horizontally by the center of a given rect """
        self.rect.centerx = rect.centerx

    def center_vertical(self, rect):
        """ Center rect vertically by the center of a given rect """
        self.rect.centery = rect.centery
