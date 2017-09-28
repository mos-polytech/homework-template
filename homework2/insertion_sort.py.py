arr = [5, 52, 3, 1, 9, 6, 7,]
print(arr)
for i in range(len(arr)):
        num = arr[i]
        index = i;
        while (arr[index - 1] > num) and (index > 0):
            arr[index] = arr[index - 1]
            index = index - 1
            arr[index] = num
print(arr)
