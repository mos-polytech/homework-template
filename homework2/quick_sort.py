def input_arr(num):
    arr = []
    for i in range(0, num):
        current_elem = float(input('Введите ' + str(i) + ' элемент массива: '))
        arr.append(current_elem)

    return arr


def quick_sort(b, e):
    start = b
    end = e
    supporting_elem = arr[int((start + end) / 2)]

    while start <= end:
        while arr[start] < supporting_elem:
            start += 1
        while arr[end] > supporting_elem:
            end -= 1
        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    if b < end:
        quick_sort(b, end)
    if e > start:
        quick_sort(start, e)
    return arr


arr = input_arr(int(input('Введите размер массива: ')))
print(quick_sort(0, len(arr) - 1))


# Сложность данного алгоритма в среднем O(n log n)
# Пробегая данный исходный массив он постоянно разбивается на мелкие части,
# после чего каждая из частей сортируется относительно опорного элемента
# Не эффективен на малом кол-ве чисел
# Тем не менее, при сравнении с другими алгоритмами сортировки выигрывает
# в большинстве случаев
