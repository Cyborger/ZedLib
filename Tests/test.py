import ZedLib

class SnakeGame(ZedLib.Game):
    def __init__(self):
        self.playing_state = ZedLib.GameState(self)
        self.timer = ZedLib.Timer(200)
        self.lapping_timer = ZedLib.LappingTimer(200)
        self.test_surface = ZedLib.Surface("test_image.png", scale=2)

game = SnakeGame()
