#!/bin/python3

import math
import os
import random
import re
import sys


def bubble_sort():
    for i in range(n):
        number_of_swaps = 0
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                number_of_swaps += 1
    print("Array is sorted in " + str(number_of_swaps) +  " swaps.")
    if number_of_swaps != 0:
        print("First Element: " + str(a[0]))
        print("Last Element: " + str(a[n - 1]))


if __name__ == '__main__':
    n = 3

    a = [3, 2, 1]
    bubble_sort()
    print(a)

    # Write your code here
