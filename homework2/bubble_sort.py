list = [4, 1, 5, 2, -2]
j = 1
while j < len(list):
    for i in range(len(list) - j):
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
    j = j + 1

print (list)

# Сложность O(n * n)
# Постоянное сравнение элементов
# Если i > (i + 1), меняем местами