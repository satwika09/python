import random
board=['-','-','-',
        '-','-','-',
        '-','-','-']
pp= 'X'
win= None
gameon= True
#printing the game board
def printBoard(board):
    print(' '+board[0] +' | ' + board[1] +' | '+board[2])
    print('-----------')
    print(' '+board[3] +' | ' + board[4] +' | '+board[5])
    print('-----------')
    print(' '+board[6] +' | ' + board[7] +' | '+board[8])
#taking input
def pinput(board):
    while True:
        ip = int(input("Enter a number from 1 to 9 :"))
        if ip>=1 and ip<=9 and board[ip-1] =='-':
            board[ip-1]=pp
            break
        else:
            print("player is already in the spot!")
        printBoard(board)

#check win or tie
def chkHorizontal(board):
    global win
    if board[0] == board[1] == board[2] and board[1]!='-':
        win=board[1]
        return True
    elif board[3] == board[4] == board[5] and board[3]!='-':
        win = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[7]!='-':
        win=board[6]
        return True
def chkRow(board):
    global win
    if board[0] == board[3] == board[6] and board[6]!='-':
        win=board[3]
        return True
    elif board[1] == board[4] == board[8] and board[1]!='-':
        win=board[1]
        return True
    elif board[2] == board[5] == board[8] and board[5]!='-':
        win=board[5]
        return True

def chkdiagonal(board):
    global win
    if board[0] == board[4] == board[8] and board[8]!='-':
        win=board[8]
        return True
    elif board[2] == board[4] == board[6] and board[4]!='-':
        win=board[4]
        return True
def chkTie(board):
    global gameon
    if '-' not in board :
        printBoard(board)
        print("It is a tie!")
        gameon=False


def chkWin():
    if chkdiagonal(board) or chkHorizontal(board) or chkRow(board):
        print(f"The winner is {win}")

def anotherPlayer():
    global pp
    if pp =='X':
        pp='O'
    else:
        pp='X'


def computer(board):
    while pp =='O':
        position = random.randint(0,8)
        if board[position] == '-':
            board[position] = 'O'
            anotherPlayer()
while gameon:
    printBoard(board)
    if win != None :
        break
    pinput(board)
    chkWin()
    chkTie(board)
    anotherPlayer()
    computer(board)
    chkWin()
    chkTie(board)