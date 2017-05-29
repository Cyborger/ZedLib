""" A sprite that has constant movement each frame and shows when collided"""
import ZedLib


class Projectile(ZedLib.GameSprite):
    def __init__(self, image, x=0.0, y=0.0):
        super().__init__(image, x, y)

    def UpdateMovement(self):
        self.pos.MoveX(self.x_velocity)
        self.pos.MoveY(self.y_velocity)
        self.UpdatePosition()


class AxisProjectile(Projectile):
    def __init__(self, image, axis, speed, x=0.0, y=0.0):
        super().__init__(image, x, y)
        if axis == 'x':
            self.x_velocity = speed
        elif axis == 'y':
            self.y_velocity = speed
        else:
            print("invalid axis for a projectile")


class AngledProjectile(Projectile):
    def __init__(self, image, angle, velocity, x=0.0, y=0.0):
        super().__init__(image, x, y)
        self.max_vel = velocity
        movement = self.GetMovementOnAngle(angle, self.max_vel)
        self.x_velocity = movement[0]
        self.y_velocity = movement[1]
