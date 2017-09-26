#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sort_utils import swap
from sort_utils import shuffle


def sort(array, lo=None, hi=None):
    '''
    Quick sort
    Complexity
        Memory
            O(n) - because of using all swap operation in-place and no additional data-structure required
        Complexity
            Always O(n*log(n)), where log(n) in base of 2 - because after each recursion calls size of array is divided
                by two and we need to do n recursion calls
    '''
    # assume that function will never used like sort(array, lo=1, hi=None)
    if (lo == hi == None):
        # shuffle array to avoid O(n^2) in worst case
        shuffle(array)
        lo = 0
        hi = len(array) - 1

    if hi > lo:
        # so sorting is not completed yet
        i = _partition(array, lo, hi)
        sort(array, lo, i - 1)
        sort(array, i + 1, hi)


def _partition(array, lo, hi):
    pivot = array[hi]
    i = lo
    for j in range(lo, hi + 1):
        if array[j] < pivot:
            swap(array, i, j)
            i += 1
    swap(array, i, hi)
    return i

