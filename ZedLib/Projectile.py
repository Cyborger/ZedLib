""" A sprite that has constant movement each frame and shows when collided"""
import ZedLib


class Projectile(ZedLib.GameSprite):
    def __init__(self, image, x=0, y=0):
        super().__init__(image, x, y)
        self.x_velocity = 0.0
        self.y_velocity = 0.0

    def UpdateMovement(self):
        pass


class AxisProjectile(Projectile):
    def __init__(self, image, axis, speed, x=0, y=0):
        super().__init__(image, x, y)
        if axis == 'x':
            self.x_velocity = speed
        elif axis == 'y':
            self.y_velocity = speed
        else:
            print("invalid axis for a projectile")

    def UpdateMovement(self):
        self.pos.MoveX(self.x_velocity)
        self.pos.MoveY(self.y_velocity)


class AngledProjectile(Projectile):
    def __init__(self, image, angle, velocity, x=0, x=0):
        super().__init__(image, x, y)
        self.max_vel = max_vel
        self.x_velocity = 0.0
        self.y_velocity = 0.0

    def UpdateMovement(self):
        if self.max_vel is None:
            self.pos.Move(self.x_velocity, self.y_velocity)
        else:
            self.pos.MoveDiagonal(self.x_velocity, self.y_velocity,
                                  self.max_vel)
        self.UpdatePosition()
