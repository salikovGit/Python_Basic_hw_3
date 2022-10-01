'''
5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

*Пример:*

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
[Негафибоначчи](https://clck.ru/yWbkX.)
'''


def fibonacci(k: int) -> list:
    '''

    :param k: quantity of positive elements
    :return: list of negafibonacci and fibonacci serires
    '''
    nega = []
    fibo = [0, 1]
    for i in range(2, k + 1):
        fibo.append(fibo[i-2] + fibo[i-1])
    for i in range(-1*k, 0)[::-1]:
        nega.append(int(-1*(-1)**(i+1)*fibo[i]))
    return nega + fibo


print(fibonacci(8))
