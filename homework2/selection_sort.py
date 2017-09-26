def input_arr(num):
    arr = []
    for i in range(0, num):
        current_elem = float(input('Введите ' + str(i) + ' элемент массива: '))
        arr.append(current_elem)

    return arr


def selection_sort(arr):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


arr = input_arr(int(input('Введите размер массива: ')))
print(selection_sort(arr))

# Сложность O(n^2)
# Еще один малоэффективный алгоритм сортировки
# Проходит каждый элемент массива и ищет на его место
# минимальный(максимальный) элемент
# Который ставит меняет местами с текущим элементом массива
