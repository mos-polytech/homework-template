def insertion_sort(arr):
    for i in range(len(arr)):
        element = arr[i]
        j = i;
        while (arr[j - 1] > element) and (j > 0):
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = element
    return arr


arr = [2, 5, 3, 8, 5]
print(insertion_sort(arr))
