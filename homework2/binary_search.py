def binary_search(arr, key):
    minimum = 0
    maximum = len(arr) - 1
    while minimum < maximum:
        middle = (minimum + maximum) // 2
        if key == arr[middle]:
            return middle
        elif key < arr[middle]:
            maximum = middle - 1
        elif key > arr[middle]:
            minimum = middle + 1
    return 'Элемент не найден'


arr = [1, 3, 5, 6, 7, 9]
key = 5
print(binary_search(arr, key))
