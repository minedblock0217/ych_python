import random as r
import os
import platform

#function to clear the screen
def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

#choose mark for User
def select_mark():
    user_mark = input("choose your mark>>>(x,o)").lower()
    if user_mark == 'x':
        return 'x','o'
    elif user_mark == 'o':
        return 'o','x'
    else:
        return select_mark()

# make random order (1 = com,0 = user)
def random_turn():
    turn = r.randrange(0,2)
    if turn == 1:
        return 1
    elif turn == 0:
        return 0

#make game board
def make_board():
    board = []
    for i in range(9):
        board.append("*")
    return board

#check who is win
def check_win(board, mark):
    if board[0] == mark and board[1] == mark and board[2] == mark:
        return True
    elif board[0] == mark and board[4] == mark and board[8] == mark:
        return True
    elif board[0] == mark and board[3] == mark and board[6] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[2] == mark and board[4] == mark and board[6] == mark:
        return True
    elif board[3] == mark and board[4] == mark and board[5] == mark:
        return True
    elif board[6] == mark and board[7] == mark and board[8] == mark:
        return True
    else:
        return False

def print_board(board):
    for i in range(0,8,3):
        print(board[i],board[i + 1],board[i + 2])
    print("=====")

def put_mark():
    temp = None
    while temp == None:
        try:
            temp = int(input("Enter the number(0 ~ 8) : "))
            if board[temp] == "o" or board[temp] == "x":
                temp = None
                print("Error: there is mark choose another one")
        except Exception as e:
            print("Error:", e)
            temp = None
    return temp

def again():
    again = input("again? (y/n) : ").lower()
    if again == 'y':
        again_flag = 1
        return again_flag
    else:
        again_flag = 0
        return again_flag

#start code zone
again_flag = 1
while again_flag != 0:
    clear()
    user_mark, com_mark = select_mark()
    turn = random_turn()
    board = make_board()

    while True:
        clear()
        print_board(board)
        check_User = check_win(board, user_mark)
        check_com = check_win(board, com_mark)

        if turn == 0:
            temp = put_mark()
            board[temp] = user_mark
            turn = 1

        elif turn == 1:
            com_put = r.randrange(0, 9)
            while board[com_put] != "*":
                com_put = r.randrange(0,9)
            board[com_put] = com_mark
            turn = 0

        if check_User == True:
            print("player win!")
            again_flag = again()
            break

        elif check_com == True:
            print("computer win!")
            again_flag = again()
            break

        if board[0] != "*" and  board[1] != "*" and board[2] != "*" and board[3] != "*" and board[4] != "*" and board[5] != "*" and board[6] != "*" and board[7] != "*" and board[8] != "*":
            print("draw")
            again_flag = again()
            break