import random as r

#choose mark for User
def select_mark():
    user_mark = str(input("choose your mark>>>(x,o)")).lower()
    if user_mark == 'x':
        return 'x','o'
    elif user_mark == 'o':
        return 'o','x'
    else:
        while not (user_mark == 'x' or uesr_mark == 'o'):
            uesr_mark = str(input("choose your mark>>>(x,o)"))



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
    temp = int(input("Enter the number(0 ~ 8) : "))
    while board[temp] == "o" or board[temp] == "x":
        print("there is mark choose another one")
        temp = int(input("Enter the number(0 ~ 8) : "))
    return temp

def again():
    again = input("again?").lower()
    if again == 'y':
        again_flag = 1
        return again_flag
#start code zone
again_flag = 1
while again_flag != 0:
    user_mark,com_mark = select_mark()
    turn = random_turn()
    board = make_board()

    while(True):
        print_board(board)
        check_User = check_win(board, user_mark)
        check_com = check_win(board, com_mark)
        if(turn == 0):
            temp = put_mark()
            board[temp] = user_mark
            turn = 1
        elif(turn == 1):
            com_put = r.randrange(0, 9)
            while board[com_put] != "*":
                com_put = r.randrange(0,9)
            board[com_put] = com_mark
            turn = 0

        if check_User == True:
            print("player wind!")
            again_flag = again()
        elif check_com == True:
            print("computer win!")
            again_flag = again()

        if board[0] != "*" and  board[1] != "*" and board[2] != "*" and board[3] != "*" and board[4] != "*" and board[5] != "*" and board[6] != "*" and board[7] != "*" and board[8] != "*":
            print("draw")
            again_flag = again()


