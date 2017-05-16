import ZedLib


class Animation:
    def __init__(self, frames, looping=True):
        self.frames = frames
        self.current_frame_n = 0
        self.frame_image = None
        self.looping = looping
        self.needs_update = True

    def GetFrameImage(self):
        if self.needs_update:
            self.needs_update = False
            return self.frames[self.current_frame_n]

    def IncrementFrame(self):
        self.current_frame_n += 1
        if self.current_frame_n > len(self.frames) - 1:
            self.ReachedEnd()
        self.needs_update = True

    def DecreaseFrame(self):
        self.current_frame_n -=1
        if self.current_frame_n < 0:
            self.current_frame_n = 0
        self.needs_update = True

    def ReachedEnd(self):
        if self.looping:
            self.current_frame_n = 0
        else:
            self.current_frame_n = len(self.frames) - 1


class DeltaAnimation(Animation):
    def __init__(self,  frames, ms_delay, looping=True):
        super().__init__(frames, looping)
        self.timer = ZedLib.LappingTimer(ms_delay)

    def Update(self, delta):
        self.timer.Update(delta)
        for i in range(self.timer.laps_complete):
            self.IncrementFrame()
            self.timer.laps_complete -= 1
