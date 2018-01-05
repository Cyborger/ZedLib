import zedlib
import pytmx


class TMXData:
    def __init__(self, file_path):
        self.data = pytmx.load_pygame(file_path)
        self.properties = self.data.properties
        self.tile_width = self.data.tilewidth
        self.tile_height = self.data.tileheight
        self.tiles_wide = self.data.width
        self.tiles_high = self.data.height
        self.map_width = self.tile_width * self.tiles_wide
        self.map_height = self.tile_height * self.tiles_high

        self.tile_layers = []
        self.object_layers = []

        self.load()

    def get_layer(self, layer_name):
        """ Get a layer by its name """
        for layer in self.data.layers:
            if layer.name == layer_name: return layer

    def load(self):
        """ Load all the tmx data """
        for layer in self.data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                self.tile_layers.append(layer)

            elif isinstance(layer, pytmx.TiledObjectGroup):
                self.object_layers.append(layer)


def load_tmx(file_path):
    """ Get a TMXData object using given file path """
    tmx_data = TMXData(file_path)
    return tmx_data
