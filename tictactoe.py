first_to_move = input('Who moves first? ')
if first_to_move == 'X' or first_to_move == 'x':
    print('X moves first!')
elif first_to_move == 'O' or first_to_move == 'o':
    print('O moves first!')
else:
    print('Unknown player')

i=0
while i<3:
    print('|' '|' )
    i+=1