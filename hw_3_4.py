'''
4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.

*Пример:*

- 45 -> 101101
- 3 -> 11
- 2 -> 10

'''


def get_binary_format(number):
    '''

    :param number:
    :return: binary form of original decimal number
    '''
    list_of_nums = []
    while True:
        if number < 2:
            list_of_nums.append(number % 2)
            break
        remainder = number % 2
        list_of_nums.append(remainder)
        number //= 2
    list_of_nums = list(map(str, list_of_nums))
    return int(''.join(list_of_nums[::-1]))


print(get_binary_format(5))
print(get_binary_format(4))
