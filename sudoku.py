import random


#Backtracking Algorithim
def backtrack_alg(gb: list) -> True:
    """Implement recursive backtracking algorithim."""
    empty_space = _is_empty(gb)
    if not empty_space:
        return True
    else:
        row, col = empty_space
    for i in range(1,10):
        if _is_valid(gb,i,(row, col)):
            gb[row][col] = i
        
            if backtrack_alg(gb):
                return True
            
            gb[row][col] = 0 #Backtrack; reset last element
        
    return False #ALL SOLUTIONS NOT POSSIBLE, SENDS TO BACKTRACK
        



def print_game_board(gb: list) -> None:
    """Print the game board."""
    for i in range(len(gb)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ") #Every 3 rows, print straight horiz. line
         
        for j in range(len(gb[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "") #Check for position, if first number add vert. line
                 
            if j == 8:
                print(gb[i][j])
            else:
                print(str(gb[i][j]) + " ", end = "")


def _is_empty(gb: list) -> tuple:
    """Find empty space."""
    for i in range(len(gb)): #Scan for row
        for j in range(len(gb[0])): #Scan for column
            if gb[i][j] == 0: #if value is 0, return tuple with row and column coordinates
                return (i,j)
    return None

def _is_valid(gb: list, num: int, pos: tuple) -> bool:
    """Check if position is valid."""
    #Check the row
    for i in range(len(gb[0])):
        if gb[pos[0]][i] == num and pos[1] != i:
            return False
        
    #Check the column
    for i in range(len(gb)):
        if gb[i][pos[1]] == num and pos[0] != i:
            return False   
    #Check box
    box_x_coord = pos[1] // 3
    box_y_coord = pos[0] // 3
    for i in range(box_y_coord * 3, box_y_coord * 3 + 3):
        for j in range(box_x_coord * 3, box_x_coord * 3 + 3):
            if gb[i][j] == num and (i,j) != pos:
                return False
    return True

if __name__ == "__main__":
    game_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
    ]
    print('EMPTY')
    print_game_board(game_board)
    backtrack_alg(game_board)
    print()
    print('SOLVED')
    print_game_board(game_board)
