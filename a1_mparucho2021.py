"""
    Author: Marco Parucho
    Date: 5/20/2023
    Description: This is Project 1: Tic-Tac-Toe. 
    In this tic tac toe app I have to implement the MINMAX algorithm...
"""
#Globals
board = [1,2,3,4,5,6,7,8,9]
currentPlayer = 'X'
# This function creates the game board using a list 
def drawBoard():
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[6],board[7],board[8])

# This function places the 'X' or 'O' in the board
def place():
    global currentPlayer #I forgot that we had to do this in Python, help from Stackoverflow, document link on report. 
    choice = input("Enter choice: ")
    choice = int(choice) 

    if 1 <= choice <= 9:
        if board[choice-1] != 'X' and board[choice-1] != 'O':
            board[choice-1] = currentPlayer
            #switching player from X to O
            if currentPlayer == 'X':
                currentPlayer = 'O'
            else:
                currentPlayer = 'X'    
        else:
            print("Error. Position is already filled.")
    else:
        print("Error. Pick a choice between 1 and 9!")

#this function will be in charge of checking if any player win
def checkWin():
    #horizontal
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        print("Player X wins the game!")
    if board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        print("Player X wins the game!")
    if board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        print("Player X wins the game!")
    #vertical
    #diagonal

#calling functions
while True:
    drawBoard()
    place()
    checkWin()

     

  