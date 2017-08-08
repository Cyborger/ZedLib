import ZedLib


class Projectile(ZedLib.GameSprite):
    """ GameSprite that moves at a given angle """
    def __init__(self, image, angle=0.0, speed=0.0, x=0.0, y=0.0):
        super().__init__(image, x, y)
        self.speed = speed
        self.angle = angle
        self.x_velocity = 0.0
        self.y_velocity = 0.0
        self.CalculateMovement()

    def ChangeAngle(self, new_angle):
        self.angle = angle
        self.CalculateMovement()

    def ChangeSpeed(self, new_speed):
        self.speed = new_speed
        self.CalculateMovement()

    def CalculateMovement(self):
        self.x_velocity, self.y_velocity = self.GetMovementOnAngle(self.angle, self.speed)

    def InvertHorizontally(self):
        self.x_velocity *= -1

    def InvertVertically(self):
        self.y_velocity *= -1
