mass = [1, 2, 10, 14, 15, 21, 27, 30, 100, 510, 520, 538]
print(mass)
print('Выберите число из данного массива:')
a = int(input())
i = 0
j = len(mass) - 1
x = int(j / 2)
while mass[x] != a and i < j:
    if a > mass[x]:
        i = x + 1
    else:
        j = x - 1
    x = int((i + j) / 2)

if i > j:
    print('Число не найдено!')
else:
    print('Индекс числа ', a, ': ', x)
# Сложность алгоритма - O(log n).
# Поиск нужного значения упорядоченного массива начинается с определения значения центрального элемента
# Значение данного элемента сравнивается с искомым значением и в зависимости от результатов
# сравнения предпринимаются определенные действия.
# Если искомое и центральное значения оказываются равны, то поиск завершается успешно.
# Если искомое значение меньше/больше центрального, то формируется массив из элементов,
# находящихся слева/справа от центрального соответственно. 
# Затем поиск повторяется в новом массиве.
