#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from binary_search import search as binary_search
from bubble_sort import sort as bubble_sort
from insertion_sort import sort as insertion_sort
from quick_sort import sort as quick_sort
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
        array = [-992134, 2135, 61, 0, 215, 213952135, -234, 0, 521, 324, 765, 1337, -10, -100, 52]  # noqa: ignore=E501
        bubble_sort(array)
        self.assertEqual(array, [-992134, -234, -100, -10, 0, 0, 52, 61, 215, 324, 521, 765, 1337, 2135,
                                 213952135])  # noqa: ignore=E501


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
        array = [-992134, 2135, 61, 0, 215, 213952135, -234, 0, 521, 324, 765, 1337, -10, -100, 52]  # noqa: ignore=E501
        selection_sort(array)
        self.assertEqual(array, [-992134, -234, -100, -10, 0, 0, 52, 61, 215, 324, 521, 765, 1337, 2135,
                                 213952135])  # noqa: ignore=E501


class InsertionSort(unittest.TestCase):
    def test_simple_sorting(self):
        array = [2, 3, 1]
        insertion_sort(array)
        self.assertEqual(array, [1, 2, 3])

    def test_not_positive_numbers(self):
        array = [100, 0, -10, 4, 1, -54, 9, -100]
        insertion_sort(array)
        self.assertEqual(array, [-100, -54, -10, 0, 1, 4, 9, 100])

    def test_sort_sorted_array(self):
        array = [-10, -5, 0, 5, 10]
        insertion_sort(array)
        self.assertEqual(array, [-10, -5, 0, 5, 10])

    def test_sort_empty_array(self):
        array = []
        insertion_sort(array)
        self.assertEqual(array, [])

    def test_sort_one_element_array(self):
        array = [1]
        insertion_sort(array)
        self.assertEqual(array, [1])

    def test_sort_big_arrays(self):
        array = [-992134, 2135, 61, 0, 215, 213952135, -234, 0, 521, 324, 765, 1337, -10, -100, 52]  # noqa: ignore=E501
        insertion_sort(array)
        self.assertEqual(array, [-992134, -234, -100, -10, 0, 0, 52, 61, 215, 324, 521, 765, 1337, 2135,
                                 213952135])  # noqa: ignore=E501


class QuickSort(unittest.TestCase):
    def test_simple_sorting(self):
        array = [2, 3, 1]
        quick_sort(array)
        self.assertEqual(array, [1, 2, 3])

    def test_not_positive_numbers(self):
        array = [100, 0, -10, 4, 1, -54, 9, -100]
        quick_sort(array)
        self.assertEqual(array, [-100, -54, -10, 0, 1, 4, 9, 100])

    def test_sort_sorted_array(self):
        array = [-10, -5, 0, 5, 10]
        quick_sort(array)
        self.assertEqual(array, [-10, -5, 0, 5, 10])

    def test_sort_empty_array(self):
        array = []
        quick_sort(array)
        self.assertEqual(array, [])

    def test_sort_one_element_array(self):
        array = [1]
        quick_sort(array)
        self.assertEqual(array, [1])

    def test_sort_big_arrays(self):
        array = [-992134, 2135, 61, 0, 215, 213952135, -234, 0, 521, 324, 765, 1337, -10, -100, 52]  # noqa: ignore=E501
        quick_sort(array)
        self.assertEqual(array, [-992134, -234, -100, -10, 0, 0, 52, 61, 215, 324, 521, 765, 1337, 2135,
                                 213952135])  # noqa: ignore=E501


class BinarySearch(unittest.TestCase):
    def test_search_empty_array(self):
        array = []
        self.assertEqual(None, binary_search(array, 3))

    def test_search_single_element_array(self):
        array = [1]
        self.assertEqual(0, binary_search(array, 1))

    def test_search(self):
        array = [-1034, -352, -65, -3, 0, 1, 35, 953, 9352]
        self.assertEqual(2, binary_search(array, -65))

    def test_search_when_element_is_not_there(self):
        array = [-3245, -546, -73, -9, 0, 5, 65, 732, 4742]
        self.assertEqual(None, binary_search(array, 99))


if __name__ == '__main__':
    unittest.main()
