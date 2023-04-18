board = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

board[1][1] = "X"


def display_board(board):
    #     # The function accepts one parameter containing the board's current status
    #     # and prints it out to the console.

    print("+" + (("-" * 7) + "+") * 3)
    print("|" + ((" " * 7) + "|") * 3)
    print("|" + " " * 3 + board[0][0] + " " * 3 + "|"
          + " " * 3 + board[0][1] + " " * 3 + "|"
          + " " * 3 + board[0][2] + " " * 3 + "|")
    print("|" + ((" " * 7) + "|") * 3)
    print("+" + (("-" * 7) + "+") * 3)
    print("|" + ((" " * 7) + "|") * 3)
    print("|" + " " * 3 + board[1][0] + " " * 3 + "|"
          + " " * 3 + board[1][1] + " " * 3 + "|"
          + " " * 3 + board[1][2] + " " * 3 + "|")
    print("|" + ((" " * 7) + "|") * 3)
    print("+" + (("-" * 7) + "+") * 3)
    print("|" + ((" " * 7) + "|") * 3)
    print("|" + " " * 3 + board[2][0] + " " * 3 + "|"
          + " " * 3 + board[2][1] + " " * 3 + "|"
          + " " * 3 + board[2][2] + " " * 3 + "|")
    print("|" + ((" " * 7) + "|") * 3)
    print("+" + (("-" * 7) + "+") * 3)


def enter_move(board):
    #     # The function accepts the board's current status, asks the user about their move,
    #     # checks the input, and updates the board according to the user's decision.

    lib_move = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2]
    }

    while True:
        inputStep = int(input("Enter your move: "))
        if inputStep >= 1 and inputStep <= 9:
            UsrStp = lib_move[inputStep]
            if tuple(UsrStp) in make_list_of_free_fields(board):
                board[UsrStp[0]][UsrStp[1]] = "O"
                return board

            else:
                print("this field is already taken")
        else:
            print("wrong step")


def make_list_of_free_fields(board):
    #     # The function browses the board and builds a list of all the free squares;
    #     # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []

    for i in range(3):
        if board[0][i] != "O" and board[0][i] != "X":
            free_fields.append((0, i))
        if board[1][i] != "O" and board[1][i] != "X":
            free_fields.append((1, i))
        if board[2][i] != "O" and board[2][i] != "X":
            free_fields.append((2, i))

    return free_fields


def victory_for(board, sign):
    #     # The function analyzes the board's status in order to check if
    #     # the player using 'O's or 'X's has won the game
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == sign:
            return True
    for j in range(3):
        if board[j][0] == board[j][1] == board[j][2] == sign:
            return True

    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True


def draw_move(board):
    #     # The function draws the computer's move and updates the board.
    lib_move = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2]
    }

    from random import randrange

    while True:
        rand = randrange(9) + 1
        raStp = lib_move[rand]
        if tuple(raStp) in make_list_of_free_fields(board):
            board[raStp[0]][raStp[1]] = "X"
            return board


flag = 0
display_board(board)

while flag < 4:
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("You won!")
        break
    draw_move(board)
    if victory_for(board, 'X'):
        display_board(board)
        print("You lose!")
        break
    display_board(board)
    flag += 1

if flag == 4:
    print("Draw!")
    enter_move(board)
