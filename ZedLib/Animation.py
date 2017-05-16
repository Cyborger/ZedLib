import ZedLib


class Animation:
    def __init__(self, sprite, frames, looping=True):
        self.sprite = sprite
        self.frames = frames
        self.current_frame_n = 0
        self.frame_image = None
        self.looping = looping

    def IncrementFrame(self):
        self.current_frame_n += 1
        if self.current_frame_n > len(self.frames) - 1:
            self.ReachedEnd()
        self.frame_image = self.frames[self.current_frame_n]
        self.sprite.image = self.frame_image

    def DecreaseFrame(self):
        self.current_frame_n -=1
        if self.current_frame_n < 0:
            self.current_frame_n = 0
        self.frame_image = self.frames[self.current_frame_n]
        self.sprite.image = self.frame_image

    def ReachedEnd(self):
        if self.looping:
            self.current_frame_n = 0
        else:
            self.current_frame_n = len(self.frames) - 1


class DeltaAnimation(Animation):
    def __init__(self, sprite, frames, ms_delay, looping=True):
        super().__init__(sprite, frames, looping)
        self.timer = ZedLib.LappingTimer(ms_delay)

    def Update(self, delta):
        self.timer.Update(delta)
        for i in range(self.timer.laps_complete):
            self.IncrementFrame()
            self.timer.laps_complete -= 1
