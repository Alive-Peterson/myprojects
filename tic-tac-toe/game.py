import time
from player import HumanPlayer,RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board=[' ' for _ in range (9)] # using a single list, to represent 3x3 matrix shape
        self.current_winner=None # to keep track of the winner

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
            if self.winner(square,letter):
                self.current_winner=letter
            return True
        return False
    
    def winner(self,square,letter):
        # check the possibilities of 3 in a row or column, to find winner
        #start by checking row
        row_ind=square//3
        row=self.board[row_ind*3:(row_ind+1)*3]
        if all([spot==letter for spot in row]):
            return True
        
        #check column
        col_ind=square%3
        column=[self.board[col_ind+i*3] for i in range(3)]
        if all([spot==letter for spot in column]):
            return True
        
        #check diagonals
        #but only the even square positions like(0,2,4,6,8)
        #these are only possible moves to win in a diagonal
        if square%2==0:
            diagonal1=[self.board [i] for i in [0,4,8]]
            if all([spot==letter for spot in diagonal1]):
                return True
            diagonal2=[self.board [i] for i in [2,4,6]]
            if all([spot==letter for spot in diagonal2]):
                return True
        #if all else fails 
        return False

def play(game,o_player,x_player,print_game=True):
    if print_game:
        game.print_board_nums()

    letter='x' #starting letter
    #iterate while the game still has empty squares
    while game.empty_squares():
        #gets move from appropriate player
        if letter=='o':
            square=o_player.get_move(game)
        else:
            square=x_player.get_move(game)

        # a function to make move
        if game.make_move(square,letter):
            if print_game:
                print(letter + f' make a move to square {square}')
                game.print_board()
                print(' ') #empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            
            #after we made our move, we need to alternate letters
            letter='o' if letter=='x' else 'x'  #switches the player 
            #if letter=='x':
            #    letter='o'
            #else:
            #    letter='x'
            #small break

        #small gap break
        time.sleep(0.8) 


    if print_game:
            print("It's a tie")
    
    


if __name__ == '__main__':
    x_player=HumanPlayer('x')
    o_player=RandomComputerPlayer('o')
    t=TicTacToe()
    play(t,o_player,x_player,print_game=True)