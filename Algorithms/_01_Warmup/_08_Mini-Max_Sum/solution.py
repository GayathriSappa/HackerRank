#!/bin/python3

import sys
from itertools import combinations


arr = list(map(int, input().strip().split(' ')))
xs = list(map(sum, combinations(arr, len(arr) - 1)))
print(min(xs), max(xs))
