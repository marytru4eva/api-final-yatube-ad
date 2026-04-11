# adjective = input("Введите прилагательное : ")
# noun = input("ВВедите существительное: ")
# verb = input("Введите глагол в прошедшем времени: ")
# print("Ваша чепуха :")
# print("Этот ", adjective, noun, verb, "на ленивую рыжую собаку .")


# adjective = input("Введите прилагательное : ")
# noun = input("ВВедите существительное: ")
# verb = input("Введите глагол в прошедшем времени (м.р, ед.ч.): ")
# animal = input("Введите название животного с предлогом «на»")
# print("Ваша история :")
# print("Этот ", adjective, noun, verb, animal + ".")

import turtle
t = turtle.Pen()
turtle.bgcolor('black')
sides = 5
sides = int(input('ВВедите количество сторон от 2 до 6: '))
colors = [
    "red", "yellow", "blue", "orange", "green",
    "purple",
    # "white", "pink", "cyan", "magenta"
    ]
# print(f"Рисуем спираль с {sides} сторонами")
# print(f"Используем цвета: {', '.join(colors[:sides])}")

for x in range(360):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
# print("Готово! Закройте окно.")
turtle.done()
