def bubble_sort(arr):
    for j in range(len(arr) - 1):
            for i in range(len(arr) - 1):
                    if arr[i] > arr[i + 1]:
                            isave = arr[i]
                            arr[i] = arr[i + 1]
                            arr[i + 1] = isave
                    i += 1
                    j += 1
    print(arr)

arr = [4, 3, 8, 5, 5, 2]
bubble_sort(arr)
