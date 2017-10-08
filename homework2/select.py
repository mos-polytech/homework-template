def select_sort_stable(arr):
    """
    Эта сортировка уже сложней.
    ПРишлось гуглить и понимать логику алгоритма на примере языка php
    Не совсем понятна логика данного алгоритма и для чего ее использовать если есть алгоритм сортировки легче и проще
    :param arr:
    :return:
    """
    if len(arr) == 0:
        return

    for j in range(len(arr)):
        my_min = j

        for i in range(j + 1, len(arr)):
            if arr[i] < arr[my_min]:
                my_min = i

        if my_min != j:
            value = arr[my_min]

            for l in range(my_min, j - 1, -1):
                arr[l] = arr[l - 1]

            arr[j] = value

    return arr


if __name__ == '__main__':
    my_arr1 = [3, 2, 1, 4, 0, 5]
    result = select_sort_stable(my_arr1)
    print(result)
