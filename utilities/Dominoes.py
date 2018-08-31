class dominos:
    # Creates the set of dominoes
    numbers = list(range(0, 7))
    Domino_List = []
    for first_number in numbers:
        for second_number in numbers:
            reverse = ('%i-%i' % (second_number, first_number))
            if reverse not in Domino_List:
                Domino_List.append('%i-%i' % (first_number, second_number))
    # print(Domino_List)
    # print(len(Domino_List))
