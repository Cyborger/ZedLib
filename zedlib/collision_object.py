import pygame


class CollisionObject:
    def __init__(self, width, height, x=0, y=0):
        self.rect = pygame.Rect(x, y, width, height)

    def horizontal_collide(self, sprite):
        """ Stops sprite from walking through this object on x-axis """
        if sprite.move_x > 0.0:
            sprite.rect.right = self.rect.left
        elif sprite.move_x < 0.0:
            sprite.rect.left = self.rect.right

    def vertical_collide(self, sprite):
        """ Stops sprite from going through this object on y-axis """
        if sprite.move_y > 0.0:
            sprite.rect.bottom = self.rect.top
        elif sprite.move_y < 0.0:
            sprite.rect.top = self.rect.bottom
