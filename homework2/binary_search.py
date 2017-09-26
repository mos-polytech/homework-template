

def search(array, element):
    current_array = array
    while not _element_absent(current_array, element):
        middle = len(current_array) // 2
        if current_array[middle] > element:
            current_array = current_array[:middle]
        elif current_array[middle] < element:
            current_array = current_array[middle:]
        else:
            return middle
    return -1

def _element_absent(array, element):
    return len(array) == 0 or (len(array) == 1 and array[0] != element)
