def sort3(array):
    for i in range(len(array)):
        j = array[i]
        while (array[i - 1] > j) and (i > 0):
            array[i] = array[i - 1]
            i = i - 1
        array[i] = j
    return array


arr = [6, 5, 3, 1, 8, 7, 2, 4]
print(sort3(arr))

# Сложность O(n^2)
# Алгоритм последовательно создаёт массивы из элесентов большого массива
# Который подаётся на вход, затем сравнивает каждый элемент из большого массива
# С подмассивом, и добавляет элемент либо в начало, либо в конец.
# В худшем случае в исходном массиве все элементы стоят в обратном порядке
# Тогда алгоритму необходимо будет провести O(n^2) операций