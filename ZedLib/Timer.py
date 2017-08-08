class Timer:
    """ A timer that can keep track of timed passed """
    def __init__(self, delay):
        self.delay = delay
        self.complete = False
        self.time_passed = 0

    def Update(self, delta):
        """ Update time passed """
        self.time_passed += delta
        if self.time_passed >= self.delay:
            self.time_passed = self.delay
            self.complete = True

    def Reset(self):
        """ Reset the timer to the beginning """
        self.time_passed = 0
        self.complete = False


class LappingTimer:
    """ A timer that keeps track of time and continues on after it reaches the
        end, but keeps track of how many times it has lapped """
    def __init__(self, lap_time):
        self.lap_time = lap_time
        self.time_passed = 0
        self.laps_complete = 0

    def Update(self, delta):
        """ Update time passed """
        self.time_passed += delta
        while self.time_passed >= self.lap_time:
            self.time_passed -= self.lap_time
            self.laps_complete += 1

    def Reset(self):
        """ Reset the timer to the beginning """
        self.laps_complete = 0
        self.time_passed = 0

    def DecreaseLaps(self, amount=1):
        """ Decrease the counter for times the timer has completed """
        self.laps_complete -= 1
        if self.laps_complete < 0:
            self.laps_complete = 0


class CountingTimer:
    def __init__(self):
        self.time_passed = 0

    def Update(self, delta):
        self.time_passed += delta

    def Reset(self):
        self.time_passed = 0
