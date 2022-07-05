from ai import Ai

class Game:
    def __init__(self):
        pass

    def run_game(self):
        self.greeting()

    def greeting(self):
        print('Welcome to RPSLS!')

    def game_rules(self):
        print(f'\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Pape\n')

    def game_mode(self):
        print('1. Single game\n2. Multiplayer')
        user_input = input('Please, select a game mode: ')
        if user_input == '1':
            single_player = Ai()
        
        
