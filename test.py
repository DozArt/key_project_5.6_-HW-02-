def greet():
    print('-----------------------')
    print('Добро пожаловать в игру')
    print('  "Крестики - нолики"')
    print('-----------------------')
    print('формат ввода: x y')
    print('x - номер строки')
    print('y - номер столбца')


def format_matrix(mat):  # Форматирование матрицы
    size = range(len(mat))  # Размер матрицы
    b = " "  # отступ первой строки
    for a in size:  # первая строка  str("0  1  2 ... n-1")
        b += "  " + str(a)
    for a in size:  # последующие строки матрицы с номерацией
        b += f"\n{a}  " + "  ".join(mat[a])
    return b


def step(mat):  # Запрос координат с проверкой по матрице
    while True:
        coord = input("Введите координаты: ")

        if (
            len(coord) != 3 or
            not coord[0].isdigit() or
            not coord[2].isdigit() or
            not size_matrix > int(coord[0]) >= 0 or
            not size_matrix > int(coord[2]) >= 0 or
            coord[1] != " "
        ):
            print('введите координаты в формате "x y"')
            continue
        loyal_x = int(coord[0])
        loyal_y = int(coord[2])

        if mat[loyal_x][loyal_y] != "-":
            print("Клетка занята")
            continue
        return loyal_x, loyal_y


def search_left_top(mat, x, y):  # проверка совпадений по диагонали в лево в верх
    if mat[x][y] == mat[x-1][y-1] and x > 0 and y > 0:
        return search_left_top(mat, x - 1, y - 1)
    else:
        return x, y


def search_right_bottom(mat, x, y):  # проверка совпадений по диагонали в право в вниз
    size = len(mat)
    if x < size - 1 and y < size - 1 and mat[x][y] == mat[x + 1][y + 1]:
        return search_right_bottom(mat, x + 1, y + 1)
    else:
        return x, y

def search_left_bottom(mat, x, y):  # проверка совпадений по диагонали в лево в низ
    size = len(mat)
    if x < size - 1 and mat[x][y] == mat[x+1][y-1] and y > 0:
        return search_left_bottom(mat, x + 1, y - 1)
    else:
        return x, y


def search_right_top(mat, x, y):  # проверка совпадений по диагонали в право в верх
    size = len(mat)
    if y < size - 1 and x > 0 and mat[x][y] == mat[x - 1][y + 1]:
        return search_right_top(mat, x - 1, y + 1)
    else:
        return x, y


def search_left(mat, x, y):
    if mat[x][y] == mat[x][y-1] and y > 0:
        return search_left(mat, x, y - 1)
    else:
        return x, y


def search_right(mat, x, y):
    size = len(mat)
    if y < size - 1 and mat[x][y] == mat[x][y + 1]:
        return search_right(mat, x, y + 1)
    else:
        return x, y


def search_top(mat, x, y):
    if mat[x][y] == mat[x-1][y] and x > 0:
        return search_top(mat, x - 1, y)
    else:
        return x, y


def search_bottom(mat, x, y):
    size = len(mat)
    if x < size - 1 and mat[x][y] == mat[x + 1][y]:
        return search_bottom(mat, x + 1, y)
    else:
        return x, y


def win_center(mat, x, y):
    x0, y0 = search_left_top(matrix, x, y)
    x1, y1 = search_right_bottom(matrix, x0, y0)
    if (x1 - x0) == 4:
        print(f"победа игрока {player}")
    x0, y0 = search_left_bottom(matrix, x, y)
    x1, y1 = search_right_top(matrix, x0, y0)
    if (x0 - x1) == 4:
        print(f"победа игрока {player}")
    x0, y0 = search_left(matrix, x, y)
    x1, y1 = search_right(matrix, x0, y0)
    if (y1 - y0) == 4:
        print(f"победа игрока {player}")
    x0, y0 = search_top(matrix, x, y)
    x1, y1 = search_bottom(matrix, x0, y0)
    if (x1 - x0) == 4:
        print(f"победа игрока {player}")


def win(mat):
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(mat[c[0]][c[1]])
        if symbols == ["x", "x", "x"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["o", "o", "o"]:
            print("Выиграл 0!!!")
            return True
    return False

# Start = str(input("Желаете начать игру? (Y/N): "))
#
# if Start == "Y":


size_matrix = 9  # max 10. сделать проверку
matrix = [["-"] * size_matrix for i in range(size_matrix)]  # создаем матрицу по заданному размеру

greet()
number_iter = 1
The_and = False
while True:
    player = "o" if number_iter % 2 == 0 else "x"  # нечетным ходит игрок крестик
    print(f'=шаг:{number_iter}============================')
    if win(matrix):  # проверяем на победу
        The_and = True
    elif number_iter > size_matrix ** 2:  # Если шагов больше 9 и нет победителей
        print("Ничья")
        The_and = True
    else:
        print(f'Ход игрока {player}')
    print(format_matrix(matrix))  # выводим отформатированную матрицу
    if The_and:
        break
    x, y = step(matrix)  # запрашиваем координаты и проверяем
    number_iter += 1  # следующий шаг, будет ходить другой игрок
    matrix[x][y] = player  # Ставим крестик по координатом "y" строка, "x" столбец
    win_center(matrix, x, y)
