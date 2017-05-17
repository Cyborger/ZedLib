""" Create animations that change can be used to switch between images of a
list passed. Can be looping or not, but can also require to be changed
manually or to change based on time passed (DeltaAnimation)."""
import ZedLib


class Animation:
    def __init__(self, frames, looping=True):
        self.frames = frames
        self.current_frame_n = 0
        self.looping = looping

    def GetFrameImage(self):
        return self.frames[self.current_frame_n]

    def IncrementFrame(self):
        self.current_frame_n += 1
        if self.current_frame_n > len(self.frames) - 1:
            self.ReachedEnd()

    def DecreaseFrame(self):
        self.current_frame_n -= 1
        if self.current_frame_n < 0:
            self.ReachedStart()

    def ReachedStart(self):
        if self.looping:
            self.current_frame_n = len(self.frames) - 1
        else:
            self.current_frame_n = 0

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
