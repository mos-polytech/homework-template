#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from bubble_sort import sort as bubble_sort
from selection_sort import sort as selection_sort


class BubbleSort(unittest.TestCase):
    def test_simple_sorting(self):
        array = [2, 3, 1]
        bubble_sort(array)
        self.assertEqual(array, [1, 2, 3])

    def test_not_positive_numbers(self):
        array = [100, 0, -10, 4, 1, -54, 9, -100]
        bubble_sort(array)
        self.assertEqual(array, [-100, -54, -10, 0, 1, 4, 9, 100])

    def test_sort_sorted_array(self):
        array = [-10, -5, 0, 5, 10]
        bubble_sort(array)
        self.assertEqual(array, [-10, -5, 0, 5, 10])

    def test_sort_empty_array(self):
        array = []
        bubble_sort(array)
        self.assertEqual(array, [])

    def test_sort_one_element_array(self):
        array = [1]
        bubble_sort(array)
        self.assertEqual(array, [1])

    def test_sort_big_arrays(self):
        array = [-992134, 2135, 61, 0, 215, 213952135, -234, 0, 521, 324, 765, 1337, -10, -100, 52]
        bubble_sort(array)
        self.assertEqual(array, [-992134, -234, -100, -10, 0, 0, 52, 61, 215, 324, 521, 765, 1337, 2135, 213952135])


class SelectionSort(unittest.TestCase):
    def test_simple_sorting(self):
        array = [2, 3, 1]
        selection_sort(array)
        self.assertEqual(array, [1, 2, 3])

    def test_not_positive_numbers(self):
        array = [100, 0, -10, 4, 1, -54, 9, -100]
        selection_sort(array)
        self.assertEqual(array, [-100, -54, -10, 0, 1, 4, 9, 100])

    def test_sort_sorted_array(self):
        array = [-10, -5, 0, 5, 10]
        selection_sort(array)
        self.assertEqual(array, [-10, -5, 0, 5, 10])

    def test_sort_empty_array(self):
        array = []
        selection_sort(array)
        self.assertEqual(array, [])

    def test_sort_one_element_array(self):
        array = [1]
        selection_sort(array)
        self.assertEqual(array, [1])

    def test_sort_big_arrays(self):
        array = [-992134, 2135, 61, 0, 215, 213952135, -234, 0, 521, 324, 765, 1337, -10, -100, 52]
        selection_sort(array)
        self.assertEqual(array, [-992134, -234, -100, -10, 0, 0, 52, 61, 215, 324, 521, 765, 1337, 2135, 213952135])


if __name__ == '__main__':
    unittest.main()
