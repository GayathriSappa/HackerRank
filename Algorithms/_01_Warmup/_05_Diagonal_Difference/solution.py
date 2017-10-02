#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

primary_diagonal_values, secondary_diagonal_values = 0, 0
left, right = 0, n - 1

for i in a:
    primary_diagonal_values += i[left]
    secondary_diagonal_values += i[right]
    left += 1
    right -= 1

print(abs(primary_diagonal_values - secondary_diagonal_values))
