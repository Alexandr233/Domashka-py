#Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k, не превосходящие числа N.

num = int(input("Введите положительное число "))
pow = 1
power = 1
while pow < num:
    print(pow, end=' ')
    pow = 2 ** power
    power += 1
    result = pow
