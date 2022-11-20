"""
Step 1: Identify an empty square

Step 2: Place a number

Step 3: Check if that number is repeated

Step 4: Proceed if the number is not repeated

Step 5: Check next square

"""
def display_board(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            print(board[row][col], end=" ")
        print()


def check(board, row, col, number):
    for i in range(len(board)):
        if board[row][i] == number:
            return False
        if board[i][col] == number:
            return False
        if board[3 * int(row / 3) + int(i / 3)][3 * int(col / 3) + int(i%3)] == number:
            return False
    return True
    

def place_number(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                for number in range(1,10):
                    if check(board, row, col, number):
                        board[row][col] = number
                        if place_number(board):
                            return True
                        else:
                            board[row][col] = 0
                return False
    return True                        
                    
if __name__=='__main__':
    board_1 = [
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 3],
        [0, 7, 4, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 2],
        [0, 8, 0, 0, 4, 0, 0, 1, 0],
        [6, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 7, 8, 0],
        [5, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0]
    ]

board = board_1

print("Initial Board: ")
display_board(board)
place_number(board)
print("Solved Board: ")
display_board(board)