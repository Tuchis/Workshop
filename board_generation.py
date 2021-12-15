import string

def board_generate():
    lst = []
    timed_lst = []
    let_list = []
    for i in range(1, 11):
        let_list.append(string.ascii_uppercase[i - 1])
        i = str(i)
        # if len(i) < 2:
        #     i = '0' + i
        # timed_lst.append(i)
        for j in range(1, 11):
            timed_lst.append('_')
        lst.append(timed_lst)
        timed_lst = []
    lst.insert(0, let_list)
    for index, line in enumerate(lst):
        line_str = ''
        for item in line:
            line_str +=item + ' '
        if index<10:
            print('0' + str(index)+ '  ' + line_str)
        else:
            print(str(index) + '  ' + line_str)
    return lst

print(board_generate())

first_board = board_generate()
user_board = board_generate()


def vyvid (lst_board):
    for index, line in enumerate(lst_board):
        line_str = ''
        for item in line:
            line_str +=item + ' '
        if index<10:
            print('0' + str(index)+ '  ' + line_str)
        else:
            print(str(index) + '  ' + line_str)
    return lst_board

vyvid(board_generate())

