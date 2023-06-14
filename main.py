

import math
import random


def test_greetings():
    # Напишите программу, которая выводит на экран приветствие.

    name = 'Дамир'
    age = '37'

    text = f"Привет, меня зовут {name}. Мне {age} лет."
    print(text)
    assert text == "Привет, меня зовут Дамир. Мне 37 лет."

test_greetings()

def test_test_rectangle():
    # Напишите программу, которая берет длину и ширину прямоугольника и считает его периметр и площадь.

    length = 13
    width = 15
    perimetr = (length + width) * 2
    area = length * width
    text = f"периметр: {perimetr}, площадь: {width}"
    print (text)
    assert text == "периметр: 56, площадь: 15"

test_test_rectangle()

def test_rectangle():
    #Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    #Используйте константу PI

    radius = 21

    area = math.pi * radius**2
    perimetr = 2 * math.pi * radius

    text = f"Периметр: {perimetr}, площадь окружности: {area}"
    assert text == "Периметр: 131.94689145077132, площадь окружности: 1385.4423602330987"

    print(text)

test_rectangle()

def test_random_list():
    #Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.

    random_list = sorted(random.sample(range(1, 100), 10))

    print(random_list)

    assert len(random_list) == 10
    assert random_list[0] < random_list[-1]

test_random_list()

def test_unique_elements():
#Удалите из списка все повторяющиеся элементы

    spisok = [42, 3, 4, 4, 4, 2, 55, 44, 23, 12]
    spisok2 = list(set(spisok))
    print(spisok2)
    assert spisok2 == [2, 3, 4, 42, 44, 12, 23, 55]
test_unique_elements()

def test_dicts():
#Создайте словарь из двух списков. Используйте первый список как ключи, а второй - как значения.
#Выведите на экран все значения словаря. Подсказка: используй встроенную функцию zip.
    sp1 = [3, 4, 5, 6]
    sp2 = ['a', 's', 'd', 'b']
    sp12 = list(zip(sp1, sp2))
    print(sp12)
    assert sp12 ==[(3, 'a'), (4, 's'), (5, 'd'), (6, 'b')]
test_dicts()