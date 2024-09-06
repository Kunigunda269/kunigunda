def draw_area():
    for i in area:
        print(*i)
    print()


def check_winner():
    for row in area:
        if row[0] == row[1] == row[2] and row[0] != '*':
            return True
    for col in range(3):
        if area[0][col] == area[1][col] == area[2][col] and area[0][col] != '*':
            return True
    if area[0][0] == area[1][1] == area[2][2] and area[0][0] != '*':
        return True
    if area[0][2] == area[1][1] == area[2][0] and area[0][2] != '*':
        return True

    return False


area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print('Добро пожаловать в Крестики-Нолики')
print('-----------------')
draw_area()

for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = '0'
        print('Ходят нолики')
    else:
        turn_char = 'X'
        print('Ходят крестики')

    row = int(input('Введите номер строки (1,2,3): ')) - 1
    column = int(input('Введите номер столбца (1,2,3): ')) - 1

    if area[row][column] == '*':
        area[row][column] = turn_char
    else:
        print('Ячейка уже занята, попробуйте снова.')
        continue

    draw_area()

    if check_winner():
        print(f'Победили {turn_char}!')
        break
else:
    print('Ничья!')
