arr = [9, 4, 7, 0, ]

print(arr)
length = len(arr)
m = length - 1
while m > 0:
    for i in range(m):
        if arr[i] > arr[i + 1]:
            x = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = x
    m = m - 1
print(arr)
