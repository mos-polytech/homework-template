mass = [3, -5, 2, 4, 0, 9, -6, 7, 1]
print('Исходный массив:', mass)
n = len(mass)
m = n-1
while m > 0:
    for i in range(m):
        if mass[i] > mass[i+1]:
            x = mass[i]
            mass[i] = mass[i+1]
            mass[i+1] = x
    m = m-1
print('Отсортированный массив:', mass)
# Сложность алгоритма-O(n^2).
# Алгоритм сортировки пузырьком сводится к повторению проходов по элементам сортируемого массива.
# Проход по элементам выполняет внутренний цикл.
# За каждый проход сравниваются 2 соседних элемента, если порядок неверный элементы меняются местами.
# Внешний цикл работает, до тех пор, пока массив не будет отсортирован.
# Когда при очередном проходе по элементам не будет совершено ни одной перестановки, то массив будет отсортированным