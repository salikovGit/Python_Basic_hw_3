'''
2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
второй и предпоследний и т.д.

*Пример:*

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''


def get_pair_sum(list_of_numbers):
    '''
    :param list_of_numbers: original list of integers
    :return: list with products of paired elements of the original list
    '''
    result_list = []
    if len(list_of_numbers) % 2 == 0:
        for i in range(len(list_of_numbers) // 2):
            result_list.append(list_of_numbers[i] * list_of_numbers[i*(-1) - 1])
    else:
        for i in range(len(list_of_numbers) // 2):
            result_list.append(list_of_numbers[i] * list_of_numbers[i*(-1) - 1])
        result_list.append((list_of_numbers[len(list_of_numbers) // 2 ])**2)
    return result_list


print(get_pair_sum([2, 3, 5, 6]))
print(get_pair_sum([2, 3, 4, 5, 6]))
