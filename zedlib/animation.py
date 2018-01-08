import zedlib

class Animation:
    """ A series of images that can be traversed """

    def __init__(self, image_set, ms_delta=0, looping=True):
        self.frames = image_set
        self.current_frame_n = 0
        self.looping = looping
        self.time_dependent = ms_delta > 0
        self.timer = zedlib.LappingTimer(ms_delta)

    def on_first_frame(self):
        """ Returns true if the animation is on the first frame """
        return self.current_frame_n == 0

    def on_last_frame(self):
        """ Returns true if the animation is on the last frame """
        return self.current_frame_n == len(self.frames) - 1

    def frames_from_end(self):
        """ Get number of frames until end of animation """
        return len(self.frames) - (self.current_frame_n + 1)

    def get_current_frame(self):
        """ Get the current image of the animation """
        return self.get_frame(self.current_frame_n)

    def get_frame(self, frame_number):
        """ Get a frame from its index """
        return self.frames[frame_number]

    def restart(self):
        """ Go back to the first frame """
        self.current_frame_n = 0

    def update(self, delta=0):
        """ Go to the next image """
        if self.time_dependent:
            self.timer.update(delta)
            for _ in range(self.timer.laps_complete):
                self.increment_frame()
                self.timer.decrease_laps()
        else:
            self.current_frame_n += 1
            if self.current_frame_n > len(self.frames) - 1:
                self.reached_end()

    def reached_end(self):
        """ Called when animation reaches end of frames """
        if self.looping:
            self.current_frame_n = 0
        else:
            self.current_frame_n = len(self.frames) - 1
