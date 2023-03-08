def find_rhythm(text: str):
    phrases = text.split()
    phrases_vow = []
    for i in phrases:
        phrases_vow.append(list(filter(lambda x: x in 'аеиоуэюя', list(i))))
    result_list = map(lambda x: len(x) == len(phrases_vow[0]), phrases_vow)
    return all(result_list)


def print_operation_table(operation, num_rows=6, num_columns=6):
    matrix = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for x in range(num_rows):
        temp = []
        for y in range(num_columns):
            temp.append(str(matrix[x][y]).ljust(3))
        print(*temp)

def print_operation_table1(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(str(operation(i, j)).ljust(3), end=' ')
        print()