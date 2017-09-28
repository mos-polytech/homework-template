lis = [2, 1, 0, -1, 3]
j = 0
while j < len(lis) - 1:
    m = j
    i = j + 1
    while i < len(lis):
        if lis[i] < lis[m]:
            m = i
        i += 1
    t = lis[j]
    lis[j] = lis[m]
    lis[m] = t
    j += 1

print(lis)

# Сложность O(n * n)
# Ицем наименьший элемент и меняем его с
# нулевым элементом массива. И так пока не
# закончится массив.
