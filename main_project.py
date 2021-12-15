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

def main():
    Place_horizontaly=True
    Ships=[4,3,3,2,2,2,2,1,1,1,1]
    Ships_position=[]
    while True:
        Field=Get_field(Ships_position)
        ship=Ships[0]
        print("Your ship:")
        print('*'*ship)
        print("Placing mode:")
        if Place_horizontaly:
            print("Horizontal")
        else:
            print("Vertical")
        Player_comand=input()
        if Player_comand=='0':
            print("Mode changed")
            Place_horizontaly=not Place_horizontaly
            continue
        try:
            Player_comand=Player_comand.split(' ')
            x_cor=int(Player_comand[0])
            y_cor=int(Player_comand[1])
        except:
            print('Wrong input')
            continue
        New_ship_coordinate=[]
        for i in range(ship):
            if Place_horizontaly:
                if (y_cor>10)|((x_cor+ship)>10)|((x_cor, y_cor+i) in Ships_position):
                    print("You can not place ship here")
                    New_ship_coordinate=[]
                    break
                New_ship_coordinate.append((x_cor, y_cor))
  
def Get_field(List_of_ships_coordinate):
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
    for coordinate in List_of_ships_coordinate:
        lst[coordinate[1]][coordinate[0]]='*'
    for line in lst:
        print(*line)
    return lst
main()
