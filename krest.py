pole = [[' '] * 3 for i in range(3)]
igrok = "X"
schet = 1
def razmetka():
    print(f'    0   1   2')
    for i in range(3):
        print(f'{i} | {" | ".join(pole[i])} |')
razmetka()
def hod():
    global igrok
    global schet
    while True:
        coordynaty = input('Выбирите номер столбца и строки в значении от 0-2 через пробел: ').split()
        if len(coordynaty) != 2:
            print('Вы ввели неверное число')
            continue
        else:
            x, y = coordynaty
        if not(x.isdigit()) or not (y.isdigit()):
            print('Введите числа!')
            continue
        x, y = int(x), int(y)

        if 0 <= x < 3 and 0 <= y < 3:
            if pole[y][x] == " ":
                pole[y][x] = igrok
                razmetka()
                schet += 1
                if schet % 2 == 0:
                    igrok = '0'
                else:
                    igrok = 'X'

            else:
                print('Поле занято')
        else:
            print('Вы ввели неправильное число')


hod()