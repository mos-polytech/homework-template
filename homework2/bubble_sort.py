def input_arr(num):
    arr = []
    for i in range(0, num):
        current_elem = float(input('Введите ' + str(i) + ' элемент массива: '))
        arr.append(current_elem)

    return arr


def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


arr = input_arr(int(input('Введите размер массива: ')))
print(bubble_sort(arr))
"""""
Сложность O(n^2)
Малоэффектинвый алгоритм сортировки
Применяется только в учебе
Сравнивает соседние числа и меняет их местами, если это требуется
И так до тех пор, пока все числа не отсортируются
При увеличении кол-ва чисел производительность сильно падает
"""""
