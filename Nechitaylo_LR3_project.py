def X():
    x = float(input(f"\nВведите вещественное число x: "))
    return x
def Y():
    y = float(input(f"\nВведите вещественное число y: "))
def Z(): 
    z = float(input(f"\nВведите вещественное число z:  "))


def SUMO(x, y, z):
    frac_x = x - int(x)
    frac_y = y - int(y)
    frac_z = z - int(z)
    print(frac_x + frac_y + frac_z)

def CEL_SUMO(x, y, z):
    int_x = int(x)
    int_y = int(y)
    int_z = int(z)
    print(int_x + int_y + int_z)

x, y, z = None, None, None

while True:
    choice = int(input(f"\n1 - Ввести вещественное число x\n2 - Ввести вещественное число y" \
                       "\n3 - Ввести вещественное число z\n4 - Найти сумму дробных частей этих 3-х чисел" \
                       "\n5 - Найти сумму целых частей этих 3-ч чисел" \
                        "\nВведите выбранный вами вариант действия: "))
    if choice == 1:
        x = X()
    elif choice == 2:
        y = Y()
    elif choice == 3:
        z = Z()
    elif choice == 4:
        if x is None or y is None or z is None:
            print(f"\nВнимание! Не все числа введены!")
        else:
            sumo = SUMO(x, y, z)
    elif choice == 5:
        if x is None or y is None or z is None:
            print(f"Внимание! Не все числа введены!")
        else:
            cel_sumo = CEL_SUMO(x, y, z)