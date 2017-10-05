def insertion_sort(array):
    a = array
    for i in range(len(a)):
        k = a[i]
        j = i
        while (a[j - 1] > k) and (j > 0):
            a[j] = a[j - 1]
            j = j - 1
        a[j] = k
    return a


arr = [54, 0, 11, 22, 1, 7, 5, 3, 4, 6, 2]
print(insertion_sort(arr))


# из массива последовательно берется каждый элемент
# и вставляется в отсортированную часть(например в начале массива или конце)
# Сложность O(n ** 2)
