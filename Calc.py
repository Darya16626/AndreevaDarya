import math

print("Доступные операции:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. Факториал")
print("6. Возведение в степень\n7. Квадратный корень\n8. Синус\n9. Косинус\n10. Тангенс\n")
def get_number():
    while True:
        try:
            num = int(input("Выберите операцию: "))
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод")
number = get_number()
def first_number():
    while True:
        try:
            a = int(input("Введите первое число: "))
            return a
        except ValueError:
            print("Вы НЕ ПРАВИЛЬНО ввели первое число. Повторите ввод")
first_number = first_number()

if number == 1:
    def two_number():
        while True:
            try:
                b = int(input("Введите второе число: "))
                return b
            except ValueError:
                print("Вы НЕ ПРАВИЛЬНО ввели второе число. Повторите ввод")
    two_number = two_number()
    rez = first_number + two_number
    print(f"\nРезультат: {rez}")
if number == 2:
    def two_number():
        while True:
            try:
                b = int(input("Введите второе число: "))
                return b
            except ValueError:
                print("Вы НЕ ПРАВИЛЬНО ввели второе число. Повторите ввод")
    two_number = two_number()
    rez = first_number - two_number
    print(f"\nРезультат: {rez}")
if number == 3:
    def two_number():
        while True:
            try:
                b = int(input("Введите второе число: "))
                return b
            except ValueError:
                print("Вы НЕ ПРАВИЛЬНО ввели второе число. Повторите ввод")
    two_number = two_number()
    rez = first_number * two_number
    print(f"\nРезультат: {rez}")
if number == 4:
    while True:
        b = input("Введите второе число: ")
        if not b.isnumeric():
            print("Вы НЕ ПРАВИЛЬНО ввели второе число. Повторите ввод")
        elif int(b) == 0:
            print("\nВы ввели ноль. Повторите ввод")
        else:
            break
    two_number = b
    rez = first_number / int(two_number)
    print(f"\nРезультат: {rez}")
if number == 5:
    factorial = first_number
    for i in range(1, first_number):
        factorial = factorial * i
    print(f"\nРезультат: {factorial}")
if number == 6:
    def two_number():
        while True:
            try:
                b = int(input("Введите степень: "))
                return b
            except ValueError:
                print("Вы НЕ ПРАВИЛЬНО ввели второе число. Повторите ввод")
    two_number = two_number()
    rez = first_number ** two_number
    print(f"\nРезультат: {rez}")
if number == 7:
    rez = first_number ** 0.5
    print(f"\nРезультат: {rez}")
if number == 8:
    import math
    print("\nРезультат:", math.sin(first_number))
if number == 9:
    import math
    print("\nРезультат:", math.cos(first_number))
if number == 10:
    import math
    print("\nРезультат:", math.tan(first_number))
