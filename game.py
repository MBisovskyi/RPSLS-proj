from ai import Ai
from human import Human

class Game:
    def __init__(self):
        self.ai = Ai()
        self.human = Human()
        self.human_gesture = None
        self.ai_gesture = None
        self.human_score_counter = 0
        self.ai_score_counter = 0

    def run_game(self):
        self.greeting()
        self.game_rules()
        round = 0
        while self.human_score_counter != 2 and self.ai_score_counter != 2:
            self.players_picked_gestures()
            print(self.ai_gesture)
            self.compare_gestures()
            print(self.ai_score_counter, self.human_score_counter)
            round += 1
            self.score_comparison()

    def greeting(self):
        print('Welcome to RPSLS!')

    def game_rules(self):
        print(f'\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\n')

    def game_mode(self):
        print('1. Single game\n2. Multiplayer')
        user_input = input('Please, select a game mode: ')
        if user_input == '1':
            pass
        
    def players_picked_gestures(self):
        self.human_gesture = self.human.picked_gesture()
        self.ai_gesture = self.ai.picked_gesture()

    def compare_gestures(self):
        if self.human_gesture == self.ai_gesture:
            self.tie_result()
        elif self.human_gesture == 'Rock':
            self.rock_wins()
        elif self.human_gesture == 'Paper':
            self.paper_wins()
        elif self.human_gesture == 'Scissors':
            self.scissors_wins()
        elif self.human_gesture == 'Lizard':
            self.lizard_wins()
        elif self.human_gesture == 'Spock':
            self.spock_wins()
    
    def tie_result(self):
        if self.human_gesture == self.ai_gesture:
            print(f'No one wins. Player picked {self.human_gesture} and Ai picked {self.ai_gesture}!')

    def rock_wins(self):
        if self.ai_gesture == 'Lizard' or self.ai_gesture == 'Scissors':
            print(f'Player wins!')
            print(f'Rock crushes {self.ai_gesture}')
            self.human_score_counter += 1
        elif self.ai_gesture == 'Paper':
            print(f'Ai wins. {self.ai_gesture} covers rock!')
            self.ai_score_counter += 1
        elif self.ai_gesture == 'Spock':
            print(f'Ai wins. {self.ai_gesture} vaporizes rock!')
            self.ai_score_counter += 1
            
    def paper_wins(self):
        if self.ai_gesture == 'Rock':
            print(f'Player wins!')
            print(f'Paper covers Rock!')
            self.human_score_counter += 1
        elif self.ai_gesture == 'Spock':
            print(f'Player wins!')
            print(f'Paper disproves Spock!')
            self.human_score_counter += 1
        elif self.ai_gesture == 'Scissors':
            print(f'Ai wins. {self.ai_gesture} cuts paper!')
            self.ai_score_counter += 1
        elif self.ai_gesture == 'Lizard':
            print(f'Ai wins. {self.ai_gesture} eats paper!')
            self.ai_score_counter += 1

    def scissors_wins(self):
        if self.ai_gesture == 'Paper':
            print(f'Player wins!')
            print(f'Scissors cuts paper!')
            self.human_score_counter += 1
        elif self.ai_gesture == 'Lizard':
            print(f'Player wins!')
            print(f'Scissors decapitates Lizard!')
            self.human_score_counter += 1
        elif self.ai_gesture == 'Rock':
            print(f'Ai wins. {self.ai_gesture} crushes scissors!')
            self.ai_score_counter += 1
        elif self.ai_gesture == 'Spock':
            print(f'Ai wins. {self.ai_gesture} smashes scissors!')
            self.ai_score_counter += 1
        
    def lizard_wins(self):
        if self.ai_gesture == 'Spock':
            print(f'Player wins!')
            print(f'Lizard poisons spock!')
            self.human_score_counter += 1
        elif self.ai_gesture == 'Paper':
            print(f'Player wins!')
            print(f'Lizard eats paper')
            self.human_score_counter += 1
        elif self.ai_gesture == 'Rock':
            print(f'Ai wins. {self.ai_gesture} crushes lizard!')
            self.ai_score_counter += 1
        elif self.ai_gesture == 'Scissors':
            print(f'Ai wins. {self.ai_gesture} decapitates lizard!')
            self.ai_score_counter += 1

    def spock_wins(self):
        if self.ai_gesture == 'Scissors':
            print(f'Player wins!')
            print(f'Spock smashes scissors!')
            self.human_score_counter += 1
        if self.ai_gesture == 'Rock':
            print(f'Player wins!')
            print(f'Spock vaporizes rock!')
            self.human_score_counter += 1
        elif self.ai_gesture == 'Lizard':
            print(f'Ai wins. {self.ai_gesture} poisons spock!')
            self.ai_score_counter += 1
        elif self.ai_gesture == 'Paper':
            print(f'Ai wins. {self.ai_gesture} disproves spock!')
            self.ai_score_counter += 1

    def score_comparison(self):
        if self.human_score_counter == 2:
            print('Player won this game!')
        elif self.ai_score_counter == 2:
            print('Ai won this game')      

