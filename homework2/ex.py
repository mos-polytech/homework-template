
def selection_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j
        t = array[min]
        array[min] = array[i]
        array[i] = t
    return array

arr = [input() for i in range(int(input()))]
print(selection_sort(arr))
