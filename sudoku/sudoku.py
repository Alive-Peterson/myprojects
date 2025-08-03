def find_next_empty(puzzle):
    #finds next row, col on the puzzle that's not filled yet
    for r in range(9):
        for c in range(9): #returns 0,1,2...8
            if puzzle[r][c] == -1:
                return r,c
    return None,None # if no spaces are in puzzle empty(-1)

def is_valid(puzzle,guess,row,col):
    #returns true if guess is valid
    #for row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    #for col

    #col_vals=[]
    #for i in range(9):
    #    col_vals.append(puzzle[i] [col])

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    #then comes the 3x3 square, we want to know the starting position
    row_start = (row // 3)*3 # 1//3=0, 5//3=1,....
    col_start = (col // 3)*3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False
    #if we get here, taht means we passed the checks
    return True

def solve_sudoku(puzzle):
    #using BackTracking 

    #step1: choose somewhere on the puzzle to make a guess
    row,col = find_next_empty(puzzle)

    #if there's nowhere left then we're done cuz we allowed only valid inputs
    if row is None:
        return True
    
    #step 2:if there is a place to make a guess, choose from 1 to 9
    for guess in range(1,10):#range 1,2,3...9
        #step3: checks if the guess is valid
        if is_valid(puzzle,guess,row,col):

            #if its valid place that guess on the puzzle
            puzzle[row][col] = guess

            #step4: recursively call our function
            if solve_sudoku(puzzle):
                return True
            
        #step5: if the guess is not valid or guess does not match to the puzzle 
        # we need to backtrack and try a new number
        puzzle[row][col] = -1

    #step6: if none of the guess works, then the puzzle is unsolavable
    return False


if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)