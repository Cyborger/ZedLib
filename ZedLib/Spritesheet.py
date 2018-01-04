import zedlib


class Spritesheet:
    def __init__(self, file_path, tiles_wide, tiles_high, scale=1,
                 x_offset=0, y_offset=0):
        self.image = zedlib.load_image(file_path, scale)
        self.tiles_wide = tiles_wide
        self.tiles_high = tiles_high
        self.tile_width = self.image.get_width() / self.tiles_wide
        self.tile_height = self.image.get_height() / self.tiles_high

    def get_image(self, x, y):
        """ Get a subsurface at a given tile coordinate """
        image_x = x * self.tile_width
        image_y = y * self.tile_height
        image = self.image.subsurface((image_x, image_y, self.tile_width,
                                       self.tile_height))
        return image

    def get_horizontal_strip(self, y):
        """ Get a list of images from a horizontal strip """
        images = []
        for x in range(self.tiles_wide):
            image = self.get_image(x, y)
            images.append(image)
        return images

    def get_vertical_strip(self, x):
        """ Get a list of images from a vertical strip """
        images = []
        for y in range(self.tiles_high):
            image = self.get_image(x, y)
            images.append(image)
        return images

    def get_first_image(self):
        """ Get the top left image of the spritesheet """
        return self.get_image(0, 0)
