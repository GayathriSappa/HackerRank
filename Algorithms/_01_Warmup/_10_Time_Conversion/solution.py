#!/bin/python3

import sys
import time

def timeConversion(s):
    # Complete this function
    t = time.strptime(s, "%I:%M:%S%p")
    return time.strftime("%H:%M:%S", t)


s = input().strip()
result = timeConversion(s)
print(result)
