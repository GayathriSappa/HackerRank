#!/bin/python3

import sys


def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    cnt_a, cnt_b = 0, 0
    for i, j in zip([a0, a1, a2], [b0, b1, b2]):
        if i > j:
            cnt_a += 1
        elif i < j:
            cnt_b += 1
        else:
            pass
    return cnt_a, cnt_b

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print(" ".join(map(str, result)))
