# Создайте программу для игры в ""Крестики-нолики"".

board = list(map(str, range(1, 10)))

win_ids = [
    (0,1,2),
    (3,4,5),
    (6,7,8),
    (0,3,6),
    (1,4,7),
    (2,5,8),
    (0,4,8),
    (2,4,6)
]

def print_board(): 
    print('=============')
    for i in range(3):
        print(f'| {board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]} |')
    print('=============')

def handle_input(player_label: str): 
    while True:
        cell_n = input(f'Выберите клетку: {player_label} ?')
        if not cell_n.isdigit():
            print('ВВедите число')
            continue
        cell_idx = int(cell_n) - 1 
        if board[cell_idx] in "XO":
            print("Клетка занята!")
            continue
        board[cell_idx] = player_label
        break


def get_winner():

    for item in win_ids:
        if board[item[0]] == board[item[1]] == board[item[2]]:
            return board[item[0]]

    return None


def game_XO():
    winner = None
    input_count = 0
    x_turn = True
    while not winner and input_count < len(board):
        print_board()
        handle_input("X" if x_turn else "O")
        x_turn = not x_turn
        input_count += 1
        winner = get_winner()

    print_board()
    if winner:
        print(f'Победитель {winner}')
    else:
        print('Ничья')
    

game_XO()