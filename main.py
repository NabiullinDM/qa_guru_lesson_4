

import math
import random


def test_greetings():
    # Напишите программу, которая выводит на экран приветствие.

    name = 'Дамир'
    age = '37'

    text = f"Привет, меня зовут {name}. Мне {age} лет."
    print(text)


test_greetings()

def test_test_rectangle():
    # Напишите программу, которая берет длину и ширину прямоугольника и считает его периметр и площадь.

    length = 13
    width = 15
    perimetr = (length + width) * 2
    area = length * width

    print (f"периметр: {perimetr}, площадь: {width}")

test_test_rectangle()

def test_rectangle():
    #Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    #Используйте константу PI

    radius = 21

    area = math.pi * radius**2
    perimetr = 2 * math.pi * radius

    text = f"Периметр: {perimetr}, площадь окружности: {area}"
    print(text)

test_rectangle()

def test_random_list():
    #Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    list_new = []

    for a in range(10):
        namber = random.randint(1,100)
        list_new.append(namber)
    list_new.sort()
    print(list_new)

test_random_list()

def test_unique_elements():
#Удалите из списка все повторяющиеся элементы

    spisok = [42, 3, 4, 4, 4, 2, 55, 44, 23, 12]
    spisok2 = list(set(spisok))
    print(spisok2)

test_unique_elements()

def test_dicts():
#Создайте словарь из двух списков. Используйте первый список как ключи, а второй - как значения.
#Выведите на экран все значения словаря. Подсказка: используй встроенную функцию zip.
    sp1 = [3, 4, 5, 6]
    sp2 = ['a', 's', 'd', 'b']
    sp12 = list(zip(sp1, sp2))
    print(sp12)

test_dicts()