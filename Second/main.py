import os

board = [1, 2, 3, 4, 5, 6 ,7, 8, 9]
game = 0
player = 1
mark = "X"

def drawBoard():
    txt = """
    Press the number key to place
    an alternating "X" or "O."

    -------------
    | {} | {} | {} |
    -------------
    | {} | {} | {} |
    -------------
    | {} | {} | {} |
    -------------
    """
    print(txt.format(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))


def update():
    global mark
    global player
    if player % 2 != 0:
        mark = 'X'
    else:
        mark = "O"
    choice = int(input("Please select a number: "))
    board[choice-1] = mark
    player += 1
    checkWin()

def checkWin():
    global game
    if board[0] == board[1] and board[1] == board[2] and isinstance(board[1], int) != True:
        game = 1
    elif board[3] == board[4] and board[4] == board[5] and isinstance(board[4], int) != True:
        game = 1
    elif board[6] == board[7] and board[7] == board[8] and isinstance(board[4], int) != True:
        game = 1
    elif board[0] == board[3] and board[3] == board[6] and isinstance(board[4], int) != True:
        game = 1
    elif board[1] == board[4] and board[4] == board[7] and isinstance(board[4], int) != True:
        game = 1
    elif board[2] == board[5] and board[5] == board[8] and isinstance(board[4], int) != True:
        game = 1
    elif board[0] == board[4] and board[4] == board[8] and isinstance(board[4], int) != True:
        game = 1
    elif board[2] == board[4] and board[4] == board[6] and isinstance(board[4], int) != True:
        game = 1
    else:
        game = 0
while(game == 0):
    os.system("cls")
    drawBoard()    
    update()
    if game == 1:
        player -= 1
        if player % 2 != 0:
            print("Player 1 Won")
        else:
            print("Player Two Won")

os.system("pause")