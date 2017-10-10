#!/bin/python3

import sys


def factorial(x):
    if x < 1:
        return 1
    else:
        x = x * factorial(x-1)
        return x

n = int(input().strip())
print(factorial(n))
