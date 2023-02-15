#Задача 18: Требуется найти в массиве A[1..N] самый близкий по
#вводит натуральное число N – количество элементов в массиве. В
#последующих строках записаны N целых чисел Ai. Последняя строка
#содержит число X
#5
#1 2 3 4 5
#6
#-> 5
from random import randint
size = int(input('Введите размер списка: '))
numbers = tuple(randint(1, size) for _ in range(size))
print(*numbers)
num_X = int(input('Введите число! я скажу близкое ему число по величине: '))
num_value = 0
argument = False
for _ in range(len(set(numbers))):
    for i in set(numbers):
        if i == num_X - num_value or i == num_X + num_value:
            print(i)
            argument = True
            break
    if argument:
        break
    num_value += 1