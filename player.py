from operator import ge


class Player:
    def __init__(self):
        self.name = ''
        self.gesture = ['Paper', 'Rock', 'Scissors', 'Lizard', 'Spock']

    def gesture_choice(self):
        print(f'1.{self.gesture[0]} 2.{self.gesture[1]} 3.{self.gesture[2]} 4.{self.gesture[3]} 5.{self.gesture[4]}')
        user_input = int(input('Make a choice: '))
        if user_input == 1:
            gesture = self.gesture[0]
        elif user_input == 2:
            gesture = self.gesture[1]
        elif user_input == 3:
            gesture = self.gesture[2]
        elif user_input == 4:
            gesture = self.gesture[3]
        elif user_input == 5:
            gesture = self.gesture[4]
        elif user_input > len(self.gesture):
            self.gesture_choice()
        return gesture

player = Player()
gesture = player.gesture_choice()
print(gesture)