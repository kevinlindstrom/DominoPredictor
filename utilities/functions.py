class functions:
    def add_domino(self):
        # Takes user input and converts it to standard form
        numbers = str(input('Input two numbers on the domino: \n'))
        if len(numbers) != 2:
            return 'FAIL'
        one = numbers[0]
        two = numbers[1]
        if one > two:
            first_number = two
            second_number = one
        else:
            first_number = one
            second_number = two
        if int(first_number) > 6 or int(second_number) > 6:
            return 'FAIL'
        print('The entered domino was: %s-%s' % (first_number, second_number))
        return '%s-%s' % (first_number, second_number)


    # Move type 1
    def add_domino_to_board(self, domino, domino_board, hand):
        # Ensures domino being played has not already been played
        if domino not in domino_board and domino[::-1] not in domino_board:
            append_to_number = input('Number connected to: \n')
            if append_to_number in domino:
                domino_reverse = domino[::-1]

                # Add domino to beginning of the board
                if str(domino_board[0])[0] == append_to_number:
                    print('Connected to beginning of board : ' + str(domino_board[0])[0])
                    if domino[0] == append_to_number:
                        domino_board = [domino_reverse] + domino_board
                    if domino[:] == append_to_number:
                        domino_board = [domino] + domino_board

                # Add domino to the end of the board
                elif str(domino_board[:])[:] == append_to_number:
                    print('Connected to end of board: ' + str(domino_board[:])[:])
                    if domino[0] == append_to_number:
                        domino_board = domino_board.append(domino)
                    if domino[:] == append_to_number:
                        domino_board = domino_board.append(domino_reverse)

                else:
                    print('You cannot play this domino... try again...')
                    return 'FAIL'
            else:
                print('Cannot connect numbers that do not match')
                return 'FAIL'
        else:
            print('You cannot play a domino already existing on the board')
            return 'FAIL'

        return [domino_board, hand]


    # Move type 2
    def add_domino_from_hand_to_board(self, hand, domino_board):
        print('Yor hand is:\n' + str(hand))
        domino = self.add_domino()
        for domino_number, hand_domino in enumerate(hand):
            if hand_domino == domino:
                del(hand[domino_number])
                return self.add_domino_to_board(domino, domino_board, hand)
        else:
            print('Domino not found in hand...')
            return 'FAIL'

    # Move type 3
    def draw_domino_to_hand(self, hand, domino_board):
        domino = self.add_domino()
        hand = hand.append(domino)
        add_to_board = input('Can you add this domino to the board? (y/n):\n')
        if add_to_board == 'y':
            self.add_domino_from_hand_to_board(hand, domino_board)
        elif add_to_board == 'n':
            print('Better luck next time.')
        else:
            print('Entry not recognized repeat move')
        return [domino_board, hand]

    # Function to perform turns
    def turn(self, hand, domino_board):
        move_type = str(input('Input move type (? for help):\n'))
        if move_type == '?':
            print('1 for add domino to board not from hand \n'
                  '2 for adding domino to board from hand \n'
                  '3 for drawing \n4 for passing\n5 for ending the game')

        elif move_type == '1':
            print('Move type: %s' % move_type)
            return self.add_domino_to_board(self.add_domino(), domino_board, hand)

        elif move_type == '2':
            print('Move type: %s' % move_type)
            return self.add_domino_from_hand_to_board(hand, domino_board)

        elif move_type == '3':
            print('Move type: %s' % move_type)
            return self.draw_domino_to_hand(hand, domino_board)
        elif move_type == '4':
            print('Move type: %s' % move_type)

        elif move_type == '5':
            if input('Has the game ended? (y/n)\n') == 'y':
                return 'end_game', 'end_game'

        else:
            print('Move not recognized...')

