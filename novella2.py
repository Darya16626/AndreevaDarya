import math
print("Игра \"Дорога в техникум\"")
def random():
    import random
    minut = (30, 45, 60, 90)
    sum = minut[random.randrange(len(minut))]
    return sum
sum1 = random()

print(f"\nВы проснулись и поняли, что до начала занятий осталось {sum1} минут.")
print("Выберите ваше действие:\n1 - Быстро собраться и выйти из дома.\n2 - Спокойной собраться и выйти из дома.\n3 - Забить на пары и спать дальше.")
def destvie():
    a = input("Введите номер действия:\t")
    return a

a1 = destvie()
v = {"1": 10, "2": 30, "3": 90}
vv = v.get(a1)
def item():
    print("Что возьмете с собой? 3 вещи")
    item_mn = {0}
    nn = 1
    while nn < 4:
        item = input(f"Введите {nn} вещь\t")
        item_mn.add(item.capitalize())
        nn += 1
    item_mn.remove(0)
    return item_mn
print(f"\nВы взяли с собой: {item()}.")

def beda(beda_kort):
    import random
    beda = beda_kort[random.randrange(len(beda_kort))]
    d_mnog = {5, 10, 15, 20, 25, 30}
    d = d_mnog.pop()
    print(f"\n{beda}. Потеря {d} минут.")
    return d

if a1 == "1":
    beda1_kort = ("Вы забыли ключи", "Вы застряли в лифте", "Вы забыли студеннческий билет", "Вы не причесались")

d1 = beda(beda1_kort)
sum2 = sum1 - vv - d1
def konec(sum22):
    if sum22 <= 0:
        print(f"Вы опоздали на занятие!!!\n\nКонец игры")
        quit()
konec(sum2)
print("\nВы вышли из дома, на чём поедите в техникум?")
print("Выберите ваше действие:\n1 - Метро.\n2 - Такси.\n3 - Пешкарус.")

a2 = int(destvie()) - 1
t = [10, 5, 30]
if a2 == 0:
    beda2_kort = ("Вы попали в давку", "В тоннеле ходит человек..", "Вы поехали в другую сторону")
elif a2 == 1:
    beda2_kort = ("Машина поломалась", "Вы попали в пробку", "Вас остановила полиция")

d2 = beda(beda2_kort)
sum3 = sum2 - t[a2] - d2
konec(sum3)
print("Вы пришли во время. Победа!!!\n\nКонец игры")