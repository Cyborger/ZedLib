class Stopwatch:
    """ Keeps track of time passed """
    def __init__(self):
        self.time_passed = 0

    def update(self, delta):
        """ Update time that has passed """
        self.time_passed += delta

    def reset(self):
        """ Reset stopwatch to the beginning """
        self.time_passed = 0

class Timer:
    """ Counts to given amount of time and stops counting when complete"""
    def __init__(self, ms_time):
        self.time = ms_time
        self.time_passed = 0
        self.complete = False

    def update(self, delta):
        """ Update time that has passed """
        self.time_passed += delta
        if self.time_passed >= self.time:
            self.time_passed = self.time
            self.complete = True

    def reset(self):
        """ Reset timer to the beginning """
        self.time_passed = 0
        self.complete = False


class LappingTimer:
    """ A timer that loops and keeps track of loops complete """
    def __init__(self, ms_time):
        self.lap_time = ms_time
        self.time_passed = 0
        self.laps_complete = 0

    def update(self, delta):
        """ Update time that has passed """
        self.time_passed += delta
        while self.time_passed >= self.lap_time:
            self.time_passed -= self.lap_time
            self.laps_complete += 1

    def reset(self):
        """ Reset timer to the beginning """
        self.time_passed = 0
        self.laps_complete = 0

    def decrease_laps(self, amount=1):
        """ Decrease the lap counter """
        self.laps_complete -= amount
        if self.laps_complete < 0:
            self.laps_complete = 0
