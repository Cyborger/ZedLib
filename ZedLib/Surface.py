"""Surfaces for creating images like splash screens"""
import ZedLib


class Surface:
    def __init__(self, image, x=0, y=0):
        self.image = image
        self.rect = self.image.get_rect()
        self.SetPosition(x, y)

    def SetPosition(self, x, y):
        self.SetPositionX(x)
        self.SetPositionY(y)

    def SetPositionX(self, x):
        self.rect.x = x

    def SetPositionY(self, y):
        self.rect.y = y

    def PlaceInCenter(self, surface, x_offset=0, y_offset=0):
        self.PlaceInCenterX(surface, x_offset)
        self.PlaceInCenterY(surface, y_offset)

    def PlaceInCenterX(self, surface, offset=0):
        self.SetPositionX((surface.get_width() / 2 - self.rect.width / 2) +
                          offset)

    def PlaceInCenterY(self, surface, offset=0):
        self.SetPositionY((surface.get_height() / 2 - self.rect.height / 2) +
                          offset)

class StandAloneSurface(Surface):
    def __init__(self, file_path, x=0, y=0, scale=1):
        image = ZedLib.LoadImage(file_path, scale)
        super().__init__(image, x, y)
