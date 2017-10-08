#!/bin/python3

import sys


s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = input().strip().split(' ')
m, n = [int(m), int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

apple_cnt = 0
orange_cnt = 0

for i in apple:
    if t >= (a + i) >= s:
        apple_cnt += 1

for j in orange:
    if s <= (b + j) <= t:
        orange_cnt += 1

print(apple_cnt)
print(orange_cnt)
