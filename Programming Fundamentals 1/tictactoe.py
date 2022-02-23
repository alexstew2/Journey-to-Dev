# Project: Tic-tac-toe

# Write a command-line program where two people can play tic-tac-toe against one another.

# 1) Should display the board
# 2) Should take player input for what box they play in each turn
# 3) Should handle games ending in wins/losses
# 4) Should handle games ending in a tie

# first_player = input('Who moves first? ')

# if first_player.upper() == 'X':
#     print('X moves first!')
#     second_player = 'O'
# elif first_player.upper() == 'O':
#     print('O moves first!')
#     second_player = 'X'
# else:
#     print('Unknown player')
    

board = [[[],[],[]],[1,2,3],[1,2,3]]

# Prints the current board state
def make_board():
    i = 0
    for row in board:
        print(board[i])
        i += 1


# make_board()

# move_row = int(input('Select row: ')) - 1
# move_column = int(input('Select column: ')) - 1

# if board[move_row][move_column] == 'X' or board[move_row][move_column] == 'O':
#     print('This space is occupied, select another')
# else:
#     board[move_row][move_column] = first_player.upper()

make_board()

