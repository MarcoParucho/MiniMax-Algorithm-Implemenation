"""
    Author: Marco Parucho
    Date: 5/20/2023
    Description: This is Project 1: Tic-Tac-Toe. 
    In this tic tac toe app I have to implement the MINMAX algorithm...
"""
board = [1,2,3,4,5,6,7,8,9]
# This function creates the game board using a list 
def drawBoard():
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[6],board[7],board[8])

# This function places the 'X' or 'O' in the board
def place():
    choice = input("Enter choice: ")
    choice = int(choice) 

    if 1 <= choice <= 9:
        if board[choice-1] != 'X' and board[choice-1] != 'O':
            board[choice-1] = 'X'
        else:
            print("Error. Position is already filled.")
    else:
        print("Error. Pick a choice between 1 and 9!")


while True:
    drawBoard()
    place()
