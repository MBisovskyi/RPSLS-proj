import imp
from human import Human

class Multiplayer:
    def __init__(self):
        self.player_1 = Human()
        self.player_2 = Human()
        self.human_1_gesture = None
        self.human_2_gesture = None
        self.human_1_score_counter = 0
        self.human_2_score_counter = 0
        self.round_counter = 0

    def run_multiplayer(self):
        pass