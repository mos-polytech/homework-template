def sort2(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                min_element = array[j]
        array[j] = array[i]
        array[i] = min_element
        return array

arr=[4, 9, 7, 6, 2, 3]
print(sort2(arr))

# Сложность O(n^2)
# Алгоритм выбирает минимальный элемент массива
# Затем он проходит весь массив и ищет следующий минимальный элемент
# И ставит его после первого.
# Таким образом после серии проходов массив будет отсортирован.
# При худшей ситуации алгоритму придётся совершить O(n^2) операций.