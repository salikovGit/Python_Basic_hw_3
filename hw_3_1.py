'''
1- Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на нечётной позиции.

*Пример:*

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''


numbers = [2, 3, 5, 9, 3]


def get_odd_sum(list_of_nums):
    '''
    :param list_of_nums: list of some integers
    :return: sum of elements in odd positions
    '''
    return sum(list_of_nums[1::2])


print(get_odd_sum(numbers))
