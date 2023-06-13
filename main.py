pole = [[' '] * 3 for i in range(3)]
igrok = "X"
schet = 1
print('Добро пожаловать в игру \n    крестики-нолики\nвводите поле в формате x, y\nгде x - строка, y - столбец')


def win():
    winline = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
               ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
               ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))
               ]
    for line in winline:
        a = line[0]
        b = line[1]
        c = line[2]
        if pole[a[0]][a[1]] == pole[b[0]][b[1]] == pole[c[0]][c[1]] != " ":
            print(f'Выиграл {pole[a[0]][a[1]]}')
            return True
    return False


def razmetka():
    print(f'    0   1   2')
    for i in range(3):
        print(f'{i} | {" | ".join(pole[i])} |')


razmetka()


def hod():
    global igrok
    global schet
    while True:
        coordynaty = input('Выбирите номер строки и столбца в значении от 0-2 через пробел: ').split()
        if len(coordynaty) != 2:
            print('Вы ввели неверное число')
            continue
        else:
            x, y = coordynaty  # присвоение координат, можно сменить столбцы на строки
        if not (x.isdigit()) or not (y.isdigit()):
            print('Введите числа!')
            continue
        x, y = int(x), int(y)

        if 0 <= x < 3 and 0 <= y < 3:
            if pole[x][y] == " ":
                pole[x][y] = igrok
                razmetka()
                if win():
                    return
                schet += 1
                if schet % 2 == 0:
                    igrok = '0'
                else:
                    igrok = 'X'
            else:
                print('Поле занято')
        else:
            print('Вы ввели неправильное число')
        if schet == 10:
            print('Ничья')
            break


hod()
