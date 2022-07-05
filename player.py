class Player:
    def __init__(self):
        self.name = ''
        self.gestures = ['Paper', 'Rock', 'Scissors', 'Lizard', 'Spock']

    def choose_gesture(self):
       pass

    def chose_gesture(self):
        print(self.choose_gesture)

player = Player()
player.chose_gesture()