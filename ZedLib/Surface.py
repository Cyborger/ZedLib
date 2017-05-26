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

class StandAloneSurface:
    def __init__(self, file_path, x=0, x=0, scale=1):
        image = ZedLib.LoadImage(file_path, scale)
        super().__init__(image, x, y)
