import Spritesheet

class Animation:
  def __init__(self, sprite, frames):
    self.sprite = sprite
    self.frames = frames
    self.current_frame_n = 0
    self.frame_image = None
    
