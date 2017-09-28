mass = [-9, 2, -1, 1, 5, 8, 7, 6, -4]
print('Исходный массив:', mass)
for i in range(1, len(mass)):
    a = mass[i]
    j = i-1
    while j >= 0:
        if a < mass[j]:
            mass[j+1] = mass[j]
            mass[j] = a
            j = j - 1
        else:
            break
print('Отсортированный массив:', mass)
# Сложность алгоритма - O(n^2). 
# 1ый элемент массива считается отсортированным, все остальные — не отсортированные. 
# Начиная со 2го элемента массива, алгоритм вставляет неотсортированный элемент в нужную позицию в отсортированной части. 
# Cледовательно, за 1 шаг сортировки отсортированная часть  увеличивается на 1 элемент, а неотсортированная - уменьшается на 1 элемент.
