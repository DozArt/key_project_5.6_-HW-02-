def red(text):  # Важное будем подсвечивать красным
    return f'\033[31m{text}\033[0m'


def greet():
    print('-----------------------')
    print('Добро пожаловать в игру')
    print('  "Крестики - нолики"')
    while True:
        while True:
            print('-----------------------')
            size = int(input('Введите размер игрового\nполя от 3 до 10: '))
            if 3 <= size <= 10:
                break

        # Задаем длинну совпадений для выигрыша
        if size <= 4:
            long = 3
        elif size == 5:
            long = 4
        else:
            long = 5  # игра "Пять в ряд"

        print('-----------------------')
        print('  Ваша задача занять')
        print(f'   ряд из {red(long)} ячеек')
        print('\n')
        print('формат ввода: x y')
        print('x - номер строки')
        print('y - номер столбца')
        if input('Готовы начать игру? (y/n): ') == "y":
            return size, long
        else:
            continue


def format_matrix(mat):  # Форматирование игрового поля
    size = range(len(mat))  # Размер матрицы
    b = " "  # отступ первой строки
    for a in size:  # первая строка  str("0  1  2 ... n-1")
        b += "  " + str(a)
    for a in size:  # последующие строки матрицы с номерацией
        b += f"\n{a}  " + "  ".join(mat[a])
    return b


def step(mat):  # Запрос координат с проверкой по матрице
    while True:
        coord = input("Введите координаты: ").split()

        if len(coord) != 2:
            print('Введите две координаты')
            continue
        elif (
            not coord[0].isdigit() or
            not coord[1].isdigit()
        ):
            print('Введите два числа')
            continue
        elif (
            not size_matrix > int(coord[0]) >= 0 or
            not size_matrix > int(coord[1]) >= 0
        ):
            print('Координаты вне диапазона')
            continue
        loyal_x = int(coord[0])
        loyal_y = int(coord[1])

        if mat[loyal_x][loyal_y] != "-":
            print("Клетка занята")
            continue
        return loyal_x, loyal_y


# Набор функций для проверки на выигрыш
# Ищем совпадения в 6 направлениях начиная от введенной координаты
# Получаем координаты трех линий
# Если разница координат равна 2 то длинна линии - 3 одинаковых символа
# Контрольное количество символов зависит от размера игрового поля

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


def win_center(mat, x, y, lo):  # Проверка на победу
    if x is None or y is None:  # Проверять еще нечего
        return False
    x0, y0 = search_left_top(mat, x, y)
    x1, y1 = search_right_bottom(mat, x, y)
    if (x1 - x0) == (lo - 1):  # длинна линии по первой диагонали
        print(f"победа игрока {mat[x][y]}")
        return True
    x0, y0 = search_left_bottom(mat, x, y)
    x1, y1 = search_right_top(mat, x, y)
    if (x0 - x1) == (lo - 1):  # длинна линии по второй диагонали
        print(f"победа игрока {mat[x][y]}")
        return True
    x0, y0 = search_left(mat, x, y)
    x1, y1 = search_right(mat, x, y)
    if (y1 - y0) == (lo - 1):  # длинна линии по горизонтали
        print(f"победа игрока {mat[x][y]}")
        return True
    x0, y0 = search_top(mat, x, y)
    x1, y1 = search_bottom(mat, x, y)
    if (x1 - x0) == (lo - 1):  # длинна линии по вертикали
        print(f"победа игрока {mat[x][y]}")
        return True
    return False

# Start = str(input("Желаете начать игру? (Y/N): "))
#
# if Start == "Y":


size_matrix, long_win = greet()  # max 10. сделать проверку

matrix = [["-"] * size_matrix for i in range(size_matrix)]  # создаем матрицу по заданному размеру

# greet()
number_iter = 1
The_and = False
X, Y = None, None
while True:
    player = "o" if number_iter % 2 == 0 else "x"  # нечетным ходит игрок крестик
    print(f'=шаг:{number_iter}=========================')

    if win_center(matrix, X, Y, long_win):  # проверяем на победу
        The_and = True
    elif number_iter > size_matrix ** 2:  # Если шагов больше чем клеток
        print("Ничья")
        The_and = True
    else:
        print(f'Ход игрока {player}')

    print(format_matrix(matrix))  # выводим отформатированную матрицу

    if The_and:
        break

    X, Y = step(matrix)  # запрашиваем координаты и проверяем
    number_iter += 1  # следующий шаг, будет ходить другой игрок
    matrix[X][Y] = player  # Ставим x/o по координатам
