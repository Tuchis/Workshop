def shoot_func(board_for_program:list):
    board_for_player = board_generate()
    boolean = True
    while boolean:
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        enumerate_let = list(enumerate(letters))
        row, column = input("Введіть координати пострілу [1-10][A-J](наприклад: 5 B): ").split()
        for item in enumerate_let:
            if column in item:
                coordinate = item[0]
                break
        if board_for_program[int(row)][coordinate] == "_":
            board_for_program[int(row)][coordinate] = board_for_program[int(row)][coordinate].replace("_", "0")
            board_for_player[int(row)][coordinate] = board_for_program[int(row)][coordinate].replace("_", "0")
            boolean = False
        elif board_for_program[int(row)][coordinate] == "*":
            board_for_program[int(row)][coordinate] = board_for_program[int(row)][coordinate].replace("*", "X")
            board_for_player[int(row)][coordinate] = board_for_program[int(row)][coordinate].replace("*", "x")
        else:
            boolean = False
    return board_for_player
