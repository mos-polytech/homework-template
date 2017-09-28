# Сложность O(n^2)
# Берем каждый элемент массива, начиная с нулевого элемента, и постоянно сравниваем с остальными элементами, при необходимости меняем местами. Когда мы дойдем до середины слева будет отсортированная часть, а справа неотсортированная 

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i - 1
        while j >= 0 and array[j] > array[j + 1]:
            a = array[j]
            array[j] = array[j+1]
            array[j+1] = a
            j -= 1


if __name__ == '__main__':
    arr = [input() for i in range(int(input()))]
    insertion_sort(arr)
    print(arr)
