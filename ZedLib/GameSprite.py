"""Generic gamesprite for anything involving movement"""
import ZedLib
import math
import pygame

class GameSprite:
    def __init__(self, image, x=0.0, y=0.0):
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = ZedLib.Position(x, y)
        self.move_x = 0.0
        self.move_y = 0.0
        self.x_velocity = 0.0
        self.y_velocity = 0.0
        self.speed = 0.0

    def UpdateRectPosition(self):
        self.pos.SetRectPosition(self.rect)

    def UpdateActualPosition(self):
        self.pos.x = self.rect.x
        self.pos.y = self.rect.y

    def GetMovementOnAngle(self, angle, distance):
        cos_angle = math.cos(math.radians(angle))
        x = cos_angle * distance
        sin_angle = math.sin(math.radians(angle))
        y = sin_angle * distance
        print("x: " + str(x))
        print("y: " + str(y))
        return (x, y)

    def GetMovementWithDiagonal(self, x, y, speed):
        angle = None
        if x > 0.0:
            if y > 0.0:
                angle = 315.0
            elif y < 0.0:
                angle = 45.0
            else:
                angle = 0.0
        elif x < 0.0:
            if y > 0.0:
                angle = 225.0
            elif y < 0.0:
                angle = 135.0
            else:
                angle = 180.0
        elif y > 0.0:
            angle = 270.0
        elif y < 0.0:
            angle = 90.0

        if angle is not None:
            movement = GetMovementOnAngle(angle, speed)

        return movement

    def UpdateHorizontalCollisions(self, collisions):
        self.UpdateRectPosition()
        objects_collided = pygame.sprite.spritecollide(self, collisions, False)
        for collision_object in objects_collided:
            collision_object.HorizontalCollide(self)
        self.UpdateActualPosition()

    def UpdateVerticalCollisions(self, collisions):
        self.UpdateRectPosition()
        objects_collided = pygame.sprite.spritecollide(self, collisions, False)
        for collision_object in objects_collided:
            collision_object.VerticalCollide(self)
        self.UpdateActualPosition()
