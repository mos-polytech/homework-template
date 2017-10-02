def bubble_sort(arr):
    """
    По мне самый удобный и легкий алгоритм сортировки,
    потому что логика достаточно понятна и использованны базовые элементы
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr


if __name__ == '__main__':
    my_arr = [0, 5, 1, 9, 2, 6, 4]
    result = bubble_sort(my_arr)
    print(result)
