player1 = ''
player2 = ''
board = ['#']

def initalize_board():
    global board
    for i in range(1, 10):
        board.append([i, str(i)])

def print_board():
    print('\n' * 10)
    global board
    print(
        ' {} | {} | {} '.format(check_blank_value(board[7]), check_blank_value(board[8]), check_blank_value(board[9])))
    print('-----------')
    print(
        ' {} | {} | {} '.format(check_blank_value(board[4]), check_blank_value(board[5]), check_blank_value(board[6])))
    print('-----------')
    print(
        ' {} | {} | {} '.format(check_blank_value(board[1]), check_blank_value(board[2]), check_blank_value(board[3])))

def check_blank_value(input):
    value = input[1]
    if value.isalpha():
        return input[1]
    else:
        return input[0]

def take_user_choice():
    global player1, player2
    while True:
        choice = input('Enter player 1 choice : \n')
        if choice in ('x', 'o', 'X', 'O'):
            player1 = choice.upper()
            if player1 == 'X':
                player2 = 'O'
            else:
                player2 = 'X'
            break
        else:
            print('Invalid input, choice must be among (x,o)')
    print(player1 + ":" + player2)

def take_user_input(player):
    print(f'player : {player} is playing')
    global board
    while True:
        index = int(input('please enter the index to place you value : \n'))
        if 0 < index < 10:
            if is_index_vacant(index):
                board[index] = [index, player]
                break
            else:
                print('specified index is not vacant, please enter valid one')
                continue
        else:
            print('Only number are allowed between(1-9)')

def is_index_vacant(index):
    global board
    return board[index][1].isdigit()

def flip_user(active_player):
    global player1, player2
    if active_player == player1:
        return player2
    else:
        return player1

def player_has_won(active_player):
    global board
    return (board[7][1] == active_player and board[8][1] == active_player and board[9][1] == active_player) \
           or (board[4][1] == active_player and board[5][1] == active_player and board[6][1] == active_player) \
           or (board[1][1] == active_player and board[2][1] == active_player and board[3][1] == active_player) \
           or (board[7][1] == active_player and board[4][1] == active_player and board[1][1] == active_player) \
           or (board[8][1] == active_player and board[5][1] == active_player and board[2][1] == active_player) \
           or (board[9][1] == active_player and board[6][1] == active_player and board[3][1] == active_player) \
           or (board[7][1] == active_player and board[5][1] == active_player and board[3][1] == active_player) \
           or (board[9][1] == active_player and board[5][1] == active_player and board[1][1] == active_player)

def can_play():
    global board
    for x in range(1, 10):
        value = board[x][1]
        if value.isdigit():
            return True
    return False

def play_game(active_player):
    global player1, player2
    while can_play():
        print_board()
        take_user_input(active_player)
        print_board()
        if player_has_won(active_player):
            print(f'{active_player} has won the game')
            break
        active_player = flip_user(active_player)
    if not (can_play() or player_has_won(active_player)):
        print('Its a tie')
    print('Game over')


initalize_board()
print_board()
take_user_choice()
play_game(player1)
