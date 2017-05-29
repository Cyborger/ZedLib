""" A GameSprite that has gravity"""
import ZedLib


class PhysicsSprite(ZedLib.GameSprite):
    def __init__(self, image, x=0.0, y=0.0):
        super().__init__(image, x, y)
        self.gravity = 0.1
        self.max_y_velocity = 9.0
        self.jump_force = -5.0
        self.can_jump = False

    def UpdateGravity(self):
        self.y_velocity += self.gravity
        if self.y_velocity > self.max_y_velocity:
            self.y_velocity = self.max_y_velocity
        self.move_y += self.y_velocity


    def HitGround(self):
        self.y_velocity = 0.0
        self.can_jump = True

    def Jump(self):
        if self.can_jump:
            self.y_velocity = self.jump_force
            self.can_jump = False
