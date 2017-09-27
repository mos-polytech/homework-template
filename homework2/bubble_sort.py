def bubble_sort(array):
    '''
    Сложность: всего на места нужно поставить n - 1 элементов,
    при постановке каждого элемента в среднем (n - i - 1) / 2 перестановок.
    То есть (n - 1) * (n - i - 1) / 2, что ассимптотически O(n ** 2)
    '''

    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


if __name__ == '__main__':
    arr = [4, 5, 12, 23, 1, 0, 11, 74, 73, 7]
    bubble_sort(arr)
    print(arr)
