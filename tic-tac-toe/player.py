import math
import random

class Player:
    def __init__(self,letter):
        # letter can be x or o
        self.letter=letter

    def get_move(self,move):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, move):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, move):
        pass