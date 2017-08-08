import ZedLib
import pygame

class Surface:
    """ An image with a rect, usually used for things like splashes """
    def __init__(self, image, x=0, y=0):
        self.image = image
        self.rect = self.image.get_rect()
        self.SetPosition(x, y)

    def SetPosition(self, x, y):
        """ Move the the surface to the given coordinates """
        self.SetPositionX(x)
        self.SetPositionY(y)

    def SetPositionX(self, x):
        """ Move the surface horizontally to the given x value """
        self.rect.x = x

    def SetPositionY(self, y):
        """ Move the surface vertically to the given y value """
        self.rect.y = y

    def PlaceInCenter(self, surface, x_offset=0, y_offset=0):
        """ Place the surface in the center of a pygame.Surface() """
        self.PlaceInCenterX(surface, x_offset)
        self.PlaceInCenterY(surface, y_offset)

    def PlaceInCenterX(self, surface, offset=0):
        """ Horizontally center the surface on a pygame.Surface() """
        self.SetPositionX((surface.get_width() / 2 - self.rect.width / 2) +
                          offset)

    def PlaceInCenterY(self, surface, offset=0):
        """ Vertically center the surface on a pygame.Surface() """
        self.SetPositionY((surface.get_height() / 2 - self.rect.height / 2) +
                          offset)
