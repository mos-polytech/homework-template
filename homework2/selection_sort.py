list = [2, 1, 0, -1, 3]
j = 0
while j < len(list) - 1:
    m = j
    i = j + 1
    while i < len(list):
        if list[i] < list[m]:
            m = i
        i += 1
    t = list[j]
    list[j] = list[m]
    list[m] = t
    j += 1

print(list)

# Сложность O(n * n)
# Ицем наименьший элемент и меняем его с
# нулевым элементом массива. И так пока не
# закончится массив.