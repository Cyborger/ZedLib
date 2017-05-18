""" A sprite that has constant movement each frame and shows when collided"""
import ZedLib


class Projectile(ZedLib.GameSprite):
    def __init__(self, image, x_vel, y_vel, max_vel=None, x=0, x=0):
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
