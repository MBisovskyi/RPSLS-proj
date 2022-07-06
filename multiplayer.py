from human import Human

class Multiplayer:
    def __init__(self):
        self.player_1 = Human()
        self.player_2 = Human()
        self.player_1_name = None 
        self.player_2_name = None 
        self.player_1_gesture = None
        self.player_2_gesture = None
        self.player_1_score_counter = 0
        self.player_2_score_counter = 0
        self.round_counter = 0

    def run_multi_player(self):
         while self.player_1_score_counter != 2 and self.player_2_score_counter != 2:
            self.players_picked_gestures()
            print(self.player_1_gesture)
            self.compare_gestures()
            print(f'{self.player_1_name} has {self.player_1_score_counter} and {self.player_2_name} has {self.player_2_score_counter}')
            self.round_counter += 1
            self.score_comparison()

    def acquire_player_names(self):
        self.player_1_name = input(f"What is Player 1's name? ")
        self.player_2_name = input(f"What is Player 2's name? ")

    def players_picked_gestures(self):
        self.player_1_gesture = self.player_1.picked_gesture()
        self.player_2_gesture = self.player_2.picked_gesture()

    def compare_gestures(self):
            if self.player_1_gesture == self.player_2_gesture:
                self.tie_result()
            elif self.player_1_gesture == 'Rock':
                self.rock_wins()
            elif self.player_1_gesture == 'Paper':
                self.paper_wins()
            elif self.player_1_gesture == 'Scissors':
                self.scissors_wins()
            elif self.player_1_gesture == 'Lizard':
                self.lizard_wins()
            elif self.player_1_gesture == 'Spock':
                self.spock_wins()    

    def tie_result(self):
        if self.player_1_gesture == self.player_2_gesture:
            print(f'No one wins. {self.player_1_name} picked {self.player_1_gesture} and {self.player_2_name} picked {self.player_2_gesture}!')

    def rock_wins(self):
        if self.player_2_gesture == 'Lizard' or self.player_2_gesture == 'Scissors':
            print(f'{self.player_1_name} wins!')
            print(f'Rock crushes {self.player_2_gesture}')
            player_wins = True 
        elif self.player_2_gesture == 'Paper':
            print(f'{self.player_2_name} wins. {self.player_2_gesture} covers rock!')
            player_wins = False 
        elif self.player_2_gesture == 'Spock':
            print(f'{self.player_2_name} wins. {self.player_2_gesture} vaporizes rock!')
            player_wins = False 
        self.round_winner(player_wins)
            
    def paper_wins(self):
        if self.player_2_gesture == 'Rock':
            print(f'{self.player_1_name} wins!')
            print(f'Paper covers Rock!')
            player_wins = True
        elif self.player_2_gesture == 'Spock':
            print(f'{self.player_1_name} wins!')
            print(f'Paper disproves Spock!')
            player_wins = True
        elif self.player_2_gesture == 'Scissors':
            print(f'{self.player_2_name} wins. {self.player_2_gesture} cuts paper!')
            player_wins = False
        elif self.player_2_gesture == 'Lizard':
            print(f'{self.player_2_name} wins. {self.player_2_gesture} eats paper!')
            player_wins = False
        self.round_winner(player_wins)

    def scissors_wins(self):
        if self.player_2_gesture == 'Paper':
            print(f'{self.player_1_name} wins!')
            print(f'Scissors cuts paper!')
            player_wins = True
        elif self.player_2_gesture == 'Lizard':
            print(f'{self.player_1_name} wins!')
            print(f'Scissors decapitates Lizard!')
            player_wins = True
        elif self.player_2_gesture == 'Rock':
            print(f'{self.player_2_name} wins. {self.player_2_gesture} crushes scissors!')
            player_wins = False
        elif self.player_2_gesture == 'Spock':
            print(f'{self.player_2_name} wins. {self.player_2_gesture} smashes scissors!')
            player_wins = False
        self.round_winner(player_wins)

    def lizard_wins(self):
        if self.player_2_gesture == 'Spock':
            print(f'{self.player_1_name} wins!')
            print(f'Lizard poisons spock!')
            player_wins = True
        elif self.player_2_gesture == 'Paper':
            print(f'{self.player_1_name} wins!')
            print(f'Lizard eats paper')
            player_wins = True
        elif self.player_2_gesture == 'Rock':
            print(f'{self.player_2_name} wins. {self.player_2_gesture} crushes lizard!')
            player_wins = False
        elif self.player_2_gesture == 'Scissors':
            print(f'{self.player_2_name} wins. {self.player_2_gesture} decapitates lizard!')
            player_wins = False
        self.round_winner(player_wins)

    def spock_wins(self):
        if self.player_2_gesture == 'Scissors':
            print(f'{self.player_1_name} wins!')
            print(f'Spock smashes scissors!')
            player_wins = True
        if self.player_2_gesture == 'Rock':
            print(f'{self.player_1_name} wins!')
            print(f'Spock vaporizes rock!')
            player_wins = True
        elif self.player_2_gesture == 'Lizard':
            print(f'{self.player_2_name} wins. {self.player_2_gesture} poisons spock!')
            player_wins = False
        elif self.ai_gesture == 'Paper':
            print(f'{self.player_2_name} wins. {self.player_2_gesture} disproves spock!')
            player_wins = False
        self.round_winner(player_wins)

    def round_winner(self, player_wins):
        if player_wins == True:
            self.player_1_score_counter += 1
        else:
            self.player_2_score_counter += 1

    def score_comparison(self):
        if self.player_1_score_counter == 2:
            print(f'{self.player_1_name} won this game!')
        elif self.player_2_score_counter == 2:
            print(f'{self.player_2_name} won this game')
    
    
               