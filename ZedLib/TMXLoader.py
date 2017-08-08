import ZedLib
import pytmx

class TMXData:
    def __init__(self, file_path):
        self.data = pytmx.load_pygame(file_path)
        self.tile_width = self.data.tilewidth
        self.tile_height = self.data.tileheight
        self.n_tiles_wide = self.data.width
        self.n_tiles_high = self.data.height
        self.map_width = self.tile_width * self.n_tiles_wide
        self.map_height = self.tile_height * self.n_tiles_high
        self.tile_layers = []
        self.object_layers = []
        self.Load()

    def Load(self):
        for layer in self.data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                new_tile_layer = TMXTileLayer(layer)
                self.tile_layers.append(new_tile_layer)

            elif isinstance(layer, pytmx.TiledObjectGroup):
                new_object_layer = TMXObjectLayer(layer)
                self.object_layers.append(new_object_layer)

    def GetMapProperty(self, property_name):
        value = self.data.properties.get(property_name)
        return value


class TMXLayer:
    def __init__(self, layer):
        self.layer = layer

    def GetProperty(self, property_name):
        value = layer.properties.get(property_name)
        return value


class TMXTileLayer(TMXLayer):
    def __init__(self, layer):
        super().__init__(layer)
        self.tiles = []
        self.Load()

    def Load(self):
        for x, y, image in self.layer.tiles():
            new_tile = ZedLib.Surface(image, x * self.tile_width,
                                      y * self.tile_height)
            self.tiles.append(new_tile)


class TMXObjectLayer:
    def __init__(self, layer):
        super().__init__(layer)
        self.objects = []

    def Load(self):
        self.objects.extend(self.layer)
