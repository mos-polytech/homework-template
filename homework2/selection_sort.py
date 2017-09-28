def selection_sort(list):
    a = list
    for i in range(len(a)):
        idxMin = i
        for j in range(i+1, len(a)):
            if a[j] < a[idxMin]:
                idxMin = j
        tmp = a[idxMin]
        a[idxMin] = a[i]
        a[i] = tmp
    return a

arr = [1, 8, 4, 10, 7, 3]
print(selection_sort(arr))