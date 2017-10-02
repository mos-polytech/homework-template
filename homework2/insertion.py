def insertion_sort(arr):
    """
    Этот алгоритм мне тоже пришлось понимать на примере языка php.
    не совсем понятен синтаксис arr[i], arr[i - 1] = arr[i - 1], arr[i]
    здесь в некоторых местах пришлось заняться копипастом
    :param arr:
    :return:
    """
    for i in range(1, len(arr)):
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1

    return arr


if __name__ == '__main__':
    my_arr = [1, 5, 2, 3, 4, 0]
    result = insertion_sort(my_arr)
    print(result)
