#Задача 30: Заполните массив элементами арифметической
#прогрессии. Её первый элемент, разность и количество
#элементов нужно ввести с клавиатуры. Формула для
#получения n-го члена прогрессии: a
#n= a1 + (n-1) * d.
#Каждое число вводится с новой строки.

first_elements = int(input('Введите первый элемент: '))
elements_diff = int(input('Введите разность между элементами: '))
quantity_elements = int(input('Введите количество элементов: '))
def arithmetic_sequence(first_elements: int, elements_diff: int, quantity_elements: int):
    sequence = [first_elements]
    for i in range(2, quantity_elements + 1):
        sequence.append(first_elements + (i - 1) * elements_diff)
    return sequence
def create_list(x: int):
    my_list = []
    for _ in range(x):
        my_list.append(int(input('Введите число: ')))
    return my_list
print(*arithmetic_sequence(first_elements, elements_diff, quantity_elements))