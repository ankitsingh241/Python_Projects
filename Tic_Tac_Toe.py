"""
Step 1: Get move from player 1

Step 2: Get move from player 2

Step 3: Check for winner

Step 4: Run until winner is found or grid is full 




"""

board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

def display_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
            
            if j in [0, 1]:
                print("|", end=" ")
        print()
        if i in [0, 1]:
            print("----------")


def enter_move1():
    player1_move = int(input("Enter your move Player 1 : "))
    player1_move = player1_move-1
    i = int(player1_move / 3)
    j = int(player1_move % 3)
    board[i][j] = "X"
    display_board(board)


def enter_move2():
    player2_move = int(input("Enter your move Player 2 : "))
    player2_move = player2_move-1
    i = int(player2_move / 3)
    j = int(player2_move % 3)
    board[i][j] = "O"
    display_board(board)


def check():
    for row in board :
        if row[0] == row[1] == row[2] == "X":
            return 1
        elif row[0] == row[1] == row[2] == "O":
            return 2
    
    for col in range(3) :
        if board[0][col] == board[1][col] == board[2][col] == "X":
            return 1
        if board[0][col] == board[1][col] == board[2][col] == "O":
            return 2

    if board[0][0] == board[1][1] == board[2][2] == "X":
        return 1      
    elif board[0][0] == board[1][1] == board[2][2] == "O":
        return 2

    elif board[0][2] == board[1][1] == board[2][0] == "X":
        return 1        
    elif board[0][2] == board[1][1] == board[2][0] == "O":
        return 2     
            

if __name__ == '__main__':
    winner = 0
    total_moves = 9

    while total_moves > 0:
        enter_move1()
        total_moves -= 1
        winner = check()
        if winner or total_moves <= 0:
            break
        enter_move2()
        total_moves -= 1
        winner = check()
        if winner :
            break
    
    if winner == 1:
        print("Player 1 wins !")
    elif winner == 2:
        print("Player 2 wins !")
    else:
        print("It's a Tie !")         
