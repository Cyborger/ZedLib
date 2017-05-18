"""Generic gamesprite for anything involving movement"""
import ZedLib


class GameSprite:
    def __init__(self, image, x=0, y=0):
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = ZedLib.Position(x, y)
        self.move_x = 0
        self.move_y = 0

    def UpdatePosition(self):
        self.pos.GetRectPosition(self.rect)
