arr = [0, 3, 5, 7, 10, 20, 28, 30, 45, 56]
need = 56
i = 0
j = len(arr) - 1
middle = int(j / 2)
while arr[middle] != need and i < j:
    if need > arr[middle]:
        i = middle + 1
    else:
        j = middle - 1
    middle = int((i + j) / 2)

if i > j:
    print('Элемент не найден')
else:
    print('Индекс элемента: ', middle)
