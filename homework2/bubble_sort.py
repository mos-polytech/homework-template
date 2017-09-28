lis = [4, 1, 5, 2, -2]
j = 1
while j < len(lis):
    for i in range(len(lis) - j):
        if lis[i] > lis[i + 1]:
            lis[i], lis[i + 1] = lis[i + 1], lis[i]
    j = j + 1

print (lis)

# Сложность O(n * n)
# Постоянное сравнение элементов
# Если i > (i + 1), меняем местами
