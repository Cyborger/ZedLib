import ZedLib


class Spritesheet:
    """ An image that can be split into sets of images """
    def __init__(self, file_path, tiles_wide, tiles_high,
                 scale=1, x_offset=0, y_offset=0):
        self.image = ZedLib.LoadImage(file_path, scale)
        self.tiles_wide = tiles_wide
        self.tiles_high = tiles_high
        self.tile_width = self.image.get_width() / self.tiles_wide
        self.tile_height = self.image.get_height() / self.tiles_high

    # Get a subsurface at a specified tile
    def GetImage(self, x, y):
        """ Get image from spritesheet usings coordinates of the tile """
        image_width = x * self.tile_width
        image_height = y * self.tile_height
        new_image = self.image.subsurface((image_width, image_height,
                                           self.tile_width, self.tile_height))
        return new_image

    def GetHorizontalStrip(self, y):
        """ Get a horizontal strip of images using the length of the spritesheet """
        strip = []
        for x in range(self.tiles_wide):
            image = self.GetImage(x, y)
            strip.append(image)
        return strip

    def GetVerticalStrip(self, x):
        """ Get a vertical strip of images using the height of the spritesheet """
        strip = []
        for y in range(self.tiles_high):
            image = self.GetImage(x, y)
            strip.append(image)
        return strip


class ButtonSpritesheet(Spritesheet):
    """ Spritesheet with default tile grid """
    def __init__(self, file_path, scale=1, x_offset=0, y_offset=0):
        super().__init__(file_path, 1, 3, scale, x_offset,
                         y_offset)
