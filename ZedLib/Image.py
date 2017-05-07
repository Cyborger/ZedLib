"""
For loading images and putting them into a certain
format; a spritesheet for animation or a scaled image with a rect.
"""
import pygame


# Spritesheets are made to be passed to animations.
# They hold the image itself, information such as tile width and height, and
# also hold an array of frames
class Spritesheet:
    def __init__(self, file_path, tiles_wide, tiles_high,
                 scale=1, x_offset=0, y_offset=0):
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

    # Get a subsurface at a specified tile
    def GetImage(self, x, y):
        image_width = x * self.tile_width
        image_height = y * self.tile_height
        new_image = self.image.subsurface((image_width, image_height,
                                           self.tile_width, self.tile_height))
        return new_image


# Surfaces are for creating images like splash screens, not to replace
# loading images from pygame
class Surface:
    def __init__(self, file_path, x=0, y=0, scale=1):
        self.image = LoadImage(file_path, scale)
        self.rect = self.image.get_rect()
        self.SetPosition(x, y)

    def SetPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y


# Should be used instead of pygame.image.load()
def LoadImage(self, file_path, scale=1):
    image = pygame.image.load(file_path).convert_alpha()
    if scale != 1:
        new_width = image.current_w * scale
        new_height = image.current_h * scale
        pygame.transform.scale(image, (new_width, new_height), image)
    return image
