#!/bin/python3

import sys
from collections import Counter


def birthdayCakeCandles(n, ar):
    # Complete this function
    c = Counter(ar)
    count_tallest_candles = sorted(c.values(), reverse=True)
    return count_tallest_candles[0]


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
