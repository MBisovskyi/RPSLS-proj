from player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()

    def picked_gesture(self):
        gesture = random.choice(self.gestures)
        return gesture