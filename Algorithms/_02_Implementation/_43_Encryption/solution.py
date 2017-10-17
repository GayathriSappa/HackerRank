#!/bin/python3

import sys
import textwrap
from math import sqrt, ceil
from itertools import zip_longest


s = input().strip()
s = ''.join(s.split())
w = ceil(sqrt(len(s)))

for word in zip_longest(*textwrap.wrap(s, width=w)):
    print(''.join([i for i in word if i]), end=' ')
