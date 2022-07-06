from ai import Ai
from human import Human
from single_player import SinglePlayer
from multiplayer import Multiplayer

class Game:
    def __init__(self):
        self.single_player = SinglePlayer()
        self.multi_player = Multiplayer()
        self.ai = Ai()
        self.human = Human()
        self.rerun_game = None

    def run_game(self):
        self.greeting()
        self.game_rules()
        self.game_mode()
        self.is_rerun_game()
    
    # def run_multiplayer(self):
    #      while self.player_1_counter != 2 and self.player_2_counter != 2:
    #         self.players_picked_gestures()
    #         print(self.player_1_gesture)
    #         self.compare_gestures()
    #         print(self.player_1_counter, self.player_2_counter)
    #         self.round_counter += 1
    #         self.score_comparison()
    #      self.is_rerun_game()
    #      if self.rerun_game == True:
    #         self.rerun_game = False
    #         self.player_1_counter = 0
    #         self.player_2_counter = 0
    #         self.run_game()
    

    def greeting(self):
        print('Welcome to RPSLS!')

    def game_rules(self):
        print(f'\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\n')

    def game_mode(self):
        print('1. Single game\n2. Multiplayer')
        user_input = input('Please, select a game mode: ')
        if user_input == '1':
            self.single_player.run_singleplayer()
        if user_input == '2':
            self.multi_player.acquire_player_names()
            self.multi_player.run_multi_player()

    def is_rerun_game(self):
        user_input = input('Would you like to play again? Y/N?" ').lower()
        if user_input == 'y' or user_input == 'yes':
            self.rerun_game = True
            self.single_player.human_score_counter = 0
            self.single_player.ai_score_counter = 0
            self.single_player.round_counter = 0
            self.multi_player.player_1_score_counter = 0
            self.multi_player.player_2_score_counter = 0
            self.multi_player.round_counter = 0
            self.run_game()

        else:
            self.rerun_game = False