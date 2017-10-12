#!/bin/python3

import sys
import re


q = int(input().strip())
regexp = re.compile(r'\w*h\w*a\w*c\w*k\w*e\w*r\w*r\w*a\w*n\w*k\w*')
for a0 in range(q):
    s = input().strip()
    # your code goes here
    print('YES' if re.match(regexp, s) else 'NO')
