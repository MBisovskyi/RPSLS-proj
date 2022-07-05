from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        print(f'1.{self.gestures[0]} 2.{self.gestures[1]} 3.{self.gestures[2]} 4.{self.gestures[3]} 5.{self.gestures[4]}')
        user_input = int(input('Make a choice: '))
        if user_input > len(self.gestures):
            self.choose_gesture()
        gesture = self.gestures[user_input - 1]
        return gesture