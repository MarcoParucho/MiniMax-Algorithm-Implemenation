"""
    Author: Marco Parucho
    Date: 5/20/2023
    Description: This is Project 1: Tic-Tac-Toe. 
    In this tic tac toe app I have to implement the MINMAX algorithm...
"""
import os #importing library to be able to clear board 
# Globals
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
currentPlayer = 'X'

# This function creates the game board using a list
def drawBoard():
    os.system("cls")  # Clear the screen
    print("\t  TIC TAC TOE\n")
    print("\t", board[0], " | ", board[1], " | ", board[2])
    print("\t---------------")
    print("\t", board[3], " | ", board[4], " | ", board[5])
    print("\t---------------")
    print("\t", board[6], " | ", board[7], " | ", board[8])

# This function places the 'X' or 'O' in the board. Giving it parameters player and position
def place(player, position):
    global currentPlayer

    board[position-1] = player
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'

# This function checks if any player wins. Passing board as a parameter
def checkWin(board):
    combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]              # diagonal
    ]

    for i in combinations:
        if all(board[pos] == 'X' for pos in i):
            return 'X'
        if all(board[pos] == 'O' for pos in i):
            return 'O'
    return None

# This function checks if the game is tied
def checkDraw(board):
    return all(isinstance(pos, str) for pos in board)

# Implementing minmax algorithm
def minmax(board, depth, maxPlayer):
    if checkWin(board) == 'X':
        return -1
    elif checkWin(board) == 'O':
        return 1
    elif checkDraw(board):
        return 0

    if maxPlayer:
        scoreUp = float('-inf')
        for i in range(9):
            if isinstance(board[i], int):
                board[i] = 'O'
                eval = minmax(board, depth+1, False)
                board[i] = i+1
                if eval is not None:
                    scoreUp = max(scoreUp, eval)
        if scoreUp == float('-inf'):
            return 0
        return scoreUp
    else:
        scoreDown = float('inf')
        for i in range(9):
            if isinstance(board[i], int):
                board[i] = 'X'
                eval = minmax(board, depth+1, True)
                board[i] = i+1
                if eval is not None:
                    scoreDown = min(scoreDown, eval)
        if scoreDown == float('inf'):
            return 0
        return scoreDown

# This function determines the computer moves
def bot():
    score = float('-inf')
    move = None

    for i in range(9):
        if isinstance(board[i], int):
            board[i] = 'O'
            x = minmax(board, 0, False)
            board[i] = i+1
            if x > score:
                score = x
                move = i+1
    place('O', move)

# Main game loop
while True:
    drawBoard()
    # The game will only ask for input when the player is 'X'
    if currentPlayer == 'X':
        choice = input("\n\tEnter choice: ")
        if choice.isdigit():
            choice = int(choice)
            if choice < 1 or choice > 9:
                print("Error. Pick a digit between 1 and 9")
                continue
            if board[choice-1] != choice:
                print("Error. Position is filled.")
                continue
            place('X', choice)
        else:
            print("ERROR... numeric value must be entered")
    else:
        bot()

    if checkWin(board):
        drawBoard()
        os.system("cls")
        print("The computer has won the game!")
        break
    elif checkDraw(board):
        drawBoard()
        os.system("cls")
        print("TIE!")
        break

     

  