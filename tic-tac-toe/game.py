class TicTacToe:
    def __init__(self):
        self.board=[' ' for _ in range (9)] # using a single list, to represent 3x3 matrix shape
        self.winner=None # to keep track of the winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)] :
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 it tells us which box responds to which number
        number_board=[[str(i) for i in range((j*3),(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot==' ']
        #moves=[]
        #for (i,spot) in enumerate(self.board):
        #    if spot==' ':
        #        moves.append(i)
        #return moves

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self,square,letter):
        #if valid move then make the move, assign square to letter
        #then return True. if invalid return False
        if self.board[square]==" ":
            self.board[square]=letter
            return True
        return False
        

def print_game(game,o_player,x_player,print_game=True):
    if print_game:
        game.print_board_nums()

    letter='X' #starting letter
    #iterate while the game still has empty squares
    while game.empty_squares():
        #gets move from appropriate player
        if letter=='o':
            square=o_player.get_move(game)
        else:
            square=x_player.get_move(game)

        # a function to make move