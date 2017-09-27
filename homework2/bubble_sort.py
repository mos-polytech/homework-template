def bubble_sort(array):
    a = array
    for i in range(len(a), 0, -1):
        for j in range(1, i):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
    return a


arr = [55, 48, 0, 1, 2, 22, 11, 1, 7, 5, 4, 125265]
print(bubble_sort(arr))

# Суть сортировки пузырьком состоит в сравнении, мы сравниваем первые два элемента
# если первый больше второго, меняем местами
# если первый меньше второго, мы оставляем все так и сравниваем второй и третий элементы
# и так до тех пор, пока не вытесним наибольший элемент в конец
# сложность O(n * n)
