# Project: Tic-tac-toe

# Write a command-line program where two people can play tic-tac-toe against one another.

# Should display the board
# Should take player input for what box they play in each turn
# Should handle games ending in wins/losses
# Should handle games ending in a tie

answer = False
while answer == False: 
    first_player = input('Who moves first? ')
    first_player = first_player.upper()

    if first_player == 'X':
        print('X moves first!')
        current_player = 0
        answer = True
    elif first_player == 'O':
        print('O moves first!')
        current_player = 1
        answer = True
    else:
        print('Unknown player, please select X or O')

board = [['_','_','_'],['_','_','_'],['_','_','_']]

def make_board():
    for l, c, r in board:
        print(l, c, r)

moves = {
    'top-left': [0,0],
    'top-center': [0,1],
    'top-right': [0,2],
    'cen-left': [1,0],
    'center': [1,1],
    'cen-right': [1,2],
    'bot-left': [2,0],
    'bot-center': [2,1],
    'bot-right': [2,2],
}

print('List of moves: ')
for key in moves.keys():
    print(key)

game_over = False
while game_over == False:
    make_board()
# TODO: Make move()
    move = input('Where would you like to play? ')
    if move in moves:
        coordinate = moves[move]
        if board[coordinate[0]][coordinate[1]] != '_':
            print('This space is already occupied')
            continue
        else:
            if current_player == 0:
                board[coordinate[0]][coordinate[1]] = 'X'
                current_player =+ 1
            elif current_player == 1:
                board[coordinate[0]][coordinate[1]] = 'O'
                current_player -= 1
    else:
        print('Unknown move')
        continue

# Check if game is won TODO: Make game_state()
# Rows Check
    for l, c, r in board:
        if l == c == r and l == 'X':
            game_over = True
        elif l == c == r and l == 'O':
            game_over = True
        else:
            continue
# Columns Check
#   Left Column
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] == 'X':
        game_over = True
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] == 'O':
        game_over = True
#   Center Column
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] == 'X':
        game_over = True
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] == 'O':
        game_over = True
#   Right Column
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] == 'X':
        game_over = True
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] == 'O':
        game_over = True
# Diagonals Check
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] == 'X':
        game_over = True
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] == 'O':
        game_over = True
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] == 'X':
        game_over = True
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] == 'O':
        game_over = True
# Check for tie
    if all('_' not in row for row in board):
        current_player = current_player + 100
        game_over = True
make_board()

if current_player == 1:
    print("X's Win!")
elif current_player == 0:
    print("O's Win!")
else:
    print("Tie!")