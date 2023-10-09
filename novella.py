import math
print("Игра \"Дорога в техникум\"")
import random
minut = (30, 45, 60, 90)
sum = minut[random.randrange(len(minut))]
print(f"\nВы проснулись и поняли, что до начала занятий осталось {sum} минут.")
print("Выберите ваше действие:\n1 - Быстро собраться и выйти из дома.\n2 - Спокойной собраться и выйти из дома.\n3 - Забить на пары и спать дальше.")
a = input("Введите номер действия:\t")
v = {"1": 10, "2": 30, "3": 90}
vv = v.get(a)
print("Что возьмете с собой? 3 вещи")
item_mn = {0}
nn = 1
while nn < 4:
    item = input(f"Введите {nn} вещь\t")
    item_mn.add(item.capitalize())
    nn += 1
item_mn.remove(0)
print(f"\nВы взяли с собой: {item_mn}.")
d_mnog = {5, 10, 15, 20, 25, 30}
d = 0
if a == "1":
    beda_kort = ("Вы забыли ключи", "Вы застряли в лифте", "Вы забыли студеннческий билет", "Вы не причесались")
    beda = beda_kort[random.randrange(len(beda_kort))]
    d = d_mnog.pop()
    print(f"\n{beda}. Потеря {d} минут.")
sum2 = sum - vv - d
if sum2 <= 0:
    print(f"Вы опоздали на занятие!!!\n\nКонец игры")
    quit()
print("\nВы вышли из дома, на чём поедите в техникум?")
print("Выберите ваше действие:\n1 - Метро.\n2 - Такси.\n3 - Пешкарус.")
a = int(input("Введите номер действия:\t")) - 1
t = [10, 5, 30]
dd = 0
if a == 0:
    beda_kort2 = ("Вы попали в давку", "В тоннеле ходит человек..", "Вы поехали в другую сторону")
    beda2 = beda_kort2[random.randrange(len(beda_kort2))]
    dd = d_mnog.pop()
    print(f"\n{beda2}. Потеря {dd} минут.")
elif a == 1:
    beda_kort2 = ("Машина поломалась", "Вы попали в пробку", "Вас остановила полиция")
    beda2 = beda_kort2[random.randrange(len(beda_kort2))]
    dd = d_mnog.pop()
    print(f"\n{beda2}. Потеря {dd} минут.")
sum3 = sum2 - t[a] - dd
if sum3 <= 0:
    print("Вы опоздали на занятие!!!\n\nКонец игры")
    quit()
else:
    print("Вы пришли во время. Победа!!!\n\nКонец игры")