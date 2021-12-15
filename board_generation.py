import string

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
for line in lst:
    print(*line)
