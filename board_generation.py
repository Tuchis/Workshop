import string
import sys

def generate_field():
    lst = []
    timed_lst = []
    let_list = ['  ']
    for i in range(1, 11):
        let_list.append(string.ascii_uppercase[i - 1])
        i = str(i)
        if len(i) < 2:
            i = '0' + i
        timed_lst.append(i)
        for _ in range(1, 11):
            timed_lst.append('_')
        lst.append(timed_lst)
        timed_lst = []
    lst.insert(0, let_list)
    return lst

def win_checker(field):
    """ return true if field isn't dead yet """
    flag = False
    for lst in field:
        for ele in lst:
            if ele == '*':
                flag = True
    return flag

def cord_asker():
    print('You have to make a move. If you want to leave the game, enter exit')
    column = 0
    row = 'a'
    alph = 'ABCDEFGIJ'
    row_exe = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
    while alph.find(column) == -1 and column != 'exit':
        column = input('Input the letter')
    while row not in row_exe and row != 'exit':
        row = input('Input the row')
    if row == 'exit' or column == 'exit':
        print('byee')
        sys.exit()
    return column, row


def print_field(field):
    for line in field:
        print(*line)
print_field(generate_field())

def shooting(field, cord):
    letters = ' ABCDEFGHIJ'
    while boat_in:
        if field[cord[2]][letters.find(cord[1])] == '*':
            boat_in = True
            print('Bingo!')
            field[cord[2]][letters.find(cord[1])] = 'X'
            #need to input new cord here
            letter_input = input('Print coordinates letter')
            number_input = int(input('Print coordinates number'))
            cord = (letter_input, number_input)
        elif field[cord[2]][letters.find(cord[1])] == '_':
            boat_in = False
            print('No boat here')
        else:
            print("You've already used this coordinates")
            continue
    return field

def place_figures(player, field):
    moves = 0
    while moves < 4:
        pass
