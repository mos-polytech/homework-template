

def search(array, element):
    if len(array) == 0 or (len(array) == 1 and array[0] != element):
        return -1
    middle = len(array) // 2
    if array[middle] > element:
        return search(array[:middle], element)
    elif array[middle] < element:
        return search(array[middle:], element)
    else:
        return middle
