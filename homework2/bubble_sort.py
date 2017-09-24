#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sort_utils import swap


def sort(array):
    """
    Bubble sort
    Complexity
        Memory
            O(n) - use same array and swap "in place"
        Time
            Worst: O(n^2) - when array is reversed
                ((n - 1) + (n - 2) + ... + (n - n))/2 ~ O(n^2)
            Average: O(n^2)
            Best: ϴ(n) - when array is sorted
    """
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1):
            if (array[i] > array[i + 1]):
                is_sorted = False
                swap(array, i, i + 1)
