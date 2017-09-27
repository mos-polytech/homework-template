def selection_sort(array):
    '''
    Сложность: алгоритм в любом случае пробегает n - 1 раз
    по n - i элементам. O(n ** 2)
    '''

    for i in range(len(array) - 1):
        min_element = i

        for j in range(i+1, len(array)):
            if array[j] < array[min_element]:
                min_element = j

        array[min_element], array[i] = array[i], array[min_element]


if __name__ == '__main__':
    arr = [5, 4, 12, 23, 1, 0, 11, 74, 73, 7]
    selection_sort(arr)
    print(arr)
