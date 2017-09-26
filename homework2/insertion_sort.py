def input_arr(num):
    arr = []
    for i in range(0, num):
        current_elem = float(input('Введите ' + str(i) + ' элемент массива: '))
        arr.append(current_elem)

    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        item = i - 1
        while item >= 0 and arr[item] > temp:
            arr[item + 1], arr[item] = arr[item], temp
            item -= 1

    return arr


arr = input_arr(int(input('Введите размер массива: ')))
print(insertion_sort(arr))
"""""
Сложность O(n^2)
Малоэффективный алгоритм(сравнимый с алгоритмом сортировки пузырьком)
Создаются подмассивы(начиная с нулевого элемента) и постоянно сравниваются с новым элементом
После чего меняются местами(при необходимости)
Пример:
1 3 2 5 - исходный массив
1
1 3
1 3 2
1 3 <-> 2
1 2 3 5
"""""