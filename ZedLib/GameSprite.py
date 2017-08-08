import pygame
import ZedLib
import math

class GameSprite(ZedLib.CollisionObject):
    """ A generic sprite that can move """
    def __init__(self, image, x=0.0, y=0.0):
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = ZedLib.FloatPosition(self.rect, x, y)
        self.move_x = 0.0
        self.move_y = 0.0
        self.x_velocity = 0.0
        self.y_velocity = 0.0

    def UpdateMovement(self, collisions=[]):
        """ Move the sprite based on x_velocity and changes to GameSprite.move_(x/y) """
        self.move_x += self.x_velocity
        self.pos.MoveX(self.move_x)
        self.UpdateHorizontalCollisions(collisions)
        self.move_x = 0.0

        self.move_y += self.y_velocity
        self.pos.MoveY(self.move_y)
        self.UpdateVerticalCollisions(collisions)
        self.move_y = 0.0

    def UpdateHorizontalCollisions(self, collisions):
        """ Stop sprite from moving through certain objects horizontally,
            collisions must be instances of CollisionObject """
        self.pos.UpdateRectX()
        objects_collided = pygame.sprite.spritecollide(self, collisions, False)
        for collision_object in objects_collided:
            collision_object.HorizontalCollide(self)
            self.pos.UpdatePositionX()
            self.HorizontalCollisionOccured(collision_object)

    def UpdateVerticalCollisions(self, collisions):
        """ Stop sprite from moving through certain objects vertically,
            collisions must be instances of CollisionObject """
        self.pos.UpdateRectY()
        objects_collided = pygame.sprite.spritecollide(self, collisions, False)
        for collision_object in objects_collided:
            collision_object.VerticalCollide(self)
            self.pos.UpdatePositionY()
            self.VerticalCollisionOccured(collision_object)

    def VerticalCollisionOccured(self, collision_object):
        pass

    def HorizontalCollisionOccured(self, collision_object):
        pass

    def GetMovementOnAngle(self, angle, distance):
        """ Get x and y distance based on angle and distance """
        cos_angle = math.cos(math.radians(angle))
        x = cos_angle * distance
        sin_angle = math.sin(math.radians(angle))
        y = sin_angle * distance
        return (x, y)
