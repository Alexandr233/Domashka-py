from homework_6 import create_list, indexes_of_numbers

num_list = create_list(int(input('Введите размер массива: ')))
left_endpoint = int(input('Введите MIN диапазона: '))
right_endpoint = int(input('Введите MAX диапазона: '))

print(*num_list)
print(*indexes_of_numbers(num_list, left_endpoint, right_endpoint))

