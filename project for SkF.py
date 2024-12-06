def intro():
    print("-------------------")
    print("                   ")
    print("  крестики-нолики  ")
    print("                   ")
    print("-------------------")
    print(" Формат ввода: x,y ")
    print(" X - номер строки  ")
    print(" Y - номер столбца ")

def show_frame():

    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {frame[i][0]} {frame[i][1]} {frame[i][2]}")


def ask():
    while True:

        coordinates = input("Ходите: ").split()
        if len(coordinates) != 2:
            print("Пожалуйста, введите 2 координаты")
            continue

        x, y = coordinates

        if not(x.isdigit()) or not(y.isdigit()):
            print("Пожалуйста, введите числа")
            continue
        x, y = int(x), int(y)
        if 0 <= x <= 2 and 0 <= y <= 2:
            if frame[x][y] == " ":
                return x, y
            else:
                print("Клетка занята")
        else:
            print("Координата вне диапозона")

def win_check():
    win_cords = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cords in win_cords:
        symbols = []
        for z in cords:
            symbols.append(frame[z[0]][z[1]])
        if symbols == ["x", "x", "x"]:
            print("Выиграл X!")
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
    return False

frame = [
["", " ", ""],
["", " ", ""],
["", " ", ""]
]
win_check()
intro()
frame = [[" ", " ", " "] for i in range(3)]
count = 0
while True:
    count += 1
    show_frame()

    if count % 2 == 1:
        print("Ходит X")


    else:
        print("Ходит 0")

    x, y = ask()

    if count % 2 == 1:
        frame[x][y] = "x"
    else:
        frame[x][y] = "0"


    if count == 9:
        print("Ничья")
        break
    if win_check():
        break