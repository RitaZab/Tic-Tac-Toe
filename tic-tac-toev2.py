import random
#Global variables
player=""
play_again=True
game_version=""
who_start:""
game_on=True
winner=None
board=["-", "-", "-",
       "-", "-", "-",
       "-", "-", "-",]
valid=False
player1=""
player2=""
AI=""
#Functions

def player_turn1():
    global non_ava_places
    global game_on
    player=player1
    print(f"It's {player} turn")
    choice = input("Choose a free position number:    ")
    valid = False
    while not valid:
        while choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Invalid input. Type  again number of free spot")
            choice = input("Choose a free position number:    ")
        choice = int(choice) - 1
        if board[choice] == "-":
            valid = True
        else:
            print("Invalid input. Type  again number of free spot")
            choice = input("Choose a free position number:    ")
    board[choice] = player1
    show_board()
    check_if_win()
    check_if_tie()

def player_turn2():
    global non_ava_places
    global game_on
    player = player2
    print(f"It's {player} turn")
    choice = input("Choose a free position number:    ")
    valid = False
    while not valid:
        while choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Invalid input. Type  again number of free spot")
            choice = input("Choose a free position number:    ")
        choice = int(choice) - 1
        if board[choice] == "-":
            valid = True
        else:
            print("Invalid input. Type  again number of free spot")
            choice = input("Choose a free position number:    ")
    board[choice] = player2
    show_board()
    check_if_win()
    check_if_tie()

def show_board():
    print(board[0]+' | '+board[1]+' | '+board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def AI_turn():
    global non_ava_places
    global valid
    global player
    global game_on
    global board
    player=AI
    print(f"It's {player} turn")
    choice=random.randint(1,9)
    choice = int(choice) - 1
    valid=False
    print(choice)
    while board[choice] == "-":
        valid = True
        break
    else:
        choice = random.randint(1, 9)
        choice = int(choice) - 1
    board[choice] = AI
    show_board()
    check_if_win()
    check_if_tie()


def check_rows():
    global game_on
    row1= board[0]==board[1]==board[2] !="-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        game_on=False
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]
    return

def check_col():
    global game_on
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    if column1 or column2 or column3:
        game_on=False
    if column1:
        return board[0]
    if column2:
        return board[1]
    if column3:
        return board[2]
    return

def check_diag():
    global game_on
    diagonal1=board[0] == board[4] == board[8] != "-"
    diagonal2=board[2] == board[4] == board[6] != "-"
    if diagonal1 or diagonal2:
        game_on=False
        return board[5]
    return

def check_if_win():
    global winner
    global game_on
    row_win=check_rows()
    col_win=check_col()
    diag_win=check_diag()
    if row_win:
        winner=row_win
        print(f"{winner} win!")
        game_on=False
    elif col_win:
        winner=col_win
        print(f"{winner} win!")
        game_on=False
    elif diag_win:
        winner=diag_win
        print(f"{winner} win!")
        game_on=False
    else:
        winner=None
    return
def check_if_tie():
    global game_on
    if "-" not in board:
        game_on=False
    else:
        game_on=True
def playing_again():
    global play_again
    global board
    global winner
    global game_on
    last = input("Do yu want to play again? Type Y or N  ").lower()
    if last == "y":
        board = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-", ]
        play_again=True
    else:
        play_again = False
        game_on=False
        print("Goodbye")



while play_again:
    winner=None
    while game_on:
        game_version = input("Is there 1 or 2 players?Type number:   ")
        if game_version == '1':
            player1 = input("Player 1,choose your symbol:  ")
            AI = input("Choose AI symbol:  ")
            who_start=input("Who starts?Type me or AI")
            while who_start != "me" or who_start != "AI":
                print("You need to type me or AI")
                who_start = input("Who starts?Type me or AI")
            else:
                if who_start=="me":
                    while winner is None:
                        player_turn1()
                        if winner is not None:
                            playing_again()
                            break
                        AI_turn()
                        if winner is not None:
                            playing_again()
                elif who_start=="ai":
                    while winner is None:
                        AI_turn()
                        player_turn1()
                    else:
                        game_on = False
                        break

        elif game_version == '2':
            player1 = input("Plyer 1,choose your symbol:  ")
            player2 = input("Player 2, choose your symbol:  ")
            while winner is None:
                player_turn1()
                if winner is not None:
                    playing_again()
                    break
                player_turn2()
                if winner is not None:
                    playing_again()
                    break

    else:
        playing_again()
        if play_again:
            game_on = True
        else:
            break



