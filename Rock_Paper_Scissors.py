"""
Step 1 : Take Input

Step 2 : Generate random move
 Part A : Defining the possible moves
 Part B : Let the computer choose the move

Step 3 : Print the winner
 Part A : Defining the logic
 Part B : Declaring the results

"""
import random

""" STEP : 1 : Taking inputs from operator """

your_move = input("Enter your move (R/P/S) : ")

""" STEP : 2 : Generating Random moves """

""" PART A : Defining the possible moves """

possible_moves = ["R", "P", "S"]

""" PART B : Let the computer choose the move """

computer_move = possible_moves[random.randint(0,2)]

""" STEP : 3 """

""" PART A : Defining the logic """

result = None

if your_move == "R" and computer_move == "P":
    result = "Computer"
elif your_move == "R" and computer_move == "S":
    result = "You"
elif your_move == "P" and computer_move == "R":
    result = "You"
elif your_move == "P" and computer_move == "S":
    result = "Computer"
elif your_move == "S" and computer_move == "R":
    result = "Computer"
elif your_move == "S" and computer_move == "P":
    result = "You"

""" PART B : Declaring the results """

if result:
    print(f"{result} Wins!")
else:
    print ("Tie!")










