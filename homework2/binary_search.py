#!/usr/bin/env python
# -*- coding: utf-8 -*-


def search(array, element):
    """
    Binary search
    Complexity
    Memory
        O(n) - since no additional data structure used
    Time
        Always Log(n) with base 2 - because after every comparison,
        length of array divided by 2
    :param array: sorted (!) number array
    :param element: number to search
    :return: position of element (or None when element is not in array)
    """
    current_array = array
    while not _element_absent(current_array, element):
        middle = len(current_array) // 2
        if current_array[middle] > element:
            current_array = current_array[:middle]
        elif current_array[middle] < element:
            current_array = current_array[middle:]
        else:
            return middle
    return None


def _element_absent(array, element):
    return len(array) == 0 or (len(array) == 1 and array[0] != element)
