import math
import random

class Player:
    def __init__(self,letter):
        # letter can be x or o
        self.letter=letter

    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square=random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square=False
        val=None
        while not valid_square:
            square=input(self.letter + '\'s turn. Input move (0-8):')
            # we are going to check that it's a correct value by trying to cast it as an integer
            # and if it's not its invalid and if that spot is not available on the board we also say it's invalid
            try:
                val=int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square=True #if these are successfull, then good
            except ValueError:
                print('Invalid square, Try again')
            
        return val