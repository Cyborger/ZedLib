import pygame

class Spritesheet:
    def __init__(self, file_path, tiles_wide, tiles_high, scale = 1, x_offset = 0, y_offset = 0):
        self.image = LoadImage(file_path, scale)
        self.tiles_wide = tiles_wide
        self.tiles_high = tiles_high
        self.tile_width = self.image.get_width() / self.tiles_wide
        self.tile_height = self.image.get_height() / self.tiles_high
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.frames = []
        for y in range(self.tiles_wide):
            for x in range(self.tiles_high):
                next_frame = self.GetImage(x, y)
                self.frames.append(next_frame)

    def GetImage(self, x, y):
        new_image = self.image.subsurface((x * self.tile_width + self.x_offset,
                                           y * self.tile_height + self.y_offset,
                                           self.tile_width, self.tile_height))
        return new_image

class Surface:
    def __init__(self, file_path, x=0, y=0, scale=1):
        self.image = LoadImage(file_path, scale)
        self.rect = self.image.get_rect()
        self.SetPosition(x, y)

    def SetPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y

def LoadImage(self, file_path, scale = 1):
    image = pygame.image.load(file_path).convert_alpha()
    if scale != 1:
        pygame.transform.scale(image, (image.current_w * scale, image.current_h * scale),
                               image)
    return image
