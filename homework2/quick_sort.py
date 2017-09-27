def quick_sort(array, bottom=None, top=None):
    '''
    Сложность: кажджый раз рассматриваемый массив уменьшается вдвое,
    поэтому функция quick_sort сработает ~ lg(n) раз (см. binary_search).

    Каждый раз quick_sort вызывает функцию partition, которая за один
    пробег по подмассиву расскидывает элементы относительно последнего
    (те, что меньше - влево, те что больше - вправо).
    То есть, получается O(n * lg(n))
    '''

    if bottom is None or top is None:
        bottom = 0
        top = len(array) - 1

    if bottom >= top:
        return

    delimiter = partition(array, bottom=bottom, top=top)

    quick_sort(array, bottom=bottom, top=delimiter-1)
    quick_sort(array, bottom=delimiter+1, top=top)


def partition(array, bottom=None, top=None):
    support_index = bottom

    for i in range(bottom, top+1):
        if array[i] < array[top]:
            array[i], array[support_index] = array[support_index], array[i]
            support_index += 1

    array[top], array[support_index] = array[support_index], array[top]

    return support_index

if __name__ == '__main__':
    arr = [7, 2, 1, 4, 8, 9, 5, 3]
    quick_sort(arr)
    print(arr)
