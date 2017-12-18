import zedlib


#TODO: Pretty much the entire class

class Button(zedlib.Surface):
    """ Updates based on mouse position and state of mouse buttons,
    calls given function on release """

    def __init__(self, image_path, function=None, scale=1, n_of_frames=3):
        self.spritesheet = zedlib.Spritesheet(image_path, n_of_frames, 1)
        super().__init__()
