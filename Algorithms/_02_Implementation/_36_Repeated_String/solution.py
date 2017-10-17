#!/bin/python3

import sys


s = input().strip()
n = int(input().strip())

repeat, remainder = divmod(n, len(s))
cnt = s.count('a') * repeat + s[:remainder].count('a')
print(cnt)
