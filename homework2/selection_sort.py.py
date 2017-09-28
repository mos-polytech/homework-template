arr = [10, 5, 3, 0, 8, ]
print(arr)
first = 0
while first < len(arr) - 1:
    mini = first
    i = first + 1
    while i < len(arr):
        if arr[i] < arr[mini]:
            mini = i
        i += 1
    save = arr[first]
    arr[first] = arr[mini]
    arr[mini] = save
    first += 1

print(arr)
