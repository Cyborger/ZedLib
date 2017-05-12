class Timer:
    def __init__(self, delay):
        self.delay = delay
        self.complete = False
        self.time_passed = 0

    def Update(self, delta):
        self.time_passed += delta
        if self.time_passed >= self.delay:
            self.time_passed = self.delay
            self.complete = True


class LappingTimer:
    def __init__(self, lap_time):
        self.lap_time = lap_time
        self.time_passed = 0
        self.laps_complete = 0

    def Update(self, delta):
        self.time_passed += delta
        while self.time_passed >= self.lap_time:
            self.time_passed -= self.lap_time
            self.laps_complete += 1
