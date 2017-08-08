import ZedLib


class Animation:
    """ A series of images that can be traversed through """
    def __init__(self, frame_set, looping=True):
        self.frames = frame_set
        self.current_frame_n = 0
        self.looping = looping

    def IsLastFrame(self):
        """ Returns true if the animation is on the last frame """
        if self.current_frame_n == len(self.frames) - 1:
            return True
        else:
            return False

    def IsFirstFrame(self):
        """ Returns true if the animation is on the first frame """
        if self.current_frame_n == 0:
            return True
        else:
            return False

    def FramesFromEnd(self):
        """ Number of frames until end of animation """
        frames_from_end = len(self.frames) - (current_frame_n + 1)
        return frames_from_end

    def GetCurrentFrame(self):
        """ Get the current image """
        return self.frames[self.current_frame_n]

    def IncrementFrame(self):
        """ Go to next image in set """
        self.current_frame_n += 1
        if self.current_frame_n > len(self.frames) - 1:
            self.__ReachedEnd()

    def DecreaseFrame(self):
        """ Go to previous image in set """
        self.current_frame_n -= 1
        if self.current_frame_n < 0:
            self.__ReachedStart()

    def __ReachedStart(self):
        if self.looping:
            self.current_frame_n = len(self.frames) - 1
        else:
            self.current_frame_n = 0

    def __ReachedEnd(self):
        if self.looping:
            self.current_frame_n = 0
        else:
            self.current_frame_n = len(self.frames) - 1


class DeltaAnimation(Animation):
    """ An animation that goes to the next frame from time passed """
    def __init__(self, frames, ms_delay, looping=True):
        super().__init__(frames, looping)
        self.timer = ZedLib.LappingTimer(ms_delay)

    def Update(self, delta):
        """ Add time passed and go to the next image if needed """
        self.timer.Update(delta)
        for i in range(self.timer.laps_complete):
            self.IncrementFrame()
            self.timer.laps_complete -= 1
