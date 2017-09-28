arr = [10, 5, 3, 0, 8, ]
print (arr)
first = 0
while first < len(arr) - 1:
    min = first
    i = first + 1
    while i < len(arr):
        if arr[i] < arr[min]:
            min = i
        i += 1
    save = arr[first]
    arr[first] = arr[min]
    arr[min] = save
    first += 1

print(arr)
