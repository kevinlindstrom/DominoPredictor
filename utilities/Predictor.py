from utilities.Dominoes import dominos
from utilities.functions import functions

# Call imported classes
dm = dominos()
func = functions()

# define dominoes
deck = dm.Domino_List
# domino_board = []
domino_board = ['0-0', '0-1']

# initial hand
hand = ['0-2', '1-2', '2-2', '2-3', '2-4', '2-5', '2-6']
# hand = []
# for i in range(0, 7):
#     hand.append(func.add_domino())
print(hand)

if 'FAIL' in hand:
    print('Please enter your hand properly.')
    exit()

print('Beginning Game...')
turn_count = 0
while(1 == 1):
    print('The current board is:')
    print(domino_board)
    turn = func.turn(hand, domino_board)
    if type(turn[0]) == list:
        domino_board = turn[0]
        hand = turn[1]
        turn_count += 1
        print('Move completed... ')
    elif domino_board == 'end_game':
        print('GAME OVER')
        print('There were %i turns in the game.' % turn_count)
        break
    else:
        print('Move not completed... ')




