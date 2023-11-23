
board = [
  [5, 3, 0, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def print_board(grid):
    """
    Prints board in sudoku format
    """
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')
            
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
                
            if j == 8:
                    print (grid[i][j])
            else:
                    print(str(grid[i][j]) + " ", end="")

def find_empty(grid):
    """
    Checks for empty space
    """
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 0:
                return(i,j)
    
    return None

def valid(grid, num, pos):
    """
    Checks rows and columns for duplicates
    """
    #loop through row
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False
    
    #loop through column
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False
        
    #checking 3x3 boxes
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False
    return True

def solve(grid):
    """
    if there are empty spaces replace with num 1-10. Solve function calls itself(such recursion, such wow), if true and valid returns solved, else backtracks
    """
    find = find_empty(grid)
    
    #if there are no empty spaces game is solved
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1, 10):
        if valid(grid, i, (row, col)):
            grid[row][col] = i
            
            if solve(grid):
                return True
            
            #reset value if unsolvable
            grid[row][col] = 0
            
    return False

print_board(board)
solve(board)
print('_________________')
print_board(board)