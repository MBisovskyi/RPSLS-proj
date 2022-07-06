from human import Human
from ai import Ai

class SinglePlayer:
    def __init__(self):
        self.player1 = Human()
        self.player2 = Ai()
        self.player1_name = None
        self.player2_name = 'Ai'
        self.player1_gesture = None
        self.player2_gesture = None
        self.player1_score_counter = 0
        self.player2_score_counter = 0
        self.round_counter = 0

    def run_singleplayer(self):
         while self.player1_score_counter != 2 and self.player2_score_counter != 2:
            self.players_picked_gestures()
            print(f'\n{self.player1_name} picks {self.player1_gesture}.\n{self.player2_name} picks {self.player2_gesture}.\n')
            self.compare_gestures()
            print(f'\n          WINS\n{self.player1_name} has {self.player1_score_counter} and {self.player2_name} has {self.player2_score_counter}')
            self.round_counter += 1
            self.score_comparison()

    def acquire_player_name(self):
        self.player1_name = input('Enter your name: ')

    def players_picked_gestures(self):
        self.player1_gesture = self.player1.picked_gesture(self.player1_name)
        self.player2_gesture = self.player2.picked_gesture()

    def compare_gestures(self):
            if self.player1_gesture == self.player2_gesture:
                self.tie_result()
            elif self.player1_gesture == 'Rock':
                self.rock_wins()
            elif self.player1_gesture == 'Paper':
                self.paper_wins()
            elif self.player1_gesture == 'Scissors':
                self.scissors_wins()
            elif self.player1_gesture == 'Lizard':
                self.lizard_wins()
            elif self.player1_gesture == 'Spock':
                self.spock_wins()    

    def tie_result(self):
        if self.player1_gesture == self.player2_gesture:
            print(f'No one wins. {self.player1_name} picked {self.player1_gesture} and {self.player2_name} picked {self.player2_gesture}!')

    def rock_wins(self):
        if self.player2_gesture == 'Lizard' or self.player2_gesture == 'Scissors':
            print(f'{self.player1_name} wins!')
            print(f'Rock crushes {self.player2_gesture}')
            player1_wins = True 
        elif self.player2_gesture == 'Paper':
            print(f'{self.player2_name} wins. {self.player2_gesture} covers rock!')
            player1_wins = False 
        elif self.player2_gesture == 'Spock':
            print(f'{self.player2_name} wins. {self.player2_gesture} vaporizes rock!')
            player1_wins = False 
        self.round_winner(player1_wins)
            
    def paper_wins(self):
        if self. player2_gesture == 'Rock':
            print(f'{self.player1_name} wins!')
            print(f'Paper covers Rock!')
            player1_wins = True
        elif self.player2_gesture == 'Spock':
            print(f'{self.player1_name} wins!')
            print(f'Paper disproves Spock!')
            player1_wins = True
        elif self.player2_gesture == 'Scissors':
            print(f'{self.player2_name} wins. {self.player2_gesture} cuts paper!')
            player1_wins = False
        elif self.player2_gesture == 'Lizard':
            print(f'{self.player2_name} wins. {self.player2_gesture} eats paper!')
            player1_wins = False
        self.round_winner(player1_wins)

    def scissors_wins(self):
        if self.player2_gesture == 'Paper':
            print(f'{self.player1_name} wins!')
            print(f'Scissors cuts paper!')
            player1_wins = True
        elif self.player2_gesture == 'Lizard':
            print(f'{self.player1_name} wins!')
            print(f'Scissors decapitates Lizard!')
            player1_wins = True
        elif self.player2_gesture == 'Rock':
            print(f'{self.player2_name} wins. {self.player2_gesture} crushes scissors!')
            player1_wins = False
        elif self.player2_gesture == 'Spock':
            print(f'{self.player2_name} wins. {self.player2_gesture} smashes scissors!')
            player1_wins = False
        self.round_winner(player1_wins)

    def lizard_wins(self):
        if self.player2_gesture == 'Spock':
            print(f'{self.player1_name} wins!')
            print(f'Lizard poisons spock!')
            player1_wins = True
        elif self.player2_gesture == 'Paper':
            print(f'{self.player1_name} wins!')
            print(f'Lizard eats paper')
            player1_wins = True
        elif self.player2_gesture == 'Rock':
            print(f'{self.player2_name} wins. {self.player2_gesture} crushes lizard!')
            player1_wins = False
        elif self.player2_gesture == 'Scissors':
            print(f'{self.player2_name} wins. {self.player2_gesture} decapitates lizard!')
            player1_wins = False
        self.round_winner(player1_wins)

    def spock_wins(self):
        if self.player2_gesture == 'Scissors':
            print(f'{self.player1_name} wins!')
            print(f'Spock smashes scissors!')
            player1_wins = True
        if self.player2_gesture == 'Rock':
            print(f'{self.player1_name} wins!')
            print(f'Spock vaporizes rock!')
            player1_wins = True
        elif self.player2_gesture == 'Lizard':
            print(f'{self.player2_name} wins. {self.player2_gesture} poisons spock!')
            player1_wins = False
        elif self.player2_gesture == 'Paper':
            print(f'{self.player2_name} wins. {self.player2_gesture} disproves spock!')
            player1_wins = False
        self.round_winner(player1_wins)

    def round_winner(self, player1_wins):
        if player1_wins == True:
            self.player1_score_counter += 1
        else:
            self.player2_score_counter += 1

    def score_comparison(self):
        if self.player1_score_counter == 2:
            print(f'{self.player1_name} won this game!')
        elif self.player2_score_counter == 2:
            print(f'{self.player2_name} won this game')
    



