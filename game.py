from single_player import SinglePlayer
from multiplayer import Multiplayer

class Game:
    def __init__(self):
        self.single_player = SinglePlayer()
        self.multiplayer = Multiplayer()
        self.rerun_game = None

    def run_game(self):
        self.greeting()
        self.game_rules()
        self.game_mode()
        self.is_rerun_game()
    
    def greeting(self):
        print('Welcome to RPSLS!')

    def game_rules(self):
        print(f'\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\n')

    def game_mode(self):
        print('1. Single game\n2. Multiplayer')
        user_input = input('Please, select a game mode: ')
        if user_input == '1':
            self.single_player.acquire_player_name()
            self.single_player.run_singleplayer()
        if user_input == '2':
            self.multiplayer.aquire_players_names()
            self.multiplayer.run_multiplayer()

    def is_rerun_game(self):
        user_input = input('Would you like to play again? Y/N?" ').lower()
        if user_input == 'y' or user_input == 'yes':
            self.rerun_game = True
            self.single_player.player1_score_counter = 0
            self.single_player.player2_score_counter = 0
            self.single_player.round_counter = 0
            self.multiplayer.round_counter = 0
            self.multiplayer.player1_score_counter = 0
            self.multiplayer.player2_score_counter = 0
            self.run_game()
        else:
            self.rerun_game = False