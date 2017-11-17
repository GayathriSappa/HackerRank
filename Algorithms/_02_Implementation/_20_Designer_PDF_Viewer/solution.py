#!/bin/python3

import sys


h = list(map(int, input().strip().split(' ')))
word = input().strip()

maximum_height = 0
for char in word:
    height = h[ord(char)-97]
    if height > maximum_height:
        maximum_height = height

area = len(word) * 1 * maximum_height
print(area)
