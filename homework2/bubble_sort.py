# сложность O(n * n)
# Суть состоит в том, что мы , начиная с нулевого элемента,
# сравниваем рядом стоящие элементы до тех пор, пока
# массив не будет отсортирован. После первой же итрации
# максимальный элемент "всплывет" на конец массива.


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                a = array[j]
                array[j] = array[j + 1]
                array[j + 1] = a


if __name__ == '__main__':
    arr = [input() for i in range(int(input()))]
    bubble_sort(arr)
    print(arr)
