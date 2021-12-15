import string
import sys

def generate_field():
    r"""
    The function to generate the play field
    >>> generate_field() #doctest +EPSILLON
    '[['  ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']...'
    """
    lst = []
    timed_lst = []
    let_list = ['  ']
    for i in range(1, 11):
        let_list.append(string.ascii_uppercase[i - 1])
        i = str(i)
        if len(i) < 2:
            i = '0' + i
        timed_lst.append(i)
        for j in range(1, 11):
            timed_lst.append('_')
        lst.append(timed_lst)
        timed_lst = []
    lst.insert(0, let_list)
    return lst


def print_field(field):
    """
    Printing of the field
    """
    for line in field:
        print(*line)


def place_figures(player, field):
    """
    The finction to place figures
    """
    print("You're player", player)
    figures = ['****', '***', '**', '*']
    moves = 0
    while moves < 4:
        print("Here's what your field looks like:")
        print_field(field)
        figure = figures[moves]
        print("You're now placing the figure:", figure)
        print("Choose the location to place the figure, for example: 'A 1'.")
        move = input().upper().split()
        print(move)
        if len(move) == 2:
            if move[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
                if int(move[1]) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                    cutter = string.ascii_uppercase.index(move[0]) + 1
                    if cutter + len(figure) < len(field[1]):
                        # cutter = field[string.ascii_uppercase.index(move[0]) + 1]
                        field[int(move[1])] = field[int(move[1])][0:cutter] + [i for i in figure] + field[int(move[1])][cutter + len(figure):]
                        moves += 1
    print("Your final field look like this:")
    print_field(field)
    return field


def shooting(field, cord):
    """
    The function that "shoots".
    """
    letters = ' ABCDEFGHIJ'
    boat_in = True
    while boat_in:
        if field[cord[1]][letters.find(cord[0])] == '*':
            boat_in = True
            print('Bingo!')
            field[cord[1]][letters.find(cord[0])] = 'X'
            #need to input new cord here
            try:
                letter_input = input('Print coordinates letter')
                number_input = int(input('Print coordinates number'))
            except:
                break
            cord = (letter_input, number_input)
        elif field[cord[1]][letters.find(cord[0])] == '_':
            boat_in = False
            field[cord[1]][letters.find(cord[0])] = 'O'
            print('No boat here')
        elif field[cord[1]][letters.find(cord[0])] == 'X' or field[cord[1]][letters.find(cord[0])] == 'O':
            print("You've already used this coordinates")
            letter_input = input('Print coordinates letter')
            number_input = int(input('Print coordinates number'))
            cord = (letter_input, number_input)
            continue
    return field


def win_checker(field):
    """ return true if field isn't dead yet """
    flag = False
    for lst in field:
        for ele in lst:
            if ele == '*':
                flag = True
    return flag

print()
def cord_asker():
    """
    The function that asks for coordinates for input
    """
    print('You have to make a move. If you want to leave the game, enter exit')
    column = 0
    row = 'a'
    alph = 'ABCDEFGIJ'
    row_exe = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    while alph.find(str(column)) == -1 and column != 'exit':
        column = input('Input the letter')
    while row not in row_exe and row != 'exit':
        row = input('Input the row')
    if row == 'exit' or column == 'exit':
        print('byee')
        sys.exit()
    return column, int(row)


def main():
    print("First, name yourselves!")
    player1_name = input('Player 1, enter your nickname\n>>>')
    player2_name = input('Player 1, enter your nickname\n>>>')
    player1_field = generate_field()
    player2_field = player1_field.copy()
    print("Time to fill the fields!")
    print(player1_name, 'turn!')
    field_for_output_player1 = player2_field.copy()
    field_for_output_player2 = player1_field.copy()
    player1_field = place_figures(1, player1_field)
    for _ in range(100):
        print()
    print(player2_name, 'turn!')
    player2_field = place_figures(2, player2_field)
    for _ in range(100):
        print()
    print("It's time to attack!")
    while True:
        player1_attack = cord_asker()
        print(player2_name, ", it's your turn to attack!")
        timed_lst_pl1 = []
        field_for_output_player2 = []
        for i in range(1, len(player1_field)):
            field_for_output_player2.append([])
            for elem in range(1, len(player1_field[i])):
                if player1_field[i][elem] == "*":
                    field_for_output_player2[i-1].append("_")
                else:
                    field_for_output_player2[i-1].append(player2_field[i][elem])
        timed_lst_pl2 = []
        field_for_output_player1 = []
        for i in range(1, len(player2_field)):
            field_for_output_player1.append([])
            for elem in range(1, len(player2_field[i])):
                if player2_field[i][elem] == "*":
                    field_for_output_player1[i-1].append("_")
                else:
                    field_for_output_player1[i-1].append(player2_field[i][elem])
        # for i in player2_field:
        #     field_for_output_player1.append(i.replace('*', '_'))
        player2_field = shooting(player2_field, player1_attack)
        print(player1_name,  "it's your turn to attack!")
        print('Your opponents field looks like this:')
        print_field(field_for_output_player1)
        player2_attack = cord_asker()
        player1_field = shooting(player1_field, player2_attack)
        print(player2_name,  "it's your turn to attack!")
        print('Your opponents field looks like this:')
        print_field(field_for_output_player2)
        if not win_checker(player1_field):
            print(player2_name, 'won!')
            sys.exit()
        elif not win_checker(player2_field):
            print(player1_name, 'won!')
            sys.exit()


main()

