#!/bin/python3

import sys


def getRecord(s):
    # Complete this function
    cnt_min, cnt_max = 0, 0
    min_value, max_value = s[0], s[0]
    for i in s:
        if i < min_value:
            cnt_min += 1
            min_value = i
        if i > max_value:
            cnt_max += 1
            max_value = i
    return cnt_max, cnt_min

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print(" ".join(map(str, result)))
