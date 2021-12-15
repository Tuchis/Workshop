import string


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
        for j in range(1, 11):
            timed_lst.append('_')
        lst.append(timed_lst)
        timed_lst = []
    lst.insert(0, let_list)
    return lst

def print_field(field):
    for line in field:
        print(*line)
print_field(generate_field())

def place_figures(player, field):
    moves = 0
    while moves < 4:
        pass




