from ai import Ai
from human import Human

class Game:
    def __init__(self):
        self.ai = Ai()
        self.human = Human()

    def run_game(self):
        self.greeting()
        self.game_rules()

    def greeting(self):
        print('Welcome to RPSLS!')

    def game_rules(self):
        print(f'\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Pape\n')

    def game_mode(self):
        print('1. Single game\n2. Multiplayer')
        user_input = input('Please, select a game mode: ')
        if user_input == '1':
            pass
        
    def compare_gestures(self):
        pass

    def rock_wins(self):
        if self.human.picked_gesture() == 'Rock' and self.ai.picked_gesture() == 'Scissors' or self.ai.picked_gesture() == 'Lizard':
            print(f'Player wins because {self.human.picked_gesture()} crushes {self.ai.picked_gesture()}')