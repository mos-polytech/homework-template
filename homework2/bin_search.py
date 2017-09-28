# Сложность : O(lg(n))
# Бинарный поиск работает таким образом, что сначала находится 
# реднее значение в массиве и сравнивается с нашим искомым элементом, 
# если наш элемент оказался меньше, то поиск продолжаем слева от середины массива, 
# и такие операцию выполняем до тех пор, пока наш элемент не будет равен элементу массива, 
# если равен - выводим индекс ячейки массива, в котором лежит этот элемент. 



def bin_search(arr, x):
    i = 0
    j = len(arr) - 1
    while i < j:
        m = int((i + j) / 2)
        if x > arr[m]:
            i = m + 1
        else:
            j = m

        if arr[j] == x:
            return j
        else:
            return None

arr = [input() for i in range(int(input()))]
x = input('Введите число для поиска\n')
print(bin_search(arr, x))