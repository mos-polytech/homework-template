def binary_search(my_arr, n, my_min=None, my_max=None):
    """
    Для меня это самый сложный алгоритм из этих четырех.
    Я не понял как реализовать это на питоне. Смотрел также из примера на php
    Так же Часть кода копипастил.
    :param my_arr:
    :param n:
    :param my_min:
    :param my_max:
    :return: recursive function
    """
    if my_min is None or my_max is None:
        my_min = 0
        my_max = len(my_arr) - 1

    middle = (my_min + my_max) // 2

    if my_arr[middle] == n:
        return middle
    elif n < my_arr[middle]:
        return binary_search(my_arr, n, my_min=my_min, my_max=middle - 1)
    else:
        return binary_search(my_arr, n, my_min=middle + 1, my_max=my_max)


if __name__ == '__main__':
    arr = [0, 1, 4, 5, 2, 3]
    result = binary_search(arr, 4)

    if result == -1:
        print('Элемент не найден')
    else:
        print('Индекс элемента =', result)
