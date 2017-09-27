def selection_sort(arrayToSort):
    a = arrayToSort
    for i in range(len(a)):
        idxMin = i
        for j in range(i + 1, len(a)):
            if a[j] < a[idxMin]:
                idxMin = j
        tmp = a[idxMin]
        a[idxMin] = a[i]
        a[i] = tmp
    return a

arr = [1, 0, 65, 24, 28, 15, 178, 128 , 133, 10, 2, 4, 3, 7, 19]
print selection_sort(arr)

#Сортировка выбором заключается в том, что наименьший элемент выбирается поочередно
#сначала ищем наименьший элемент и меняем его с первым элементом в массиве
# ищем следующий наименьший элемент массива и меняем его местами со вторым элементом, 
#продолжаем эти действия, пока весь массив не отсортируется
#
#
#сложность O(n ** 2)
#
