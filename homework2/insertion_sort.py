#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sort_utils import swap


def sort(array):
    """
    Selection sort
    Complexity
        Memory
            O(n) - since all swaps "in place"
            and no addition data strictures requires
        Time
            Always O(n^2) - because no matter how array element is placed,
            second pointer go till the end

    """
    for i in range(len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j, j - 1)
            j -= 1
