""" A basic collision object that stops sprites from walking through it"""
import pygame
import ZedLib

class CollisionObject:
    def __init__(self, width, height, x=0, y=0):
        self.image = pygame.Surface((width , height))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def HorizontalCollide(self, sprite):
        if sprite.move_x > 0.0:
            sprite.rect.right = self.rect.left
        elif sprite.move_x < 0.0:
            sprite.rect.left = self.rect.right

    def VerticalCollide(self, sprite):
        if sprite.move_y > 0.0:
            sprite.rect.bottom = self.rect.top
            if isinstance(sprite, ZedLib.PhysicsSprite):
                sprite.HitGround()
        elif sprite.move_y < 0.0:
            sprite.rect.top = self.rect.bottom
