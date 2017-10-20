#!/bin/python3

import sys


def super_reduced_string(s):
    # Complete this function
    stack = []
    for i in range(len(s)):
        if stack:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
    return ''.join(stack) if stack else 'Empty String'

s = input().strip()
result = super_reduced_string(s)
print(result)
