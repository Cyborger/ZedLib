""" A GameSprite that has gravity"""
import ZedLib

class PhysicsSprite(ZedLib.GameSprite):
    def __init__(self, image, x=0, y=0):
        super().__init__(image, x, y)
        self.gravity = 0.1
        self.y_velocity = 0.0

    def UpdateGravity(self):
        self.y_velocity += self.gravity

    def HitGround(self):
        self.y_velocity = 0.0
