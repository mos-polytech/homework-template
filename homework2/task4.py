def BinSearch(li, x):
    i = 0
    j = len(li) - 1
    m = int(j / 2)
    while li[m] != x and i < j:
        if x > li[m]:
            i = m + 1
        else:
            j = m - 1
        m = int((i + j) / 2)
    if i > j:
        return 'Нет такого'
    else:
        return m


li = [0, 1, 2, 5, 10, 15, 20, 25, 40, 45]
x = int(input("Введите число: "))
print('Число:', x, '| Индекс:', BinSearch(li, x))