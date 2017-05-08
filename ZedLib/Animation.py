import ImageLoading
import Timer

class Animation:
  def __init__(self, sprite, frames, looping=True):
    self.sprite = sprite
    self.frames = frames
    self.current_frame_n = 0
    self.frame_image = None
    self.looping = looping
    
  def IncrementFrame(self):
    self.current_frame_n += 1
    if self.current_frame_n > len(self.frames):
      self.ReachedEnd()
    self.frame_image = self.frames[self.current_frame_n]
    self.sprite.image = self.frame_image
    
  def ReachedEnd(self):
    if self.looping:
      self.current_frame_n = 0
    else:
      self.current_frame_n = len(self.frames)

    
class DeltaAnimation():
  def __init__(self, sprite, frames, looping=True, ms_delay):
    super().__init__(sprite, frames, looping)
    self.timer = Timer.LappingTimer(ms_delay)
    
  def Update(self, delta):
    self.timer.Update(delta)
    for i range(self.timer.num_of_laps):
      self.IncrementFrame()
      self.timer.num_of_laps -= 1
    
    
    
