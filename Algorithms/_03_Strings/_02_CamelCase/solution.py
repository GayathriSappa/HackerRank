#!/bin/python3

import sys
import re


s = input().strip()
regexp = re.compile(r'[A-Z]')
print(len(re.split(regexp, s)))





