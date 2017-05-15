# Surfaces are for creating images like splash screens, not to replace
# loading images from pygame
import ZedLib

class Surface:
    def __init__(self, file_path, x=0, y=0, scale=1):
        self.image = ZedLib.LoadImage(file_path, scale)
        self.rect = self.image.get_rect()
        self.SetPosition(x, y)

    def SetPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y
