import random


def print_board(board):
    for row in board:
        print('|'.join(row))


def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Do you want to be X or O? ").upper()
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, position):
    row = (position - 1) // 3
    col = (position - 1) % 3
    board[row][col] = marker


def win_check(board, mark):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False


def choose_first():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def space_check(board, position):
    row = (position - 1) // 3
    col = (position - 1) % 3
    return board[row][col] == ' '


def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("Choose your next position: (1-9) "))
    return position


def computer_choice(board, computer_marker):
    for i in range(1, 10):
        if space_check(board, i):
            place_marker(board, computer_marker, i)
            if win_check(board, computer_marker):
                place_marker(board, ' ', i)
                return i
            place_marker(board, ' ', i)
    for i in range(1, 10):
        if space_check(board, i):
            place_marker(board, computer_marker, i)
            if win_check(board, computer_marker):
                place_marker(board, ' ', i)
                return i
            place_marker(board, ' ', i)
    corners = [1, 3, 7, 9]
    possible_corners = []
    for corner in corners:
        if space_check(board, corner):
            possible_corners.append(corner)
    if possible_corners:
        return random.choice(possible_corners)
    if space_check(board, 5):
        return 5
    sides = [2, 4, 6, 8]
    possible_sides = []
    for side in sides:
        if space_check(board, side):
            possible_sides.append(side)
    if possible_sides:
        return random.choice(possible_sides)


def full_board_check(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def play_game():
    board = [
        [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']
    ]
    player_marker, computer_marker = player_input()
    turn = choose_first()
    print(turn)
    while True:
        if turn == 'player':
            print_board(board)
            position = player_choice(board)
            place_marker(board, player_marker, position)
            if win_check(board, player_marker):
                print_board(board)
                print("Congratulations! You have won the game!")
                break
            elif full_board_check(board):
                print_board(board)
                print("The game is a draw.")
                break
            else:
                turn = 'computer'
        else:
            print("The computer is making its move...")
            position = computer_choice(board, computer_marker)
            place_marker(board, computer_marker, position)
            if win_check(board, computer_marker):
                print_board(board)
                print("Sorry, the computer has won the game.")
                break
            elif full_board_check(board):
                print_board(board)
                print("The game is a draw.")
                break
            else:
                turn = 'player'


play_game()
