#!/bin/python3

import sys
from collections import Counter


def migratoryBirds(n, ar):
    # Complete this function
    c = Counter(ar)
    return sorted(c.items(), key=lambda i: (i[1], -i[0]), reverse=True)[0][0]

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
