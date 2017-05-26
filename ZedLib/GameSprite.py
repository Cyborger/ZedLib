"""Generic gamesprite for anything involving movement"""
import ZedLib
import math


class GameSprite:
    def __init__(self, image, x=0, y=0):
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = ZedLib.Position(x, y)
        self.move_x = 0
        self.move_y = 0
        self.speed = 0

    def UpdatePosition(self):
        self.pos.SetRectPosition(self.rect)

    def GetMovementOnAngle(self, angle, distance):
        cos_angle = math.cos(math.radians(angle))
        x = cos_angle * distance
        sin_angle = math.sin(math.radians(angle))
        y = sin_angle * distance
        print("x: " + str(x))
        print("y: " + str(y))
        return (x, y)

    def CalculateMovementWithDiagonal(self, x, y, speed):
        angle = None
        if x > 0:
            if y > 0:
                angle = 315
            elif y < 0:
                angle = 45
            else:
                angle = 0
        elif x < 0:
            if y > 0:
                angle = 225
            elif y < 0:
                angle = 135
            else:
                angle = 180
        elif y > 0:
            angle = 270
        elif y < 0:
            angle = 90

        if angle is not None:
            movement = GetMovementOnAngle(angle, speed)
            self.pos.MoveX(movement[0])
            self.pos.MoveY(movement[1])
