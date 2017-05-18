"""Generic gamesprite for anything involving movement"""


class GameSprite:
    def __init__(self, image, x=0, y=0):
        self.image = image
        self.rect = self.image.get_rect()
        self.move_x = 0
        self.move_y = 0
