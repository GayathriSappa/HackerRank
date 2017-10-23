#!/bin/python3

import sys


def bonAppetit(n, k, b, ar):
    # Complete this function
    actual = 0
    for i in range(n):
        if i != k:
            actual += ar[i]
    difference = b - actual / 2
    return difference if difference else 'Bon Appetit'

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
