def insertion_sort(array):
    '''
    Сложность: внешний цикл работает n - 1 раз, внутренний,
    в среднем случае, i / 2, и при этом i зависит от n.
    То есть (n - 1) * n / 2, что асимптотически O(n ** 2)
    '''

    for i in range(1, len(array)):
        j = i - 1

        while j >= 0 and array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            j -= 1


if __name__ == '__main__':
    arr = [5, 4, 12, 23, 1, 0, 11, 74, 73, 7]
    insertion_sort(arr)
    print(arr)
