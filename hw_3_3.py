'''
3-Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

*Пример:*

- [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
 - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91
'''


def get_fractional_part(list_of_nums):
    '''

    :param list_of_nums: list of float numbers
    :return: difference between max and min fractional part of elements in original list
    '''
    list_of_fractionals = []
    for el in list_of_nums:
        list_of_fractionals.append('0.' + str(el).split('.')[-1])
        list_of_fractionals = list(map(float, list_of_fractionals))
    return round(max(list_of_fractionals) - min(list_of_fractionals), 2)


print(get_fractional_part([1.1, 1.2, 3.1, 5.17, 10.02]))
print(get_fractional_part([4.07, 5.1, 8.2444, 6.98]))
