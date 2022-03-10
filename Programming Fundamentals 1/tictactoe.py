# Project: Tic-tac-toe

# Write a command-line program where two people can play tic-tac-toe against one another.

# Should display the board
# Should take player input for what box they play in each turn
# Should handle games ending in wins/losses
# Should handle games ending in a tie

def print_board():
    """Displays the current board state"""
    for l, c, r in board:
        print(l, c, r)

def game_on():
    """Determines if the game has been won, tied, or is still in progress"""
# Rows
    for l, c, r in board:
        if l == c == r and l == 'X':
            return False
        elif l == c == r and l == 'O':
            return False
# Columns
    t_board = zip(*board)
    for l, c, r in t_board:
        if l == c == r and l == 'X':
            return False
        elif l == c == r and l == 'O':
            return False

# Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] == 'X':
        return False
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] == 'O':
        return False
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] == 'X':
        return False
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] == 'O':
        return False
# Tie
    if all('_' not in row for row in board):
        return False
    return True

def move(current_player):
    """Prompts user for a move, checks for validity, then executes the move"""
    space = input('Where would you like to play? ')
    if space not in moves:
        print('Unknown Move')
        return False

    coord = moves[space]
    if board[coord[0]][coord[1]] != '_':
        print('This space is already occupied.')
        return False

    board[coord[0]][coord[1]] = current_player
    return True

# TODO switch X or O
def switch_player(player):
    """Alternates player"""
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player

if __name__ == '__main__':
    need_answer = True
    while need_answer:
        first_player = input('Who moves first? ')
        upper_input = first_player.upper()
        if upper_input == 'X' or upper_input == 'O':
            print(f'{upper_input} moves first!')
            current_player = upper_input
            need_answer = False
        else:
            print('Unknown player, please select X or O')

    board = [['_','_','_'],['_','_','_'],['_','_','_']]

    moves = {
        'top-l': [0,0],
        'top-c': [0,1],
        'top-r': [0,2],
        'cen-l': [1,0],
        'center': [1,1],
        'cen-r': [1,2],
        'bot-l': [2,0],
        'bot-c': [2,1],
        'bot-r': [2,2],
    }

    print('List of moves: ')
    for key in moves.keys():
        print(key)

    while game_on():
        print_board()
        if move(current_player):
            current_player = switch_player(current_player)
        print(f'Current player is {current_player}')

    current_player = switch_player(current_player)
    print_board()

    if all('_' not in row for row in board):
        current_player = 'Tie'
    if current_player == 'X':
        print("X's Win!")
    elif current_player == 'O':
        print("O's Win!")
    else:
        print("Tie!")