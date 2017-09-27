def binary_search(array, n, low=None, high=None):
    '''
    Сложность: можно заметить, что поиск завершается, если размер
    рассматриваемого подмассива равен 1 (если элемент существует).

    При том, что каждый раз подмассив уменьшается вдвое (начиная с длины s),
    остается посчитать сколько раз нужно поделить s на 2, чтобы получилась единица.

    Другими словами, сколько раз нужно умножить 1 на 2, чтобы получить s.
    То есть при каком x величина 2 ** x достигнет s. x = log(2)s. O(lg(n))
    '''

    if low is None or high is None:
        low = 0
        high = len(array) - 1

    middle = (low + high) // 2

    try:
        if array[middle] == n:
            return middle
        elif n < array[middle]:
            return binary_search(array, n, low=low, high=middle-1)
        else:
            return binary_search(array, n, low=middle+1, high=high)
    except RecursionError:
        return -1


if __name__ == '__main__':
    arr = [0, 1, 4, 5, 7, 11, 12, 23, 73]
    found_index = binary_search(arr, 0)

    if found_index == -1:
        print('Такого элемента не существует')
    else:
        print('Индекс элемента, который вы ищете: ', found_index)
