from pprint import pprint
#The pprint module provides a capability to “pretty-print” arbitrary Python data structures

#looking for an empty place in the grid, return the index 
def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    return None, None

#check if the guess is valid 
def is_valid(puzzle, guess, row, col):
    if guess in puzzle[row]: #the value(guess ) must be unique in a row 
        return False
    if guess in [puzzle[i][col] for i in range(9)]: # it must be unique in the col too
        return False
    # checking the small 3X3 square 
    row_start = (row // 3) * 3  # ex: row = 1 => 1//3 = 0 => 0 *3 = 0 so the row starts from 0 and ends in 0+ 3 = 3 (cuz we have 3X3 square )
    col_start = (col //3) * 3   # same thing goes for columns 

    for r in range (row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True  # if we arrive here, it means the guess is true and it's unique in a row, col and the 3X3 square 

 #main function 
def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle) 
    if row is None: # if we have no empty space 
        return True
    for guess in range(1, 10): #trying numbers form 1 to 9 
        if is_valid(puzzle, guess, row, col): #if it's a valid guess , we assign that value 
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        # if we arrive here, it means that nothing true and we need to backtrack and try a new number

        puzzle[row][col] = -1    
        
        #else it is UNSOLVABLE or the initial grid was wrong
    return False

puzzle = [
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

print(solve_sudoku(puzzle))
pprint(puzzle)