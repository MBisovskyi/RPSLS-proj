from player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        random.choice(self.gestures)
        print(random.choice(self.gestures))

    def chose_gesture(self):
        print(self.chose_gesture)

        self.chose_gesture()
    
