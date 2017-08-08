import pygame
import ZedLib


class CollisionObject:
    """ A rect that doesn't allow sprites to pass """
    def __init__(self, width, height, x=0, y=0):
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.x = x
        self.rect.y = y

    def HorizontalCollide(self, sprite):
        """ Pass sprite to stop it from walking over this object horizontally"""
        if sprite.move_x > 0.0:
            sprite.rect.right = self.rect.left
        elif sprite.move_x < 0.0:
            sprite.rect.left = self.rect.right

    def VerticalCollide(self, sprite):
        """ Pass sprite to stop it from walking over this object vertically"""
        if sprite.move_y > 0.0:
            sprite.rect.bottom = self.rect.top
            if isinstance(sprite, ZedLib.PhysicsSprite):
                sprite.HitGround()
        elif sprite.move_y < 0.0:
            sprite.rect.top = self.rect.bottom
            if isinstance(sprite, ZedLib.PhysicsSprite):
                sprite.y_velocity = 0.0
