board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

def draw_board():  # функция, которая рисует игровую доску
    for row in board:
        print(row)

def is_valid_choice(row, col):  # функция проверяет, что место на доске пустое
    return board[row][col] == ' '

def make_move(player, row, col):  # функция, которая размещает крестик/нолик на доске. player — X или O.
    if is_valid_choice(row, col):
        board[row][col] = player
    else:
        raise Exception('Так нельзя')

def has_won(player):  # функция, которая проверяет, что игрок player выйграл.
    for i in range(3):  # строки
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    for i in range(3):  # столбцы
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if (board[0][0] == board[1][1] == board[2][2] == player or   # 1-9
            board[0][2] == board[1][1] == board[2][0] == player):   # 7-3
        return True
    return False

# цикл игры.
draw_board()  # рисуем начальное состояние доски.
player = 'X'  # X всегда начинает.
while True:   # пока нет победителя.
    print("Player {} turn".format(player))   # показываем, чья очередь.
    row = int(input("Row: "))   # спрашиваем, куда поставить X или O.
    col = int(input("Col: "))
    make_move(player, row, col)   # ставим X или O.
    draw_board()   # рисуем обновленное состояние доски.
    if has_won(player):   # проверяем.
        print("Player {} won!".format(player))   #  показываем, кто выиграл.
        break   # прерываем основной цикл.
    player = 'O' if player == 'X' else 'X'   # меняем игроков.