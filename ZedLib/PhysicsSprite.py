import ZedLib


class PhysicsSprite(ZedLib.GameSprite):
    """ Gamesprite with gravity """
    def __init__(self, image, x=0.0, y=0.0):
        super().__init__(image, x, y)
        self.gravity = 0.0
        self.max_y_velocity = 0.0

    def ApplyGravity(self):
        """ Increase the effect of gravity as the sprite falls """
        self.y_velocity += self.gravity
        if self.y_velocity > self.max_y_velocity:
            self.y_velocity = self.max_y_velocity
        self.move_y += self.y_velocity

    def HitGround(self):
        """ Set y_velocity to 0.0 and allow the sprite to jump again """
        self.y_velocity = 0.0
