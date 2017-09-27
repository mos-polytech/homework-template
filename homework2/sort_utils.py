#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

def swap(array, i, j):
    if (i != j):
        array[i], array[j] = array[j], array[i]


def shuffle(array):
    for i in range(0, len(array)):
        index = randint(0, i)
        swap(array, i, index)
