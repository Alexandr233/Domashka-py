#Задача 16: Требуется вычислить, сколько раз встречается некоторое
#число X в массиве A[1..N]. Пользователь в первой строке вводит
#натуральное число N – количество элементов в массиве. В последующих
#строках записаны N целых чисел Ai
#. Последняя строка содержит число X
#5
#1 2 3 4 5
#3
#-> 1
from random import randint
size = int(input('Введите размер списка: '))
nums_list = [randint(1, size)
for _ in range(size)]
print(*nums_list)
print(nums_list.count(int(input('Введите число! скажу сколько раз оно повторилось: '))))


